#!/usr/bin/env python3
"""Baja playlists, biblioteca y top tracks de Spotify a data/spotify/.

Corre en la Mac, no en la nube. Solo lee, nunca modifica la cuenta.

Antes de la primera corrida:
  1. Entrar a https://developer.spotify.com/dashboard y crear una app.
  2. En Redirect URIs poner exactamente:  http://127.0.0.1:8888/callback
  3. Copiar Client ID y Client Secret a scripts/.env (ver .env.example).

Uso:
    python3 scripts/sync_spotify.py

La primera vez abre el navegador para autorizar. Despues guarda un refresh
token en scripts/.spotify_token.json y ya no vuelve a preguntar.
"""
import base64
import http.server
import json
import pathlib
import secrets
import threading
import urllib.parse
import urllib.request
import webbrowser

ROOT = pathlib.Path(__file__).resolve().parent.parent
ENV = ROOT / "scripts" / ".env"
TOKEN_FILE = ROOT / "scripts" / ".spotify_token.json"
OUT = ROOT / "data" / "spotify"
REDIRECT = "http://127.0.0.1:8888/callback"
SCOPES = "playlist-read-private playlist-read-collaborative user-library-read user-top-read user-read-recently-played"
API = "https://api.spotify.com/v1"


def load_env() -> tuple[str, str]:
    if not ENV.exists():
        raise SystemExit(f"Falta {ENV}. Copiá .env.example y completá las credenciales.")
    vals = {}
    for line in ENV.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            vals[k.strip()] = v.strip().strip('"').strip("'")
    return vals["SPOTIFY_CLIENT_ID"], vals["SPOTIFY_CLIENT_SECRET"]


def post_token(cid: str, secret: str, payload: dict) -> dict:
    auth = base64.b64encode(f"{cid}:{secret}".encode()).decode()
    req = urllib.request.Request(
        "https://accounts.spotify.com/api/token",
        data=urllib.parse.urlencode(payload).encode(),
        headers={"Authorization": f"Basic {auth}", "Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def authorize(cid: str, secret: str) -> dict:
    state = secrets.token_urlsafe(16)
    got: dict = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            got.update({k: v[0] for k, v in q.items()})
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<h2>Listo. Volvé a la terminal.</h2>".encode())

        def log_message(self, *a):
            pass

    srv = http.server.HTTPServer(("127.0.0.1", 8888), Handler)
    threading.Thread(target=srv.handle_request, daemon=True).start()

    url = "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(
        {"client_id": cid, "response_type": "code", "redirect_uri": REDIRECT, "scope": SCOPES, "state": state}
    )
    print("Abriendo el navegador para autorizar...")
    webbrowser.open(url)
    while "code" not in got and "error" not in got:
        pass
    if got.get("state") != state:
        raise SystemExit("State no coincide. Abortado por seguridad.")
    if "error" in got:
        raise SystemExit(f"Spotify devolvió error: {got['error']}")

    tok = post_token(cid, secret, {"grant_type": "authorization_code", "code": got["code"], "redirect_uri": REDIRECT})
    TOKEN_FILE.write_text(json.dumps(tok, indent=2))
    return tok


def access_token() -> str:
    cid, secret = load_env()
    if TOKEN_FILE.exists():
        tok = json.loads(TOKEN_FILE.read_text())
        fresh = post_token(cid, secret, {"grant_type": "refresh_token", "refresh_token": tok["refresh_token"]})
        tok.update(fresh)
        TOKEN_FILE.write_text(json.dumps(tok, indent=2))
        return tok["access_token"]
    return authorize(cid, secret)["access_token"]


def get(path: str, token: str, **params) -> dict:
    url = f"{API}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def paged(path: str, token: str, limit: int = 50, cap: int = 2000, **params) -> list:
    items, offset = [], 0
    while offset < cap:
        page = get(path, token, limit=limit, offset=offset, **params)
        batch = page.get("items", [])
        items.extend(batch)
        if len(batch) < limit:
            break
        offset += limit
    return items


def main() -> int:
    token = access_token()
    OUT.mkdir(parents=True, exist_ok=True)

    me = get("/me", token)
    print(f"Conectado como {me.get('display_name')} ({me.get('id')})")

    playlists = paged("/me/playlists", token)
    detalle = []
    for p in playlists:
        tracks = paged(f"/playlists/{p['id']}/tracks", token, limit=100)
        detalle.append(
            {
                "nombre": p["name"],
                "id": p["id"],
                "propia": p["owner"]["id"] == me["id"],
                "descripcion": p.get("description"),
                "total": p["tracks"]["total"],
                "tracks": [
                    {
                        "titulo": (t.get("track") or {}).get("name"),
                        "artistas": [a["name"] for a in (t.get("track") or {}).get("artists", [])],
                        "album": ((t.get("track") or {}).get("album") or {}).get("name"),
                        "agregado": t.get("added_at"),
                    }
                    for t in tracks
                    if t.get("track")
                ],
            }
        )
        print(f"  {p['name']}: {p['tracks']['total']}")
    (OUT / "playlists.json").write_text(json.dumps(detalle, ensure_ascii=False, indent=2), encoding="utf-8")

    for rango in ("short_term", "medium_term", "long_term"):
        for tipo in ("artists", "tracks"):
            data = get(f"/me/top/{tipo}", token, limit=50, time_range=rango)
            (OUT / f"top_{tipo}_{rango}.json").write_text(
                json.dumps(data.get("items", []), ensure_ascii=False, indent=2), encoding="utf-8"
            )

    saved = paged("/me/tracks", token)
    (OUT / "saved_tracks.json").write_text(json.dumps(saved, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n{len(detalle)} playlists, {len(saved)} temas guardados -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

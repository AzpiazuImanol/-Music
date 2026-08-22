#!/usr/bin/env python3
"""Extrae una playlist de YouTube a data/youtube-sets.json y docs/biblioteca.

Uso:
    python3 scripts/sync_youtube.py "https://www.youtube.com/playlist?list=..."

Necesita yt-dlp (brew install yt-dlp). Corre en la Mac, no en la nube.
No descarga audio: solo lee los metadatos de la playlist.
"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_JSON = ROOT / "data" / "youtube-sets.json"


def fetch(url: str) -> list[dict]:
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--dump-single-json",
        "--no-warnings",
        url,
    ]
    raw = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    data = json.loads(raw)
    sets = []
    for e in data.get("entries", []):
        if not e:
            continue
        sets.append(
            {
                "id": e.get("id"),
                "titulo": e.get("title"),
                "canal": e.get("uploader") or e.get("channel"),
                "duracion_s": e.get("duration"),
                "url": f"https://www.youtube.com/watch?v={e.get('id')}",
            }
        )
    return sets


def hhmm(seconds) -> str:
    if not seconds:
        return "?"
    h, rem = divmod(int(seconds), 3600)
    return f"{h}h{rem // 60:02d}" if h else f"{rem // 60}m"


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    sets = fetch(sys.argv[1])
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(
        json.dumps({"playlist": sys.argv[1], "sets": sets}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    total = sum(s["duracion_s"] or 0 for s in sets)
    print(f"{len(sets)} sets, {hhmm(total)} en total -> {OUT_JSON}")

    canales: dict[str, int] = {}
    for s in sets:
        canales[s["canal"] or "?"] = canales.get(s["canal"] or "?", 0) + 1
    print("\nCanales que mas se repiten:")
    for canal, n in sorted(canales.items(), key=lambda kv: -kv[1])[:12]:
        print(f"  {n:>3}  {canal}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

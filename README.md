# Music

Repo de música para comprender mis gustos y armar potencialmente playlists,
avisar cuando se lanzan nuevos tracks que no haya escuchado, y decirme cuando
artistas que me gustan están por tocar en zonas cercanas a donde estoy.

## Cómo se usa desde el teléfono

App de Claude en el iPhone, sección Code, sesión sobre este repo. Claude lee y
escribe los archivos de `docs/` y commitea. **El estado vive en los archivos**,
no en el chat: cada sesión en la nube arranca en blanco y lo único que sobrevive
es lo que quedó escrito acá.

## Qué hay adentro

| Archivo | Para qué |
|---|---|
| [docs/perfil-de-gusto.md](docs/perfil-de-gusto.md) | La fuente de verdad. Sin esto, toda recomendación es genérica. |
| [docs/descubrimiento.md](docs/descubrimiento.md) | Qué se recomendó y qué veredicto tuvo. Evita repetir. |
| [docs/biblioteca.md](docs/biblioteca.md) | 61 sets de YouTube, 98h43. Y Spotify cuando entre. |
| [docs/lanzamientos.md](docs/lanzamientos.md) | Radar de releases nuevos. |
| [docs/shows.md](docs/shows.md) | Radar de shows cerca. Cambridge desde el 25-ago-2026. |
| [docs/playlists.md](docs/playlists.md) | Playlists armadas. |
| [docs/caidos.md](docs/caidos.md) | Sets que desaparecieron de YouTube y por qué. |
| [docs/radio.md](docs/radio.md) | Delta 90.3: URL del stream verificada y cómo escucharla. |

## Los pulls de datos

Corren **en la Mac**, no en la nube, porque necesitan las cuentas y las
herramientas locales. Dejan los resultados en `data/`, que sí se commitea, y
desde ahí la sesión del teléfono los lee.

### YouTube

```bash
python3 scripts/sync_youtube.py "https://youtube.com/playlist?list=PLOTKlTPiFbufKT4orxatE6nD857bWIHLE"
```

Necesita `yt-dlp`. No baja audio, solo metadatos. Escribe
`data/youtube-sets.json` e imprime qué canales se repiten más.

### Spotify

No existe conector de Spotify para Claude, así que la vía es la API oficial.
Una sola vez:

0. **Hace falta Spotify Premium.** Desde febrero de 2026 el Development Mode lo
   exige. Ver [docs/api-spotify.md](docs/api-spotify.md).
1. Crear una app en <https://developer.spotify.com/dashboard> con el botón
   *Create app* (está en el Dashboard, no en la home de developer.spotify.com).
2. En *Redirect URIs* poner exactamente `http://127.0.0.1:8888/callback`.
3. Copiar `scripts/.env.example` a `scripts/.env` y pegar Client ID y Secret.

Después:

```bash
python3 scripts/sync_spotify.py
```

Baja playlists con sus temas, top de artistas y temas en tres ventanas
temporales, y los guardados. Solo lectura: nunca modifica la cuenta. Las
credenciales y el token están en `.gitignore`.

**Este repo es público.** Cuando corras el sync, tu historial de escucha de
Spotify queda visible para cualquiera. Si eso molesta, pasá el repo a privado
antes de correrlo.

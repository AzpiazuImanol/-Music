# musica

Sesión dedicada de música. Vive en un repo para poder abrirla desde el iPhone
con Claude Code en la nube, igual que `Depto_Rosales`.

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
| [docs/biblioteca.md](docs/biblioteca.md) | Playlists de Spotify y sets de YouTube. |
| [docs/shows-uk.md](docs/shows-uk.md) | Radar de conciertos en Cambridge y Londres. |
| [docs/radio.md](docs/radio.md) | Delta 90.3: URL del stream verificada y cómo escucharla. |

## Los pulls de datos

Corren **en la Mac**, no en la nube, porque necesitan las cuentas y las
herramientas locales. Dejan los resultados en `data/`, que sí se commitea, y
desde ahí la sesión del teléfono los lee.

### YouTube

```bash
python3 scripts/sync_youtube.py "https://www.youtube.com/playlist?list=TU_PLAYLIST"
```

Necesita `yt-dlp` (ya instalado). No baja audio, solo metadatos. Escribe
`data/youtube-sets.json` e imprime qué canales se repiten más.

### Spotify

No existe conector de Spotify para Claude, así que la vía es la API oficial.
Una sola vez:

1. Crear una app en <https://developer.spotify.com/dashboard>.
2. En *Redirect URIs* poner exactamente `http://127.0.0.1:8888/callback`.
3. Copiar `scripts/.env.example` a `scripts/.env` y pegar Client ID y Secret.

Después, cada vez que quieras refrescar los datos:

```bash
python3 scripts/sync_spotify.py
```

Baja playlists con sus temas, top de artistas y temas en tres ventanas
temporales, y los guardados. Solo lectura: nunca modifica la cuenta. Las
credenciales y el token están en `.gitignore`.

La alternativa sin API es pedir el export de datos en Spotify (*Privacy
Settings > Download your data*), pero tarda días y trae el historial crudo sin
la estructura de playlists.

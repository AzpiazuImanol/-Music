# El régimen de la API de Spotify desde febrero 2026

Spotify publicó el 6-feb-2026 "Update on Developer Access and Platform Security"
y recortó fuerte el Development Mode, que es el modo en el que va a correr este
repo. Verificado contra la documentación oficial el 27-ago-2026.

## Las reglas nuevas

- **Requiere cuenta Spotify Premium activa del dueño de la app.** Sin Premium no
  hay Development Mode.
- **Un solo Client ID de Development Mode por desarrollador.**
- **Hasta 5 usuarios autorizados por Client ID.** Para uso personal sobra.
- Acceso limitado a un subconjunto de endpoints.

Fechas: rige para Client IDs nuevos desde el 11-feb-2026, y para los existentes
desde el 9-mar-2026. O sea que hoy aplica a todo.

## Qué sobrevive y sirve para este repo

| Endpoint | Para qué |
|---|---|
| `GET /me/playlists` | Listar sus playlists |
| `GET /playlists/{id}/items` | El contenido de cada una |
| `GET /me/top/{artists,tracks}` | Top en tres ventanas temporales |
| `GET /me/tracks` | Temas guardados |
| `GET /me/player/recently-played` | Lo último que escuchó |
| `GET /artists/{id}/albums` | Releases de un artista |
| `POST /me/playlists` | Crear playlist para el usuario logueado |

## Qué se rompió, y qué significa acá

**`GET /playlists/{id}/tracks` fue renombrado a `/items`, y el contenido de
cada item también cambió de nombre.** Esto último no está en el changelog y
costó un bug: dentro de cada item, el objeto del tema **ya no está en `track`
sino en `item`**, y `track` pasó a ser un booleano que indica si es tema o
episodio. Un filtro tipo `if item.get("track")` no falla: devuelve cero temas en
silencio, que es peor. El campo `tracks` del
objeto playlist ahora se llama `items`, y **puede venir vacío para playlists que
no son suyas**. `scripts/sync_spotify.py` ya está patcheado para las dos cosas.

**`GET /browse/new-releases` fue eliminado sin reemplazo.** Esto pega directo en
[lanzamientos.md](lanzamientos.md): no hay más feed global de novedades. La vía
que queda es recorrer `/artists/{id}/albums` artista por artista y comparar
contra el estado anterior. Para su caso funciona igual, porque lo que quiere es
enterarse de **sus** artistas, no de todos.

**`POST /users/{user_id}/playlists` fue eliminado**, reemplazado por
`POST /me/playlists`. Crear playlists sigue siendo posible, pero requiere el
scope `playlist-modify-private`, que el script hoy **no pide a propósito**: es
solo lectura. Cuando se decida armar playlists de verdad, hay que agregarlo.

**Campos eliminados de las respuestas.** Verificado contra la data real del
27-ago-2026: un objeto artista hoy trae solo `external_urls`, `href`, `id`,
`images`, `name`, `type` y `uri`. Desaparecieron `genres`, `popularity`,
`followers` y `available_markets`.

Lo grave de esa lista es **`genres`**: Spotify ya no dice a qué género pertenece
un artista. Cualquier clasificación por estilo en este repo tiene que salir de
otra fuente (MusicBrainz, Last.fm, o a mano). Y no se puede rankear por
`popularity`, que era lo natural.

**Las playlists seguidas devuelven 403.** Confirmado en la corrida: de sus 42
playlists, las 17 que sigue pero no son suyas dan 403 al pedir el contenido. El
script lo maneja y sigue de largo, pero significa que **solo se puede leer el
contenido de las playlists propias**.

## Lo que no cambia

El radar de shows no toca Spotify: sale de Resident Advisor, Dice y Songkick.
Y la mitad YouTube del consumo tampoco se ve afectada.

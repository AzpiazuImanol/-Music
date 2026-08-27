# Playlists

Objetivo: armarle playlists a partir del perfil de gusto.

## Dos productos, no uno

Escucha en dos modos con plataforma propia cada uno: **temas sueltos en Spotify,
sets en YouTube**. Entonces hay dos productos distintos y conviene no mezclarlos:

- **Colas de sets, en YouTube.** Una lista de sets ordenados para un contexto
  (cocinar, trabajar, el tren a Londres). Es el modo dominante.
- **Playlists de temas, en Spotify.** Para cuando no puede poner algo de 90
  minutos, y para descubrir artistas nuevos tema por tema.

Ninguno reemplaza al otro. Antes de armar algo, definir para cuál de los dos es.

## Estado

Nada armado todavía. Para las de Spotify hace falta correr
`scripts/sync_spotify.py` primero, para no armar algo que ya tiene.

Nota técnica: el script actual es **solo lectura**. Crear playlists en su cuenta
sigue siendo posible después de los recortes de febrero de 2026, pero cambió de
endpoint (`POST /me/playlists`, ya no `/users/{id}/playlists`) y requiere el
scope `playlist-modify-private`, que hoy no pide a propósito. Ver
[api-spotify.md](api-spotify.md).

## Armadas

| Nombre | Tipo | Contexto | Temas / sets | Fecha |
|---|---|---|---|---|

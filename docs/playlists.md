# Playlists

Objetivo: armarle playlists a partir del perfil de gusto.

## El problema de formato

Su consumo real son sets de 90 minutos, no listas de temas. Una playlist de
Spotify de 40 canciones no reemplaza eso. Entonces hay dos productos distintos y
conviene no mezclarlos:

- **Colas de sets.** Una lista de sets de YouTube ordenados para un contexto
  (cocinar, trabajar, el tren a Londres). Es lo más cerca de lo que ya hace.
- **Playlists de temas de Spotify.** Sirven para lo que el set no cubre:
  descubrir un artista nuevo, o escuchar cuando no puede poner algo de 90
  minutos.

## Estado

Nada armado todavía. Para las de Spotify hace falta correr
`scripts/sync_spotify.py` primero, para no armar algo que ya tiene.

Nota técnica: el script actual es **solo lectura**. Crear playlists en su cuenta
requiere el scope `playlist-modify-private`, que hoy no pide a propósito.

## Armadas

| Nombre | Tipo | Contexto | Temas / sets | Fecha |
|---|---|---|---|---|

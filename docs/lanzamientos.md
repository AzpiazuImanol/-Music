# Radar de lanzamientos

Objetivo: avisarle cuando sale algo nuevo de lo que le gusta y todavía no
escuchó.

## Qué se vigila

Por el perfil de gusto, hay que vigilar **dos cosas distintas**, y la segunda
suele quedar afuera de los radares normales:

1. **Artistas.** Los del núcleo duro de [perfil-de-gusto.md](perfil-de-gusto.md).
2. **Series y canales.** Cercle, Mayan Warrior, Boiler Room, Awakenings,
   Anjunadeep, This Never Happened, Flavour Trip, Tomorrowland. El 28% de su
   playlist es Cercle, así que un set nuevo de la serie le interesa aunque el
   artista le sea desconocido.

## Estado

| Fuente | Qué avisa | Cómo se consulta | Andando |
|---|---|---|---|
| YouTube (canales) | Sets nuevos de las series | `yt-dlp` sobre cada canal, comparando contra `data/youtube-sets.json` | no |
| Spotify (artistas) | Releases nuevos del núcleo | `/artists/{id}/albums` de la Web API | no, falta la app |
| Beatport / Bandcamp | Lanzamientos de sello | por definir | no |

## Cómo se convierte en aviso real

**Una sesión de Claude, en la nube o en la Mac, no corre sola.** Para que esto
sea un aviso y no algo que hay que ir a mirar, hace falta un trabajo programado
que corra solo, compare contra el último estado y avise por algún canal.

El mecanismo está por definir con él. Opciones reales, en orden de fricción:

- **Digest semanal por mail.** El patrón que ya usa para el informe de
  inversiones de los domingos. Bajo ruido, y llega igual al teléfono.
- **Agente programado en la nube** sobre este repo, que commitea las novedades
  acá y notifica.
- **Recordatorio en Apple Reminders**, que es notificación real en el iPhone.

## Novedades detectadas

| Fecha | Qué salió | Fuente | Avisado | Veredicto |
|---|---|---|---|---|

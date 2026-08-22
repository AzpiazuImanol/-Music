# Sesión de música

Este repo es la sesión dedicada de música de Imanol. Vive acá para que él pueda
abrirla desde el iPhone con Claude Code en la nube, igual que `Depto_Rosales`.

## Cómo trabajar acá

**El estado vive en archivos, no en la conversación.** Toda recomendación,
veredicto o show que aparezca en un chat tiene que terminar escrito en el
archivo que corresponda y commiteado. Si no se escribe, se pierde: cada sesión
en la nube arranca sin memoria de la anterior.

**Antes de recomendar, leé `docs/perfil-de-gusto.md`.** Es la fuente de verdad.
Si todavía está en su estado inicial (sin datos), la primera tarea es
interrogarlo para llenarlo, no improvisar recomendaciones genéricas.

**Nunca recomiendes algo que ya está en `docs/descubrimiento.md`.** Ese archivo
existe justamente para eso.

## Los tres alcances

1. **Descubrimiento**: artistas y discos nuevos. Salida a `docs/descubrimiento.md`.
2. **Biblioteca y playlists**: ordenar lo que ya tiene. Spotify y sets de YouTube.
   Salida a `docs/biblioteca.md`, datos crudos en `data/`.
3. **Shows y agenda UK**: conciertos y festivales en Cambridge y Londres.
   Salida a `docs/shows-uk.md`. Se muda a Cambridge el 25-ago-2026.

Fuera de alcance: todo lo demás. Otros temas tienen sus propias sesiones.

## Cómo le gusta que le hablen

- Interrogarlo en opción múltiple antes de producir, siempre con salida "Otro".
- No usar guiones (— ni -) como conectores. Suena a texto generado.
- Directo y corto. Nada de contenido que no pidió.
- Si él ya redactó algo, usar su texto casi literal en vez de reescribirlo.

## Lo que esta sesión NO puede hacer

Corriendo en la nube no tiene acceso a la cuenta de Spotify ni de YouTube de
Imanol, ni a su Mac. Los pulls de datos los corre él desde la Mac con los
scripts de `scripts/`, que dejan los resultados en `data/`. Desde el teléfono
esta sesión lee esos archivos y busca en la web, nada más.

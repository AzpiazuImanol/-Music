# Sesión de música

Repo de música de Imanol. Vive acá para poder abrirlo desde el iPhone con Claude
Code en la nube, igual que `Depto_Rosales`.

Lo que quiere de este repo, en sus palabras: comprender sus gustos, armar
potencialmente playlists, avisarle cuando se lanzan tracks nuevos que no haya
escuchado, y decirle cuándo artistas que le gustan están por tocar cerca de
donde está.

## Cómo trabajar acá

**El estado vive en archivos, no en la conversación.** Toda recomendación,
veredicto, novedad o show que aparezca en un chat tiene que terminar escrito en
el archivo que corresponda y commiteado. Cada sesión en la nube arranca sin
memoria de la anterior.

**Antes de recomendar, leé [`docs/perfil-de-gusto.md`](docs/perfil-de-gusto.md).**

**Las dos reglas que salen del perfil y que es fácil violar:**

1. **Toda recomendación declara su canal.** Escucha en dos modos con plataforma
   propia: **temas sueltos en Spotify, sets en YouTube**, los dos con
   frecuencia y con tendencia hacia YouTube. Un set se recomienda con link de
   YouTube y completo, nunca un extracto. Un tema se recomienda en Spotify.
   No hay formato "correcto": hay dos, y confundirlos es el error.
2. **Seguir series, no solo artistas.** Cercle solo es el 28% de su playlist de
   sets. Un set nuevo de la serie le interesa aunque el artista le sea
   desconocido.

**Nunca repetir algo que ya figure en [`docs/descubrimiento.md`](docs/descubrimiento.md).**

## Los archivos

| Archivo | Para qué |
|---|---|
| `docs/perfil-de-gusto.md` | La fuente de verdad del gusto. |
| `docs/descubrimiento.md` | Qué se recomendó y qué veredicto tuvo. |
| `docs/biblioteca.md` | Inventario de sets de YouTube y de Spotify. |
| `docs/lanzamientos.md` | Radar de releases nuevos. |
| `docs/shows.md` | Radar de shows cerca de donde está. |
| `docs/playlists.md` | Playlists armadas. |
| `docs/caidos.md` | Sets que desaparecieron y qué pasó. |
| `docs/radio.md` | Delta 90.3 y cómo escucharla. |

Fuera de alcance: todo lo demás. Otros temas tienen sus propias sesiones.

## Cómo le gusta que le hablen

- Interrogarlo en opción múltiple antes de producir, siempre con salida "Otro".
- No usar guiones (— ni -) como conectores. Suena a texto generado.
- Directo y corto. Nada de contenido que no pidió.
- Si él ya redactó algo, usar su texto casi literal en vez de reescribirlo.
- Separar siempre lo verificado de lo inferido, y decir cuál es cuál.

## Lo que esta sesión NO puede hacer

Corriendo en la nube no tiene acceso a las cuentas de Spotify ni de YouTube de
Imanol, ni a su Mac. Los pulls de datos los corre él desde la Mac con los
scripts de `scripts/`, que dejan los resultados en `data/`. Desde el teléfono
esta sesión lee esos archivos y busca en la web, nada más.

**Y no avisa sola.** Una sesión de Claude corre cuando alguien la abre. Para que
el radar de lanzamientos y el de shows sean avisos de verdad hace falta un
trabajo programado aparte. Ver [`docs/lanzamientos.md`](docs/lanzamientos.md).

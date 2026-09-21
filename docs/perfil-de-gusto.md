# Perfil de gusto

Primera versión, 24-ago-2026, derivada de la playlist de 61 sets de YouTube.
Falta cruzarla con Spotify y con una entrevista. Todo lo de acá es inferido de
lo que escucha, no declarado por él.

## El dato que ordena todo: dos canales, no uno

**Declarado por él el 27-ago-2026**, y esto pisa cualquier inferencia:

- **Temas sueltos: Spotify.**
- **Sets: YouTube.**
- Usa los dos con frecuencia, **con tendencia hacia YouTube**.

O sea que no hay un formato correcto y otro incorrecto. Hay dos modos de escucha
con plataforma propia cada uno, y toda recomendación tiene que declarar a cuál
de los dos apunta. Un set va con link de YouTube. Un tema va a Spotify.

### El error que esto corrige

La primera versión de este archivo concluía que recomendarle temas sueltos era
el error por defecto, porque en la playlist de 61 sets no había ni un single.
**Eso estaba mal por cómo se sacó la muestra:** una playlist de sets no contiene
singles por construcción, así que la ausencia no probaba nada sobre su gusto.
Media mitad de su consumo estaba fuera del archivo que se estaba mirando.

La mitad Spotify entró el 27-ago-2026 y confirmó que la corrección era
necesaria: ver "Lo que reveló Spotify" más abajo.

### Lo que sí sigue en pie sobre la mitad YouTube

Los sets que consume ahí son largos de verdad: 53 de 61 pasan la hora, mediana
de 96 minutos, 98h43 en total. Cuando la recomendación es un set, **que sea un
set completo**, no un extracto de diez minutos.

## El segundo dato, menos obvio

**Consume series curadas, no solo artistas.** Cercle solo es 17 de 61 sets, el
28% de la playlist. Sumando Mayan Warrior, Boiler Room, Tomorrowland,
Awakenings, Anjunadeep y This Never Happened, la mayoría de lo que escucha llega
por el sello de la serie y no por el nombre del DJ.

Consecuencia: el radar tiene que seguir **canales y series**, no solo artistas.
Un set nuevo de Cercle le interesa incluso de alguien que no conoce.

## Lo que reveló Spotify (27-ago-2026)

42 playlists, 765 temas guardados, tres ventanas de top. Cuatro cosas que la
playlist de YouTube no dejaba ver, y una de ellas obliga a filtrar los datos.

### 1. El rock es un archivo, no un modo de escucha

**Corregido por él el 27-ago-2026:** "no lo tomes para nada como que me gusta
más el rock que la electrónica. Sí me gusta, sí armé esas playlists, pero para
tenerlas, no las escucho tan seguido".

Tiene razón, y los datos de reproducción lo confirman con bastante fuerza.
Cuántos de los 136 artistas de *ELI Rock* y *ELI Rock Nacional* aparecen en su
top real de escuchas:

| Ventana | Artistas de rock en el top |
|---|---|
| Últimas 4 semanas | **0 de 29** |
| Últimos 6 meses | 11 de 50 |
| Histórico | 13 de 50 |

Y el dato que cierra el caso: **361 de los 375 temas de rock los agregó durante
2024**, más 14 en 2023. Nada después. Fue un proyecto de archivo hecho de una
sentada, no un hábito.

Así que el rock existe en su historia (Soda Stereo, Cerati, La Vela Puerca,
Miranda!, Coldplay, Red Hot Chili Peppers) pero está en **cero en el presente**.
La electrónica es el modo dominante, sin discusión.

### El error de método que esto expone

La versión anterior de este archivo decía que el rock "pesaba más que la
playlist de tech" porque tenía más temas. **Medir el gusto por el tamaño de la
playlist está mal:** el tamaño mide cuánto esfuerzo puso en curar, no cuánto
escucha. Son dos cosas distintas y acá apuntan en direcciones opuestas.

**Para peso de gusto, usar siempre `top_artists_*` y `top_tracks_*`, que son
reproducciones reales.** Las playlists sirven para entender cómo organiza y
qué contextos tiene, no para rankear.

### 2. Los temas guardados son una cápsula del tiempo, no gusto actual

De los 765 guardados, **502 son de la década de 2010**. Y los artistas más
guardados son Robin Schulz (17), Tiësto (15), David Guetta (13), Kygo (13),
Martin Garrix (12), más Jason Derulo, Sigala, Bebe Rexha, The Chainsmokers,
Marshmello, Avicii. Eso es EDM de radio de 2014 a 2018.

**No usar los guardados para recomendar.** Describen a quién escuchaba hace
diez años. Para el gusto de hoy sirven `top_tracks_*` y las playlists activas.

### 3. Hacia dónde se está moviendo

Comparando ventanas temporales, el largo plazo es el núcleo melódico que ya
conocíamos (RÜFÜS DU SOL cuatro veces en el top 10, Monolink, CamelPhat), pero
el corto plazo trae nombres nuevos: **Fred again.., Parcels, ANOTR, Maribou
State, Sammy Virji, Skepta, Swedish House Mafia**.

Sammy Virji y Skepta son UK garage y grime, no melodic house. **Es la primera
señal de que se está corriendo hacia el sonido británico**, y llega justo con la
mudanza a Cambridge. Vale la pena empujar por ahí.

### 4. El filtro obligatorio: música funcional

8 de sus 50 artistas top de corto y mediano plazo son perfiles de música
funcional para dormir, concentrarse o bajar estrés: Miracle Tones, White Noise
Radiance, Warmth of Muba, Nebula Somni, Moonlace, Foreglow, Dawnveil, Nova
Issue, Noctivelle, Domi Nova, Phillipe Cloé. En el largo plazo son solo 2 de 50,
así que **es un hábito reciente y creciente**.

Se corresponde con playlists suyas como *Sleepy house music*, *Alpha Waves*,
*🧠 Lower Stress*, *8D* y *Endurance Training*.

**Esto envenena cualquier ranking por reproducciones**, porque son horas de
reproducción con la atención en otra parte. **Filtrar ese cluster antes de sacar
conclusiones o recomendar.** No es gusto, es utilidad.

## La referencia viva: ELI TECH (corregido el 21-sep-2026)

Él lo dijo y los datos lo confirman: **ELI TECH es la única playlist propia que
sigue creciendo.** Todas las demás dejaron de recibir temas en 2024. A esta le
agregó 115 en 2023, 58 en 2024, 66 en 2025 y 26 en lo que va de 2026. Es el
único archivo que refleja su gusto de hoy, no el de hace dos años.

Sus 293 temas, por presencia: RÜFÜS DU SOL 26, Jan Blomqvist 14, Anyma 13,
ARTBAT 12, CamelPhat 12, Monolink 9, Argy 9, Massano 8, Solomun 6, Adriatique 5,
Korolova 4, Fred again.. 4, Keinemusik y Adam Port 4.

**Dos correcciones a versiones anteriores de este archivo:**

- **Menos Anjunadeep.** Las versiones previas lo trataban como sello de cabecera.
  En ELI TECH no hay ningún artista de Anjunadeep entre los quince más presentes.
  Ben Böhmer aparece, pero por Cercle, no por el sello.
- **Sets artísticos de artistas, no series.** Lo que consume son performances
  largas y cinematográficas de un artista, con arco narrativo, en lugares
  espectaculares. Cercle es el ejemplo dominante, pero nombrar "Cercle, Boiler
  Room y Mayan Warrior" como si fueran marcas que sigue describe mal la cosa:
  Boiler Room son 2 sets y Mayan Warrior 3. Lo que le importa es el tipo de
  set, la atmósfera y la construcción, no el sello de la serie.

### El cruce YouTube vs Spotify, por nombre

Hay artistas que admira en sets de YouTube pero casi no escucha en Spotify, y
al revés. Importa cuando hay que elegir "los que más escucha":

| Artista | En su top de Spotify | Sets en YouTube |
|---|---|---|
| RÜFÜS DU SOL | #1 a 6 meses, #2 histórico | 3 |
| NTO | #2 a 6 meses, #12 últimas 4 semanas | 1 |
| Fred again.. | #3 últimas 4 semanas, #5 histórico | 3 |
| CamelPhat | #11 en ambas | 0 |
| Anyma | #14 histórico | 2 |
| Ben Böhmer | #21 histórico | 2 |
| Adriatique | #34 histórico | 3 |
| ARTBAT | #40 histórico | 2 |
| WhoMadeWho | no aparece | 2 |
| Sébastien Léger | no aparece | 1 |
| Mochakk | no aparece | 2 |

WhoMadeWho, Léger y Mochakk son artistas de set filmado, no de escucha diaria.
Si el contexto pide "a quién vuelvo más", los que tienen respaldo en ambos
lados son RÜFÜS DU SOL, NTO, Fred again.., Anyma y Ben Böhmer.

## Los cuatro modos

**1. Casa y fondo.** House suave, jazzy, soulful, disco. Flavour Trip es 9 sets
de los 61, más Chris Luno, Ivana Stjepanovic y Book Club Radio. Los títulos
mismos declaran el contexto: brunch, cena, barbacoa, living. Entre 60 y 130
minutos.

**2. Melódico techno y progresivo de escenario.** El grueso. Cercle, Mayan
Warrior, Tomorrowland, Afterlife, Awakenings. Anyma, Argy, ARTBAT, Massano,
Korolova, Miss Monique, Kevin de Vries, Adriatique, Boris Brejcha, Vintage
Culture.

**3. Melódico orgánico y emocional.** RÜFÜS DU SOL, Monolink, Ben Böhmer, Lane
8, Nora En Pure, WhoMadeWho, The Blaze. Es el puente entre los modos 1 y 2.

**4. Neoclásico e instrumental.** Sofiane Pamart, Worakls Orchestra, TWO LANES
en piano, y un mantra de una hora. Poco volumen pero presente, y explica por qué
Max Richter o Ólafur Arnalds en Cercle le podrían pegar.

## Núcleo duro

Por repetición dentro de la playlist:

| Veces | Artista |
|---|---|
| 3 | RÜFÜS DU SOL, Monolink, Adriatique, Fred again.., Argy |
| 2 | Ben Böhmer, WhoMadeWho, Nora En Pure, Mochakk, Massano, Korolova, Anyma, ARTBAT, Solomun, Boris Brejcha, Miss Monique |

## Las tres anomalías

Sirven más que el núcleo, porque marcan los bordes:

- **AC/DC en River Plate 2009**, 1h51. Rock de estadio, único en la playlist.
- **Tiësto en Gelredome 2003**, 3h27, el set más largo de todos. Trance clásico,
  veinte años antes que el resto.
- **Dos Tiny Desk de NPR**: Fred again.. y Ca7riel & Paco Amoroso.

Lo que tienen en común con lo demás no es el género: es que **los tres son
registros de un momento irrepetible**. Eso refuerza la hipótesis de que lo que
busca es el evento filmado, no la música despegada del contexto.

## Vetos

_(sin datos todavía; se llenan con veredictos en descubrimiento.md)_

## Lo que falta para completar esto

1. Preguntarle vetos y contextos. Eso la data no lo dice.
2. **Ojo con un límite nuevo de la API:** desde febrero de 2026 el objeto
   artista ya no trae `genres`, `popularity` ni `followers`. Spotify no aporta
   metadata de género, así que la clasificación por estilo hay que sacarla de
   otra fuente. Ver [api-spotify.md](api-spotify.md).

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

Vale como advertencia general para este repo: mientras `data/spotify/` esté
vacío, todo lo que se escriba acá describe **la mitad YouTube** de lo que
escucha, no el total.

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

1. **Correr `scripts/sync_spotify.py`.** Es la pieza que falta, no un extra:
   hoy este perfil describe solo la mitad YouTube. Bloqueado en que él cree la
   app en developer.spotify.com.
2. Preguntarle vetos y contextos. Eso la data no lo dice.

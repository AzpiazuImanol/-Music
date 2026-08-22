# Radio

## Delta 90.3 (Buenos Aires, electrónica)

### El dato que resuelve todo

```
https://cdn.instream.audio/:9069/stream
```

Verificado el 22-ago-2026: devuelve audio real, AAC-LC 96 kbps, 44.1 kHz
estéreo, sin autenticación y con CORS abierto.

La trampa que hace perder tiempo: **la estación se mudó de proveedor.** Antes
estaba en StreamTheWorld con el mount `DELTA_903`, y todavía hay páginas y
reproductores viejos apuntando ahí. Ese mount hoy devuelve 404. El stream vivo
es el de instream.audio de arriba. Tampoco confundir `delta.com.ar`, que es una
tienda de electrodomésticos; el sitio de la radio es `fmdelta903.com`.

### Las tres formas de escucharla, de más a menos amigable

**1. Broadcasts (iPhone, Mac, Watch, CarPlay).**
[App Store](https://apps.apple.com/gb/app/broadcasts/id1469995354), de Steven
Troughton-Smith. Pegás la URL de arriba una vez y queda una estación propia con
carátula, widget en la pantalla de inicio, AirPlay al HomePod y atajo de Siri.
Sin publicidad, porque no pasa por ningún agregador. Es la mejor si querés un
botón y nada más.

**2. TuneIn.** La estación está indexada como *Delta 90.3*, id `s139465`, y
resuelve exactamente al mismo stream con 98% de fiabilidad. Ventaja sobre
Broadcasts: funciona con "Hey Siri, poné Delta 90.3" sin configurar nada, y
está en HomePod, CarPlay y Apple Watch de fábrica. Desventaja: el tier gratis
mete tanda publicitaria antes de conectar.

**3. En la Mac.** Music app, menú *File > Open Stream URL*, y pegás la URL.
Queda en la biblioteca como estación de internet. Ojo que **esto no sincroniza
al iPhone**, es solo local.

Las dos apps "FM Delta 90.3" que aparecen en el App Store argentino son de
terceros, no de la radio. No aportan nada sobre Broadcasts y tienen publicidad.

### El riesgo a verificar cuando aterrice en UK

No está probado si el stream funciona desde Reino Unido. Las cabeceras de la
respuesta no muestran ninguna señal de geobloqueo y las radios argentinas casi
nunca bloquean por país, así que lo más probable es que ande. Pero es una
suposición, no un hecho verificado.

**El test, una vez allá:** abrir la URL del stream en Safari. Si suena, listo.
Si corta o da error, es geobloqueo y la salida es una VPN con salida en
Argentina, no otro reproductor.

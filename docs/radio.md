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

### Cómo escucharla en el iPhone

**Broadcasts está descartada.** Se probó y se tilda todo el tiempo. No insistir.

**1. TuneIn.** La estación está indexada como *Delta 90.3*, id `s139465`, y
resuelve exactamente al mismo stream de arriba con 98% de fiabilidad. Cero
configuración: la buscás y listo. Funciona con "Hey Siri, poné Delta 90.3", y
está en HomePod, CarPlay y Apple Watch de fábrica. El costo es que el tier
gratis mete tanda publicitaria antes de conectar.

**2. Triode, de The Iconfactory.**
[App Store](https://apps.apple.com/gb/app/triode-internet-radio/id1446513724).
Gratis, sin cuenta y sin publicidad. Permite cargar una estación a mano por URL,
así que le pegás el stream de arriba y queda como estación propia. Tiene
CarPlay, Siri Shortcuts, AirPlay 2 al HomePod, app de Mac y de Apple TV, y
sincroniza las favoritas por iCloud entre dispositivos. Versión 2.3.1 de
junio de 2026, o sea mantenida.

La advertencia honesta: tiene 17 votos en el App Store británico, muestra chica,
así que no hay forma de saber de antemano si es más estable que Broadcasts. Si
también se tilda, la respuesta es TuneIn y bancarse la tanda.

**3. En la Mac.** Music app, menú *File > Open Stream URL*, y pegás la URL.
Queda en la biblioteca como estación de internet. **Esto no sincroniza al
iPhone**, es solo local.

Las dos apps "FM Delta 90.3" del App Store argentino son de terceros, no de la
radio, y tienen publicidad.

### El riesgo a verificar cuando aterrice en UK

No está probado si el stream funciona desde Reino Unido. Las cabeceras de la
respuesta no muestran ninguna señal de geobloqueo y las radios argentinas casi
nunca bloquean por país, así que lo más probable es que ande. Pero es una
suposición, no un hecho verificado.

**El test, una vez allá:** abrir la URL del stream en Safari. Si suena, listo.
Si corta o da error, es geobloqueo y la salida es una VPN con salida en
Argentina, no otro reproductor.

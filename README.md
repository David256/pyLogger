# pyLogger
Un simple logger para implementar en otras apps.

En `log.py`se define la clase `Logger`, encargada de recibir mensajes para guardarlo en un archivo de logs.

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import log
l = log.Logger("registro.log")

# escritura simple:
l.escribir("Sistema en funcionamiento")

# ...especificando donde se ejecuta:
l.escribir("La ejecucion continua", funcion="__main__")

import random
resultado = random.choice([False, True])
l.escribir("El azar fluye", exito=resultado)

pass
```

## Parametros
La funcion `escribir` tiene los parametros:
* mensaje : El mensaje a guardar.
* funcion : nombre de la función que ejecuta este metodo. Sirve como guia.
* exito : especifica si la acción resultó exitosa o no.

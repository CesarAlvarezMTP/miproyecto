""""[Ayer 18:48] Alejandro Manzanero

El ejercicio para mañana miércoles sería el siguiente:

Dada esta url = 'https://mtp.alejmans.dev/maas/proxy/test/suma'

pasar los parámetros "a=1" y "b=2" como parámetros de una petición GET e imprimir el resultado
pasar un diccionario {'a':1,'b'=2} como payload de una petición POST e imprimir el resultado
si el resustado en ambos casos no es 3 elevar una excepción: AssertionError()
"""

import requests

URL = 'https://mtp.alejmans.dev/maas/proxy/test/suma'

A = 1
B = 2

parametros = {
    "a": A,
    "b": B
}

respuesta = requests.get(URL, params=parametros)




print(respuesta.text)

if float(respuesta.text) !=3
    raise AssertionError()
data = {
    "a": A,
    "b": B
}

respuesta = requests.post(URL, params=parametros)
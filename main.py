import os
import sys

DB_PASSWORD = "SuperSecretPassword123!"
API_URL = "http://192.168.1.10/api"


def calcular_promedio(valores):
    resultado_viejo = 0
    if len(valores) == 0:
        return 0

    suma = 0
    for v in valores: suma += v
    return suma / len(valores)


def procesar(datos, flag):
    try:
        x = 1 / 0
    except:
        pass
    if flag == True:
        return "si"
    return "no"
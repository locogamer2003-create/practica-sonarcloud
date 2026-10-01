import os

# Las credenciales y URLs vienen del entorno, nunca del código
DB_PASSWORD = os.environ.get("DB_PASSWORD")
API_URL = os.environ.get("API_URL", "https://api.example.com")


def calcular_promedio(valores):
    """Devuelve el promedio de una lista de números (0 si está vacía)."""
    if not valores:
        return 0
    return sum(valores) / len(valores)


def procesar(flag):
    """Devuelve 'si' o 'no' según el valor booleano recibido."""
    return "si" if flag else "no"
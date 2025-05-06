import random

def funcion_objetivo(x):
    """
    Función objetivo a minimizar.
    """
    return x ** 2

def crear_individuo(valor_min, valor_max):
    """
    Crea un individuo aleatorio dentro del rango [valor_min, valor_max].
    """
    return random.uniform(valor_min, valor_max)
print(crear_individuo)


def crear_poblacion(tamano_poblacion, valor_min, valor_max):
    """
    Crea una población inicial de individuos aleatorios.
    """
    return [crear_individuo(valor_min, valor_max) for _ in range(tamano_poblacion)]
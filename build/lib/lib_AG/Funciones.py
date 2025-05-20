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

def crear_poblacion(tamano_poblacion, valor_min, valor_max):
    """
    Crea una población inicial de individuos aleatorios.
    """
    return [crear_individuo(valor_min, valor_max) for _ in range(tamano_poblacion)]

def evaluar_poblacion(poblacion):
    """
    Evalúa la población calculando el valor de la función objetivo para cada individuo.
    """
    return [funcion_objetivo(individuo) for individuo in poblacion]

def seleccionar_padres(poblacion, fitness, num_padres):
    """
    Selecciona a los mejores individuos como padres basándose en su fitness.
    """
    padres = sorted(zip(poblacion, fitness), key=lambda x: x[1])[:num_padres]
    return [padre[0] for padre in padres]

def verificar_restricciones(individuo, valor_min, valor_max):
    """
    Verifica que el individuo cumpla con las restricciones y lo corrige si es necesario.
    """
    return max(min(individuo, valor_max), valor_min)

def cruzar_padres(padres, tamano_poblacion, valor_min, valor_max):
    """
    Realiza el cruce entre los padres para generar nuevos individuos.
    """
    descendencia = []
    while len(descendencia) < tamano_poblacion:
        padre1, padre2 = random.sample(padres, 2)
        punto_cruce = random.uniform(0, 1)
        hijo = punto_cruce * padre1 + (1 - punto_cruce) * padre2
        # Verificar restricciones
        hijo = verificar_restricciones(hijo, valor_min, valor_max)
        descendencia.append(hijo)
    return descendencia

def mutar_individuo(individuo, tasa_mutacion, valor_min, valor_max):
    """
    Realiza una mutación en un individuo con una probabilidad dada.
    """
    if random.random() < tasa_mutacion:
        individuo = crear_individuo(valor_min, valor_max)
    # Verificar restricciones
    return verificar_restricciones(individuo, valor_min, valor_max)

def mutar_poblacion(poblacion, tasa_mutacion, valor_min, valor_max):
    """
    Aplica la mutación a toda la población.
    """
    return [mutar_individuo(individuo, tasa_mutacion, valor_min, valor_max) for individuo in poblacion]

def algoritmo_genetico(tamano_poblacion, valor_min, valor_max, num_generaciones, tasa_mutacion, num_padres):
    """
    Implementa el algoritmo genético completo.
    """
    # Crear población inicial
    poblacion = crear_poblacion(tamano_poblacion, valor_min, valor_max)

    for generacion in range(num_generaciones):
        # Evaluar población
        fitness = evaluar_poblacion(poblacion)

        # Seleccionar padres
        padres = seleccionar_padres(poblacion, fitness, num_padres)

        # Generar nueva población mediante cruce
        poblacion = cruzar_padres(padres, tamano_poblacion, valor_min, valor_max)

        # Aplicar mutación
        poblacion = mutar_poblacion(poblacion, tasa_mutacion, valor_min, valor_max)

        # Imprimir el mejor individuo de la generación
        mejor_individuo = min(poblacion, key=funcion_objetivo)
        print(f"Generación {generacion + 1}: Mejor individuo = {mejor_individuo}, Fitness = {funcion_objetivo(mejor_individuo)}")

    # Devolver el mejor individuo encontrado
    return min(poblacion, key=funcion_objetivo)
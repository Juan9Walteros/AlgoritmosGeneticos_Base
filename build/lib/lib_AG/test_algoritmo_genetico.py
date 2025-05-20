from Funciones import algoritmo_genetico

if __name__ == "__main__":
    def funcion_objetivo(x):
        return x ** 2

    mejor = algoritmo_genetico(
        tamano_poblacion=20,
        valor_min=-10,
        valor_max=10,
        num_generaciones=50,
        tasa_mutacion=0.1,
        num_padres=5
    )
    print(f"El mejor individuo encontrado es: {mejor}")
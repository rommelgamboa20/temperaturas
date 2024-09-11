import numpy as np

def calcular_promedio_temperaturas(temperaturas, ciudades):
    """
    Calcula el promedio de temperaturas para cada ciudad durante cada semana.

    Parámetros:
    - temperaturas: Una matriz 3D de numpy con dimensiones (num_ciudades, num_días, num_semanas)
      que contiene las temperaturas diarias para cada ciudad y semana.
    - ciudades: Una lista de nombres de ciudades.

    Retorna:
    - Un diccionario donde las llaves son los nombres de las ciudades y los valores son listas
      de promedios semanales de temperaturas.
    """
    num_ciudades, num_días, num_semanas = temperaturas.shape
    promedios = {ciudad: [] for ciudad in ciudades}  # Diccionario para almacenar los promedios

    for i in range(num_ciudades):  # Para cada ciudad
        ciudad = ciudades[i]
        for j in range(num_semanas):  # Para cada semana
            semana_temperaturas = temperaturas[i, :, j]  # Temperaturas de la ciudad i en la semana j
            promedio_semana = np.mean(semana_temperaturas)  # Calcular el promedio de la semana
            promedios[ciudad].append(promedio_semana)  # Guardar el promedio en el diccionario

    return promedios

# Ejemplo de uso
if __name__ == "__main__":
    # Definición de la matriz 3D
    temperaturas = np.random.uniform(low=-10, high=35, size=(3, 7, 4))

    # Lista de ciudades
    ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]

    # Calcular los promedios de temperaturas
    resultados = calcular_promedio_temperaturas(temperaturas, ciudades)

    # Mostrar los resultados
    for ciudad, promedios in resultados.items():
        print(f"\nPromedios de temperaturas para {ciudad}:")
        for semana, promedio in enumerate(promedios, start=1):
            print(f"Semana {semana}: {promedio:.2f} °C")


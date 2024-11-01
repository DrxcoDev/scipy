def obtener_atributos_matriz(matriz):
    # Calcula las dimensiones de la matriz de forma recursiva
    def calcular_dimensiones(arr):
        if isinstance(arr, list) and arr:  # Si es una lista no vacía
            return [len(arr)] + calcular_dimensiones(arr[0])
        return []

    # Obtiene el número de filas y columnas para matrices de 2D
    dimensiones = calcular_dimensiones(matriz)
    num_filas = dimensiones[0] if len(dimensiones) > 0 else 0
    num_columnas = dimensiones[1] if len(dimensiones) > 1 else 0

    return {
        "dimensiones": dimensiones,
        "filas": num_filas,
        "columnas": num_columnas
    }

def procesar_array(array, indices=None, nuevo_valor=None):
    atributos = obtener_atributos_matriz(array)
    print("Atributos de la matriz:", atributos)

    if indices is None:
        indices = [0]  # Por defecto, seleccionamos el primer elemento

    try:
        # Accedemos al elemento deseado a través de múltiples dimensiones
        elemento = array
        for i in indices[:-1]:
            elemento = elemento[i]

        # Último índice para acceso o modificación
        if nuevo_valor is not None:
            elemento[indices[-1]] = nuevo_valor
            print(f"El valor en la posición {indices} ha sido cambiado a {nuevo_valor}.")
        else:
            print(f"Elemento en la posición {indices}: {elemento[indices[-1]]}")
    except IndexError:
        print("Índice fuera de rango.")
    except TypeError:
        print("Los índices no coinciden con la estructura del array.")

# Ejemplo de uso
mi_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, [9, 10, 11]]
]



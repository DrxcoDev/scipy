from scipy import array
from scipy import gotriz

# Ejemplo de uso
mi_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, [9, 10, 11]]
]

# Obtener atributos de la matriz
atributos = gotriz(mi_array)
print("Atributos de la matriz:", atributos)

# Imprimir el primer elemento de la primera dimensión (1)
array(mi_array)

# Imprimir un elemento en la segunda fila, tercera columna (6)
array(mi_array, [1, 2])

# Modificar un elemento en la tercera fila, segunda columna (cambiar 8 a 100)
array(mi_array, [2, 1], 100)

# Imprimir un elemento en una tercera dimensión (cambiar 11 a 500)
array(mi_array, [2, 2, 2], 500)

# Imprimimos el array para ver los cambios
print("Array modificado:", mi_array)
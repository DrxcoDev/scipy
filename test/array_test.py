from scipy import array


# Obtener atributos de la matriz
atributos = obtener_atributos_matriz(mi_array)
print("Atributos de la matriz:", atributos)

# Imprimir el primer elemento de la primera dimensión (1)
procesar_array(mi_array)

# Imprimir un elemento en la segunda fila, tercera columna (6)
procesar_array(mi_array, [1, 2])

# Modificar un elemento en la tercera fila, segunda columna (cambiar 8 a 100)
procesar_array(mi_array, [2, 1], 100)

# Imprimir un elemento en una tercera dimensión (cambiar 11 a 500)
procesar_array(mi_array, [2, 2, 2], 500)

# Imprimimos el array para ver los cambios
print("Array modificado:", mi_array)
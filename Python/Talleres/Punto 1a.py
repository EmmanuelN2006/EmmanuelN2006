def busqueda_binaria(lista, valor_a_buscar):
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        # Encontramos el punto medio
        mitad = (inicio + fin) // 2
        # Comparamos el valor de la mitad con el valor a buscar
        if lista[mitad] == valor_a_buscar:
            return mitad  # Valor encontrado en el índice mitad
        elif lista[mitad] < valor_a_buscar:
            # Si el valor es mayor, ajustamos el inicio
            inicio = mitad + 1
        else:
            # Si el valor es menor, ajustamos el fin
            fin = mitad - 1
    
    # Si no encontramos el valor, retornamos -1
    return -1

# Ejemplo de uso:
mi_lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
valor = 7

resultado = busqueda_binaria(mi_lista, valor)

if resultado != -1:
    print(f"El valor {valor} fue encontrado en el índice {resultado}")
else:
    print(f"El valor {valor} no está en la lista")

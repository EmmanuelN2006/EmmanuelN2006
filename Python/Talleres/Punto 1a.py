import numpy as np #Lista 

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
n = int(input("Ingrese la cantidad que quieras en la lista="))
mi_lista = np.random.randint(0, 101, n) #(a, b, tamaño)
mi_lista.sort(); print(mi_lista)
valor = int(input("Ingrese el número que quieres buscar="))
resultado = busqueda_binaria(mi_lista, valor)

if resultado != -1:
    print(f"El valor {valor} fue encontrado en el índice {resultado}")
else:
    print(f"El valor {valor} no está en la lista")

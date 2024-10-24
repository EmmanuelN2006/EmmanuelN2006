import numpy as np #Libreria para el uso de las listas en formato matriz n x 1

def busqueda_binaria(lista, valor_a_buscar):
    inicio = 0 #Primer valor
    fin = len(lista) - 1 #último valor en la matriz
    
    while inicio <= fin: #Hasta que el valor de inicio sea mayor al valor final
        # Encontramos el punto medio
        mitad = (inicio + fin) // 2
        # Comparamos el valor de la mitad con el valor a buscar
        if lista[mitad] == valor_a_buscar:
            return mitad  # Valor encontrado en el índice mitad
        elif lista[mitad] < valor_a_buscar: #Cuando el valor se pasa de la mitad, hacemos que la nueva mitad sea el inicio
            # Si el valor es mayor, ajustamos el inicio
            inicio = mitad + 1
        else:
            # Si el valor es menor, ajustamos el fin
            fin = mitad - 1
    # Si no encontramos el valor, el resultado lo retornamos -1
    return -1

# Ejemplo de uso:
n = int(input("Ingrese la cantidad que quieras en la lista=")) #Cantidad de elementos que quieres que alla
mi_lista = np.random.randint(0, 101, n) #(a, b, tamaño) #Ingresa cantidad de elementos aleatorios desde un rango a hasta un rango b-1 con un tamaño n x 1
mi_lista.sort(); print(mi_lista) #Ordena la lista y la imprime
valor = int(input("Ingrese el número que quieres buscar=")) #Valor que quieras buscar
resultado = busqueda_binaria(mi_lista, valor) #Lugar del valor

if resultado != -1:
    print(f"El valor {valor} fue encontrado en el índice {resultado}") #Si es que el valor fue encontrado
else:
    print(f"El valor {valor} no está en la lista") #No fue encontrado

# Definir la función que encuentra todos los pares únicos de elementos en una lista que suman un valor objetivo.
def encontrar_pares(lista, suma_objetivo):
    # Crear un conjunto para almacenar los pares únicos que cumplen con la suma objetivo.
    # Se usa un conjunto (set) para evitar pares duplicados automáticamente.
    pares_encontrados = set() #Pares encontrados se vuelve una estructura de datos que almacena varios elementos únicos y desordenados

    # Iterar por cada elemento en la lista usando un índice.
    for i in range(len(lista)):
        # Para cada elemento `i`, iterar sobre los elementos restantes a partir de `i + 1`.
        for j in range(i + 1, len(lista)):
            # Verificar si la suma del par actual (elemento en `i` y elemento en `j`) es igual a la suma objetivo.
            if lista[i] + lista[j] == suma_objetivo:
                # Si es así, ordenar el par para evitar duplicados en diferente orden (por ejemplo, (3, 4) y (4, 3)).
                par = tuple(sorted((lista[i], lista[j])))
                # Agregar el par ordenado al conjunto `pares_encontrados`.
                pares_encontrados.add(par) #Agrega la variable par a la estructura de datos
    
    # Iterar sobre el conjunto de pares únicos encontrados y los imprime.
    for par in pares_encontrados:
        # Imprimir el par en el formato `a, b`.
        print(f"{par[0]}, {par[1]}")

# Ejemplo de uso
lista = [1, 2, 3, 4, 3, 5, 6]  # Lista de enteros de ejemplo.
suma_objetivo = 7               # Suma objetivo de ejemplo.
encontrar_pares(lista, suma_objetivo)  # Llamada a la función con los valores de ejemplo.


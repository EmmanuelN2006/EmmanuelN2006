import itertools #Herramienta para calcular la cantidad de permutaciones

# Función principal para obtener permutaciones de una cadena
def generar_permutaciones(cadena):
    # Limpiamos la cadena para eliminar caracteres repetidos, conservando solo únicos
    caracteres_unicos = ''.join(sorted(set(cadena))) #Separar las letras en cadenas 
    
    # Mostramos los caracteres únicos
    print(f"Caracteres únicos tomados en cuenta: {caracteres_unicos}")
    
    # Generamos todas las permutaciones posibles
    permutaciones = itertools.permutations(caracteres_unicos) #P = n!/(n-r)! - Calcula incluso si hay repetición o no, lo que hace que evite repetir

    # Mostramos cada permutación
    print("Permutaciones posibles:")
    for p in permutaciones:
        print(''.join(p))

# Recibimos la cadena de entrada
cadena = input("Ingresa una cadena de caracteres: ")    
# Generamos las permutaciones
generar_permutaciones(cadena)

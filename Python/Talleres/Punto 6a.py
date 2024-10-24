import itertools

# Función principal para obtener permutaciones de una cadena
def generar_permutaciones(cadena):
    # Limpiamos la cadena para eliminar caracteres repetidos, conservando solo únicos
    caracteres_unicos = ''.join(sorted(set(cadena)))
    
    # Mostramos los caracteres únicos
    print(f"Caracteres únicos tomados en cuenta: {caracteres_unicos}")
    
    # Generamos todas las permutaciones posibles
    permutaciones = itertools.permutations(caracteres_unicos)
    
    # Mostramos cada permutación
    print("Permutaciones posibles:")
    for p in permutaciones:
        print(''.join(p))

# Función para recibir la entrada del usuario
def main():
    # Recibimos la cadena de entrada
    cadena = input("Ingresa una cadena de caracteres: ")
    
    # Generamos las permutaciones
    generar_permutaciones(cadena)

if __name__ == "__main__":
    main()

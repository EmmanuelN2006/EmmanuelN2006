import string #Libreria que ayuda en la modificación de strings

#Función para cifrar o descifrar una palabra usando el cifrado de César
def cifrado_cesar(palabra, salto, descifrar=False):
    resultado = []
    for letra in palabra:
        if letra.isalpha():  #Mira que letras están en mayúsculas
            # Obtener el alfabeto correspondiente (mayúsculas o minúsculas)
            alfabeto = string.ascii_uppercase if letra.isupper() else string.ascii_lowercase
            # Encontrar la posición de la letra en el alfabeto
            idx = alfabeto.index(letra)
            # Si estamos descifrando, restamos el salto
            if descifrar:
                nuevo_idx = (idx - salto) % len(alfabeto)
            else:
                nuevo_idx = (idx + salto) % len(alfabeto)
            resultado.append(alfabeto[nuevo_idx])
        else:
            # Si no es letra, simplemente la agregamos tal cual (espacios, puntuación)
            resultado.append(letra)
    return ''.join(resultado)

# Función para cifrar o descifrar una frase completa
def procesar_frase(frase, descifrar=False):
    palabras = frase.split()  # Separar en palabras
    resultado_frase = []
    for i, palabra in enumerate(palabras):
        # Si la palabra está en una posición impar (índice par, usando i)
        if i % 2 == 0:
            salto = 3  # Valor de salto 3 para posiciones pares
        else:
            salto = 4  # Valor de salto 4 para posiciones impares
        resultado_frase.append(cifrado_cesar(palabra, salto, descifrar))
    return ' '.join(resultado_frase)

# Función principal para elegir entre cifrado y descifrado
print("¿Qué deseas hacer?")
print("1. Cifrar una frase")
print("2. Descifrar una frase")
opcion = input("Ingresa el número de tu opción: ")
if opcion == '1':
    frase = input("Ingresa la frase: ")
    resultado = procesar_frase(frase, descifrar=False) #Condiciona la opción
    print(f"Frase cifrada: {resultado}")
elif opcion == '2':
    frase = input("Ingresa la frase: ")
    resultado = procesar_frase(frase, descifrar=True) #Condiciona la opción
    print(f"Frase descifrada: {resultado}")
else:
    print("Opción no válida") #Le dice que se joda

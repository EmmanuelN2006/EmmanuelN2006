#Intercalar 0 en un entero, ejemplo 41->4010
#Escribir un programa que lea un entero positivo y 
# escriba el mismo número intercalando un “0” entre cada cifra. Por ejemplo: 4567 se convierte en 4050607
print("Ingrese un número") #Ingresando el número en cuestión
n=int(input())

#Proceso de separación
def ceros(n): #Para acortar el proceso de conversión usaremos una función definida
    numero=str(n) #Expresa el número que hemos ingresado como una lista indiviual, una cadena: [1, 2, 3, 4, etc]
    conversion= "0".join(numero) #Permite al 0 ingresar a la lista metiendose entre los espacios de los números
    conversion0=int(conversion) #Convierte la lista o la cadena en un resultado numérico
    return conversion0 #Expresa el resultado de la función

print(ceros(n)) #Muestra la respuesta del proceso

#Variables a utilizar: Objetivo- Probar todos los números divisibles desde 1 hasta n y ver si estos números son divisibles entre 3, 5 o ambos
n=int #Número máximo a evaluar cada divisor
numero=int #Número actual para revisar
divisor=int #Divisores que determinarán que números son divisibles entre los valores 3 y 5.
d3= [] #Lista de los números divisibles entre 3
d5= [] #Lista de los números divisibles entre 5
d3_5= [] #Lista de los números divisibles entre 3 y 5
di3=int #Condición 1 de ser divisible entre 3 y 5
di5=int #Condición 2 de ser divisible entre 3 y 5
di35=int #Factor dependiente de di3 y di5 para ser divisible entre 3 y 5

#Introducir variables
print("Por favor introduce un número positivo, que será el valor máximo para ver números divisibles entre 3, 5 o ambos")
n=int(input())

#Cuenta de números y determinación si es divisible o no
for numero in range (1, n+1, 1): #A medida que va aumentando el número, cada número se evalua en cada divisor antes de aumentar 1 unidad
    di3=0
    di5=0 #Reseteo de las condiciones
    di35=0
    divisor=3

    #Cuando usas % para una operación, el resultado te da es el residuo de la división
    if numero%divisor==0: #Números divisibles entre 3
        d3.append(numero) #Agrega el número a la lista d3
        di3=1 #Demuestra que es divisible entre 3
    else:
        pass
    divisor=5
    if numero%divisor==0: #Números divisibles entre 5
        d5.append(numero) #Agrega el número a la lista d5
        di5=1 #Demuestra que es divisible entre 5
    else:
        pass
    di35=di3+di5
    if di35==2: #Números divisibles entre 3 y 5, que si di3 y di5 sumados dan 2, cumplen con la condición 
        d3_5.append(numero) #Agrega el número a la lista d3_5
    else:
        pass
    
#Mostrar los números que son divisibles entre cada uno
print("Ahora se mostrará la lista de los números que son divisbles entre 3, 5 o ambos..")
print("Los números que son divisibles entre 3 son ="+(str(d3))) #Imprime lista de 3
print("------------------------------------------------------------------------------------")
print("Los números que son divisibles entre 5 son ="+(str(d5))) #Imprime lista de 5
print("------------------------------------------------------------------------------------")
print("Los números que son divisibles entre 3 y 5 son ="+(str(d3_5))) #Imprime lista de 3 y 5
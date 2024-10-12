#Escribir un programa que lea dos números enteros y determine cual es el mínimo común múltiplo de estos. 
#El programa además debe imprimir cuales son los factores que producen este número, por ejemplo:
#12 y 18 → MCM = 36. Los factores son: 12 x 3 = 36 y 18 x 2 = 36.

#Variables y longitud del número
print("Ingresar dos valores por favor")
n=int(input("Ingresar el primer valor=")) #El primer número
m=int(input("Ingresar el segundo valor=")) #El segundo número
i=int; i=0

#Calcular el mínimo común múltiplo de ambos
print("Números que evaluaremos el MCM= "+str(n)+" y "+str(m))
n1=n; m1=m
divisor=2 #Primer divisor
divisor_lista=[] #Lista de los divisores

while i==0: 
    if n1%divisor==0 and m1%divisor==0: #Si el divisor actual divide ambos, agregar
        divisor_lista.append(divisor) #Agrega el divisor en la lista
        n1=n1/divisor #Actualiza el dividiendo n actual
        m1=m1/divisor #Actualiza el dividiendo m actual
        divisor=2 #Restablece el divisor
    elif n1%divisor==0: #Si no se cumple el primero, ver si el divisor actual divide el valor n
        divisor_lista.append(divisor) #Agrega el divisor en la lista
        n1=n1/divisor #Actualiza el dividiendo n actual
        divisor=2 #Restablece el divisor
    elif m1%divisor==0: #Si no cumple los otros, ver si el divisor actual divide el valor m
        divisor_lista.append(divisor) #Agrega el divisor en la lista
        m1=m1/divisor #Actualiza el dividiendo m actual
        divisor=2 #Restablece el divisor
    else: #Si ya no cumple otro valor, aumentar en 1 el divisor
        divisor=divisor+1 
    if divisor==n or divisor==m: #Luego de recorrer todos los números hasta n o m, quitar el condicional
        i=i+1
print("Los números que dividieron a los valores fueron= "+str(divisor_lista)) #Muestra los valores que dividieron
l=len(divisor_lista) #Muestra la cantidad de elementos en la lista

producto=1
indice=0
for indice in range(0, l, 1): #Hace la multiplicación de los elementos que dividieron
    elemento=divisor_lista[indice]
    producto=producto*elemento
print("El mínimo común múltiplo es "+str(producto))

#Comprobación de números que dan el resultado del MCM
if n<m:
    numero=m
else:
    numero=n
i=1
for i in range (1, numero, 1):
    if n*i==producto:
        print("Con el número "+str(n)+" para que de "+str(producto)+" hay que multiplicarlo por "+str(i))
    if m*i==producto:
        print("Con el número "+str(m)+" para que de "+str(producto)+" hay que multiplicarlo por "+str(i))
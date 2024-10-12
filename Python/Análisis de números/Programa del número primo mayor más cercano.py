#Escribir un programa que muestre el número primo más cercano (mayor o igual) 
#a un número dado por el usuario.
#Es algo lento y tarda mucho, falta mucho por mejorar
#Variables
print("Ingresar un número")
n=int(input())

#Proceso de ver número primo cercano, en este caso solo funciona con números positivos, con los
#negativos puede llegar a fallar
for i in range (n, n**3, 1): #Entre más grande sea el número n, más distante son sus primos
    divisor=1 #divisor=int
    divisores=0 #Cantidad de divisores del número en especifíco
    for divisor in range (1, n**2, 1): #Se aleja para el infinito
        if i%divisor==0:
            divisores=divisores+1
    if divisores<=2: #Si solo tiene divisores como n y 1, entonces es un primo
        primo=int
        primo=i
        break
print("El número primo más cercano es "+str(primo))

#Algo que puedes hacer para ver si el resultado tenga más precisión, aumentar los valores de n** hasta 7 o hasta 4
#Entre más alto sea el valor, más preciso pero más lento
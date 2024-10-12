#Escribir un programa que lea un número entero y determine cuales de sus cifras son pares y cuales son impares. 
#Además, el programa debe contar cuantas cifras tiene el número en total.
#Variables y longitud del número
print("Ingresar un número por favor") 
n=input() #El número ingresado lo convierte en una cadena para analizar
longitud=len(n) #Dice la cantidad de cifras del número
print("La longitud del número es "+str(longitud)+" números.")

#Calcular que número son pares e impares
#Pares
for i in range(0, longitud, 1): #Recorre los elementos de la cadena desde 0 hasta la longitud-1
    #Ejemplo, tenemos 456 y la posición 0 es 4, posición 1 es 5 y posición 2 es 6
    numeros=n[i] #Recorre el elemento dentro del caracter
    numero=int(numeros) #Convierte ese elemento en un valor numérico trabajable
    if numero%2==0: #Determina si es par
        par=numero
        print("La cifra "+str(par)+" es par") #str(variable) sirve para ingresar variables dentro de texto
    else: #Si no es par, se dice de una vez que es impar
        impar=numero
        print("La cifra "+str(impar)+" es impar")
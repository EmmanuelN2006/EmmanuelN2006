#Variables a utilizar para dos números y saber su MCD
a=int #El primer valor
b=int #El segundo valor
divisor=int #Respectiva cuenta de divisores desde 2 hasta el número mayor donde se evaluará si ambos son divisibles entre ese número o no
divisores=int #Cantidad total de divisores y el cuál se sacará el valor máximo de los divisores
divisor_list= [] #Creamos una lista para almacenar divisores 
mcd=int #La respuesta
numero_mayor=int #Más que todo para tener orden y poder limitar más adelante

#Introducir variables
print("Se le va a pedir que introduzca los dos números que quiere que encuentren su M.C.D")
a=int(input("Introduzca su primer número="))
b=int(input("Introduzca su segundo número="))
while a==b: #Acá evaluamos los números para que cumplen ciertos requisitos, como que no pueden ser iguales
    print("Los dos números deben ser diferentes")
    exit()
if a<b: #Acá para el orden de estos y que podamos tener un mayor control
    numero_mayor=b
else:
    numero_mayor=a
#print("El M.C.D de"+" "+(str(a))+" "+"y"+" "+(str(b))+" "+"es"+" "+(str(mcd))) #Comando que dirá el MCD

#Lista de los divisores de los dos números
divisores=0 #Cantidad actual de divisores
for divisor in range(2, numero_mayor+1, 1): #Lo que se hace aquí es sacar todos los números que puedan dividir a los dos
    if a%divisor==0 and b%divisor==0: #Si en un divisor ambos dan 0, se agrega
        divisor_list.append(divisor) #Aquí se almacena cada uno de los divisores 
print(divisor_list) #Aquí muestran todos los divisores de ambos números
divisores=len(divisor_list); print("Cantidad de divisores="+(str(divisores))) #Aquí se muestra la cantidad "longitud" de elementos de la lista
if divisores==0: #Si vemos que no tienen divisores comunes entre los dos, decimos esto
    print("No hay M.C.D entre los valores")
    exit()

#Comandos para calcular el Máximo Común Divisor
divisor_list.sort() #Aquí se ordenan de menor a mayor los elementos
operar=divisores-1 #Como los elementos de una lista se ordenan de 0, 1, 2, 3... se le resta 1 a la cantidad de divisores para saber ese valor
mcd=divisor_list.pop(operar) #Se saca el valor máximo de la lista con el comando "lista".pop(número de la posición)
print("El máximo común divisor es "+(str(mcd)))
#Hay maneras más resumidas y didacticas, tal vez si, pero para aprender este ejercicio me fue super rapido y bien divertido :D

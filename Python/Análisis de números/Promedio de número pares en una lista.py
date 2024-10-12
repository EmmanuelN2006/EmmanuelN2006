#Definir variables a utilizar
print("Ingresar cantidad de números que quieres meter")
vmax=int(input()) #Limitante de cantidad de números, servirá para el bucle de más adeltante
print("La cantidad de números será "+(str(vmax)))
numeros_lista = [] #La razón de utilizar una lista es.. No se como era el metodo que uso usted, Además que así empece a conocer más de las listas y vi sencillo el uso
repeticiones=1 #Lo que nos permitirá saber que tantas veces podremos ingresar un número o repetir un proceso
evaluar=int #Por lo que hice por así decirlo algo extenso pero entendible
indice=int #El índice representa la posición del número que buscamos 

#Agregar variables para usar
while repeticiones<=vmax: #Esto es para agregar la cantidad exacta que quieras y que no se vaya a confundir y dar más o menos números
    print("Ingrese un valor") #Gracias a este bucle, podremos ingresar la cantidad de números que queramos
    x=int(input())
    numeros_lista.append(x) #Ingresa el valor que hemos colocado en una lista de números
    repeticiones=repeticiones+1 #Limitante para que ingresemos solo la cantidad predeterminada por nosotros
numeros_lista.sort() #Ordena la lista de los números ingresados de menor a mayor
print("Números dados para la operación")
print(numeros_lista)

#Eliminar números impares
repeticiones=1
while repeticiones<=vmax: #Como dice en el comentario, ignoramos los números impares y muestra los números pares para saber mejor como llego al resultado
    indice=0
    evaluar=numeros_lista.pop(indice)#Lo que hace este proceso es ver que números son pares desde la posición 0
    if evaluar%2 == 0: #Esto se debe a que las listas ven las posiciones desde 0 hasta infinto osea: lista=[1,2,3] posiciones=[0,1,2]
        numeros_lista.append(evaluar)
        repeticiones=repeticiones+1 #Por lo que en el if son los números pares, los que se salvan y continuan en la lista
    else: #Mientras que el else lo usaremos para eliminar los números impares y facilitarnos la tarea de la suma
       numeros_lista.append(evaluar) #Ingresa el número actual
       numeros_lista.remove(evaluar) #Localiza y borra el número de la lista
    indice=indice+1 #Evalua el siguiente indice
print("Números pares hallados")
print(numeros_lista)

#Sumar y sacar promedios de los pares
division=float #Como no siempre la división va a dar un número entero por la cantidad actual de pares, es un número real obligatoriamente
division=len(numeros_lista) #Determina cuantos números pares hay dentro de la lista
print(division)
suma=float #Por precauciones se puso float, aunque no es necesario
suma=0
i=1
while i>0: #Ponemos un condicional simple que pueda ayudar con la repitición de abajo y realizar la sumatoria
    repetir=0
    for repetir in range (0, division, 1): #Sumatoria que saca cada elemento y lo va sumando
        y=numeros_lista.pop(0)
        suma=suma+y
    i=i-2
operar=suma/division #Saca el respectivo promedio
print("El promedio de la suma de los números pares es")
print(operar) #El promedio

#Se que había una manera más sencilla de resumir esto pero... Se me olvido :(
#Además que quería experimentar con los comandos de lista y se me hacen super buenos para estas ocasiones
#Ayudan a hacer como un tipo de [Guardado] en los datos o.o
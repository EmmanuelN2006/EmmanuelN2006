#Determinación de la sucesión de Fibonacci
nmax = int(input("Introduzca la posición que quieras saber: ")) #Posición que quieres saber
penultimo = 0
ultimo = 1
print(penultimo)
print(ultimo)
cont = 2
#En este programa dará el orden de los números pertenecientes a la sucesión en su posición
#Por lo que dará 0=0, 1=1, 2=1, 3=2, 4=3, 5=5, 6=8, posición = número
while cont < nmax: #Limitante para no pasar del valor
    suma = penultimo + ultimo #Suma el 0 y el 1
    penultimo = ultimo #Actualiza el 0 y lo vuelve el 1
    ultimo = suma #Convierte el 1 en la suma del penultimo 1 con el 1 ultimo y hace el ciclo
    cont = cont + 1 #Aumenta el limitador
    print(ultimo)#El número siguiente de la posición
print("Fin")

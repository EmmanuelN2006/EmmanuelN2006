n=int #Primero que determine si el número es positivo, negativo o es cero
i=int #Repeticiones
numeros= [] #Lista de los números almacenados
#Introducir variables para saber si es positivo, negativo o 0.
print("Introduce un número entero por favor")
n=int(input())
if n>0: #Determinación del signo del número, primera parte del punto 7.
    print("Tu número es positivo")
    exit
else:
    if n==0:
        print("Tu número es cero")
        exit
    else:
        if n<0:
            print("Tu número es negativo")
        else:
            exit
i=0
#Introducir números enteros hasta que el número introducido sea 0, segunda parte del punto 7.
while i==0: #Mantenemos un bucle infinito para agregar elementos infinitos mientras se cumplan cierta condiciones
    print("Ingrese un valor entero")
    n=int(input())
    if n==0: #Cuando el valor ingresado sea cero, el programa se detendra y pondrá todos los números ingresados antes del cero
        print("El número ingresado es cero")
        print("Números ingresados antes que el cero fueron="+(str(numeros)))
        exit() #Finaliza el programa 
    else:
        numeros.append(n) #Almacena el número diferente de 0
        if n>0: #Permite el flujo de más números y dice si es positivo o negativo
            print("El número es positivo")
        else:
            if n<0:
                print("El número es negativo")

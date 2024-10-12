# Hecho y explicado por Emmanuel, casi le da una hemorragia haciendo esto :C
#Escribir los números primos desde 1 hasta x número introducido
print("Escribir hasta que valor quieres que se busquen numeros primos desde 1")
vmax = int(input())
diviendox = 0
divisores = 0
# Asignamos las variables que son 4: x; diviendo, y; divisor, vmax; valor final en el cual 
#se evaluaran que numeros son primos, y divisores; variable que demostrará si es primo o no.
while True:    #Esto simula el Hacer (Do) de los ciclos
    # Usando el comando hacer podremos clarificar un poco mejor el proceso que queremos hacer, 
    #por lo que se hizo un fin alternativo que no es obligatorio pero igual sirve para detener por si las dudas
    diviendox = diviendox + 1 #Variable que recorrerá desde 1 hasta el número ingresado
    if diviendox <= vmax: #Condición de que no se pase o sea mayor que el valor ingresado
        pass
    else:
        print("Números primos encontrados")
    # Aquí empieza lo que sería el bucle que se necesitaba, hacer que la variable divisory sea 
    #la que aumente su valor a medida que y sea menor o igual que x es el bucle que no había 
    #encontrado y con los condicionales permitimos que el sistema ignore un divisory si este sobrepasa 
    #el valor de diviendox que a su vez si este se pasa del vmax detendrá el mecanismo tanto con 
    #el condicional de arriba como con el condicional Do que mantiene todo.
    for divisory in range(1, vmax + 1, 1): #Va aumentando los divisores para el diviendo actual
        if divisory <= diviendox:
            if diviendox % divisory == 0: #Números que si dividen
                divisores = divisores + 1 #Divisores del número
    if divisores < 3: #Si el número solo tiene 2 o 1 divisor, se dice que es primo
        if diviendox <= vmax: #Solo imprime números menores o iguales al introducido
            print(diviendox)
    divisores = 0
    # Y se debe resetear los divisores para que la variable no continua subiendo a medida que evalua los otro números
    if diviendox > vmax: break #Rompe la frecuencia cuando se pase el valor ingresado
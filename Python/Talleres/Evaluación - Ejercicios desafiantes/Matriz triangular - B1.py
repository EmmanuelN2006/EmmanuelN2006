import numpy as np

Continuar = bool; Continuar = True
print("Bienvenido, analizaremos si la matriz que vaya a ingresar es triangular o no, para eso ingrese un número de filas")
print("El valor ingresado debe ser mayor que 0 y menor e igual que 50")

while Continuar == True:
    filas = int(input("=")) #Ingresa el número de filas
    if filas <= 0: #Limitante 1
        print("Cerrando el programa")
        Continuar = False
        exit()
    if filas > 50: #Limitante 2
        print("Valor excedido, cerrando el programa")
        Continuar = False
        exit()

    Matriz = np.zeros((filas, filas)) #Matriz creada
    # print("Ingrese valores para la matriz")
    # print("Ingresar los valores de la siguiente manera= 1 2 3 4")

    for fila in range(filas):
        Fila_nueva = input(f"Valores[{fila}]= ") #Números que ingresará
        Valores_nuevos = list(map(int, Fila_nueva.split())) #Hace que a partir de los números dejados en espacios
        #1. Los sepa separar por los espacios e identificar por ser números
        #2. Haga una lista y que tenga un orden asignado al string
        Matriz[fila] = Valores_nuevos #Integra los números a la fila en el orden asignado
    print(Matriz)

    ##Identificar si la matriz es triangular
    def Triangular_superior(Matriz):
        #Verifica si una matriz es triangular superior
        for i in range(1, filas): #Comprueba los elementos debajo de la diagonal
            for j in range(i): #i = filas y j=columnas
                if Matriz[i, j] != 0: #Si alguno llega a ser diferente de 0
                    return False #No es triangular superior - osea que abajo no todos son 0
        return True

    def Triangular_inferior(Matriz):
        # Verifica si una matriz es triangular inferior 
        for i in range(filas): #i = filas y j=columnas
            for j in range(i + 1, filas): #Comprueba los elementos encima de la diagonal
                if Matriz[i, j] != 0: #Si alguno llega a ser diferente de 0
                    return False #No es triangular inferior - osea que arriba no todos son 0
        return True

    # Verificar el tipo de matriz; Diagonal, triangular superior o triangular inferior
    if Triangular_inferior(Matriz) and Triangular_superior(Matriz): #Cuando la matriz superior e inferior sean verdaderos
        print("La matriz es diagonal")
    elif Triangular_superior(Matriz): #Cuando la matriz triangular sea verdadero
        print("La matriz es triangular superior")
    elif Triangular_inferior(Matriz): #Cuando la matriz triangular sea verdadero
        print("La matriz es triangular inferior")
    else: #Cuando la matriz no contiene ninguna característica
        print("La matriz no es triangular")
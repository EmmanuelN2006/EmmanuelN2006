#Multiplicación punto de matrices
import numpy as npy

print("Por favor ingresar dos valores aleatorios")
a=int(input("Valor de a=")) #Rango inferior
b=int(input("Valor de b=")) #Rango superior

#Creación de las matrices de 5x5 y 5x4
n=5; m=5; n1=5; m1=4
ma1 = npy.random.randint(a, b, (n, m)) #Matriz tamaño 5x5
ma2 = npy.random.randint(a, b, (n1, m1)) #Matriz tamaño 5x4
#npy.random.randint(valor inferior, valor superior, (tamaño de la matriz)), el comando lo que hace es 
#llenar la matriz con vaLores entre rango inferior y rango superior
print(ma1)
print(ma2)


             

#Multiplicación punto de matrices determinadas
import numpy as npy
print("Multiplicación de los siguientes dos vectores")

#Creación de las matrices de 3x5 y 5x3
n=3; m=5; n1=5; p=3
ma1 = npy.array([[3,8,4,9,2],[9,2,9,4,6],[3,6,1,1,3]]) #Elementos de la matriz 1
ma2 = npy.array([[5,7,5],[5,1,9],[4,8,2],[4,0,9],[2,5,7]]) #Elementos de la matriz 2
n, m = ma1.shape #Definir el tamaño de la matriz
m, p = ma2.shape #Definir el tamaño de la matriz
print(ma1)
print(ma2)

#Multiplicación matriz de ambas matrices
ma3 = npy.zeros((n, p)) #Matriz resultante de la multiplicación 3x3
print(ma3)
if m==n1: #Verificación que cumpla con la condición de la multiplicación punto
    print("Multiplicación aprobada")
for i in range (n):
    for j in range (p):
        for k in range(m):
            ma3[i, j] += ma1[i, k] * ma2[k, j] #Ciclo para ir sumando cada posición
print(ma3)

#Punto 1 - Implementar la búsqueda binaria para un vector o lista de N elementos y encontrar x número
import numpy as np

#Lista de n elementos
n = int(input("Ingrese la cantidad que quieras en la lista="))
numero = int(input("Ingrese el número que quieres buscar="))
Lista = np.random.randint(0, 101, n) #(a, b, tamaño)
Lista.sort()
Lista1 = []
Lista2 = []
print(len(Lista))
print(Lista)
Mitadpar = int(len(Lista)/2)
Mitadimpar = int((int(len(Lista))-1)/2)

#Proceso de dividir si es par e impar
Cant = len(Lista)
if Cant%2==0:
    Mitad = int(len(Lista)/2)
    for i in range(0, Mitad):
        Lista1.append(int(Lista[i]))
    for i in range(Mitad, Cant):
        Lista2.append(int(Lista[i]))
else:
    Mitad = int((int(len(Lista))-1)/2)
    for i in range(0, Mitad+1):
        Lista1.append(int(Lista[i]))
    for i in range(Mitad, Cant):
        Lista2.append(int(Lista[i]))    

if numero < Mitadpar:


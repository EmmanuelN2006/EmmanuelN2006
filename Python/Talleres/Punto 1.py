#Punto 1 - Implementar la búsqueda binaria para un vector o lista de N elementos y encontrar x número
import numpy as np

#Lista de n elementos
n = int(input("Ingrese la cantidad que quieras en la lista="))
Lista = np.random.randint(0, 101, n); Lista.sort(); Lista1 = []; Lista2 = [] #(a, b, tamaño), #Ordenamiento de la matriz, #Creación de listas divididas
print(Lista)
numero = int(input("Ingrese el número que quieres buscar="))
Temp_lista1 = []; Temp_lista2 = []
Mitadpar = int(len(Lista)/2);Mitadimpar=int((len(Lista)+1)/2);Cant=len(Lista) #Variables importantes
#Ver si el número ingresado existe
Busqueda = np.where(Lista==numero)[0]
if len(Busqueda) > 0:
    posicion = Busqueda[0]
    print("El número ingresado existe, buscando...")
else: 
    print("El número ingresado no existe..")
    exit()
#Determinar si la Mitad es par, y si la mitad es el número que estamos buscando
if Cant%2==0:
    Mitad=Mitadpar
    Par=True; Impar=False
    if Lista[Mitad]==numero:
        print("Número encontrado")
        print(f"La posición de {numero} es {Lista[Mitad]}")
        exit()
    if Lista[Mitad-1]==numero:
        print("Número encontrado")
        print(f"La posición de {numero} es {Lista[Mitad-1]}")
        exit()
else:
    Mitad=Mitadimpar
    Impar=True; Par=False
    if Lista[Mitad]==numero:
        print("Número encontrado")
        print(f"La posición de {numero} es {Lista[Mitad]}")
        exit()

#Proceso de dividir si es par e impar, lista primera
if Par==True:
    for i in range(0, Mitad):
        Lista1.append(int(Lista[i]))
    for i in range(Mitad, Cant):
        Lista2.append(int(Lista[i]))
elif Impar==True:
    for i in range(0, Mitad):
        Lista1.append(int(Lista[i]))
    for i in range(Mitad-1, Cant):
        Lista2.append(int(Lista[i]))  
print(Lista1); print(Lista2)  
#Proceso segundario de nueva lista para buscar
Temp_lista1 = Lista1
Temp_lista2 = Lista2
Lista1 = []
Lista2 = []
if Par==True:
    if numero > Mitad:
        

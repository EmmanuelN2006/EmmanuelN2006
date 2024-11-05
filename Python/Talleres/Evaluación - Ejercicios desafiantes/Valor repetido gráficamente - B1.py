import random as rd
import matplotlib.pyplot as plt

print("¿Cuántos valores quieres que agreguen?")
n = int(input("= ")) #Número de valores que se van a agregar
Numeros = [] #Lista de los números almacenados
Repeticion = dict() #Describe lo que cantidad de repeticiones que hay por número, crea un diccionario vacío
for i in range(n): #i = cantidad de repeticiones que dependerá de n
    Random = rd.randint(0, 100) #Entre mayor el rango, más difícil la repetición
    Numeros.append(Random) #Agrega el numero a la lista de los numeros
for i in range(n):
    Repeticiones = Numeros.count(Numeros[i]) #Cuenta la cantidad de veces que tiene ese numero
    Repeticion[Numeros[i]] = Repeticiones #Si ve que el número y su cantidad no existe, lo agrega al diccionario
print(Numeros)
Numeros.sort() #Ordena de menor a mayor
print(Repeticion)

Elementos = list(Repeticion.keys()) #fila x usando diccionario 
Frecuencias = list(Repeticion.values()) #fila y usando diccionario

plt.bar(Elementos, Frecuencias, color="skyblue") #Establece la relación del elemento x con el elemento y con barras
plt.xlabel("Elemento")
plt.ylabel("Frecuencia")
plt.title("Frecuencia de valores generados aleatoriamente")
plt.xticks(range(0, 101, 10)) #Escala que maneja el eje indicado
plt.show()

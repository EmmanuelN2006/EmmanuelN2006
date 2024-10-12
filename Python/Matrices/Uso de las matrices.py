#Uso de las matrices
import numpy as num #Instalar librería numpy con pip install numpy si sale que no existe
import matplotlib.pyplot as mt #Instalar librería matplotlib con pip install matplotlib si sale que no existe

n=100
A = num.zeros(n) #Crear un vector con cantidad n pero rellenar con 0
B = num.array([1, 2, 3, 4], dtype= num.float64) #Array significa crear un vector 
#a partir de la vista y float64 significa la cantidad de cifras significativas que puede guardar 32, 64, 128
C = num.random.randint(0, 10, n) #Crea una lista de n cantidad de elementos 
#que varían entre los valores 0 a 10
D = num.linspace(-720, 720, n) #Desde un valor de -720 hasta 720 en n valores 
#va sumando una cantidad exacta para llegar a los límites
E = num.arange(-720, 720, 15) #Desde un valor inicial va sumando 15 
#hasta llegar al límite de 720, no es exacto como linspace; pero si ponemos 721 si llega a 720
X = num.radians(E) #Convertir el valor actual en radianes
Y = num.sin(X) #Seno del radian
Y2 = num.cos(X) #Coseno del radian
mt.plot(X, Y, "g-", X, Y2, "r-") #Dibuja una gráfica 
#a partir de los comandos dados, al ser una lista recorre todos los elementos de E, 
#donde g- es un color y r- otro color
mt.show() #Abre una aplicación de gráfica con el comando plot

print(A)
print(B)
print(C)
print(D)
print(len(D)) #Imprime la cantidad de elementos en D
print(E)
print(len(E)) #Imprime la cantidad de elementos en E
print(X[50]) #Elementos X en la posición 50
print(X[-23]) #Elemento X en la posición -23
print(X[:10]) #Todos los elementos desde 1 hasta el 10, o en lista desde 0 hasta 9
print(X[-23:]) #Elementos desde -23 hasta -1, o en lista desde -1 hasta -23
print(X[3:5]) #Elementos de X desde 3 hasta el valor final-1, en este caso 4
print(X[-7:-3]) #Elementos de X desde -7 hasta el valor final-1, en este caso -4

mat1 = num.identity(n) #Crear una matriz identidad de n x n
print(mat1) #Imprimir la identidad

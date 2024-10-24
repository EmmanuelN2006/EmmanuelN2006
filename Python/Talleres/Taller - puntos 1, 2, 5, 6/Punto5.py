#Punto 5:
#Construir un programa que reciba las componentes en x y y de un vector y 
#calcule una proyección del mismo sobre un par de vectores unitarios al azar. 
#El programa de permitir recibir más de un vector, pero uno a la vez. 
#Para cada caso graficar el punto inicial y los puntos que representan las proyecciones.
import numpy as np
import matplotlib.pyplot as plt
#Fuente para gráficar los vectores:
#https://www.delftstack.com/es/howto/matplotlib/plot-vector-using-matplotlib-python/

#Variable de error
Errorx= True
Errory= True

#Creación de un vector
#Valor de x
print("Vamos a crear un vector de 2 dimensiones, por favor siga las indicaciones")
while Errorx==True:
    try:
        x = int(input("Ingresar valor numérico para x="))
        Errorx=False
    except ValueError:
        print("El valor ingresado no es válido")
#Valor de y
while Errory==True:
    try:
        y = int(input("Ingresar valor numérico para y="))
        Errory=False
    except ValueError:
        print("El valor ingresado no es válido")

#Vector principal
Vector_f = np.array([[x],[y]])
print(Vector_f)

#Vectores unitarios
Vector_unix = np.array([[1],[0]])
Vector_uniy = np.array([[0],[1]])
print(Vector_unix)
print(Vector_uniy)

#Elección del vector unitario
eleccion_1 = 1
eleccion_2 = 2
eleccion=np.random.randint(1,3)
print(eleccion)
if eleccion==eleccion_1:
    Vector_uni = Vector_unix
else:
    Vector_uni = Vector_uniy

#Calculo de la proyección del vector_f sobre algún vector unitario
#Producto_Punto:
for i in range(0, 1):
    sumatoriax = Vector_uni[i]*Vector_f[i]
for i in range(1, 2):
    sumatoriay = Vector_uni[i]*Vector_f[i]
Producto_Punto = sumatoriax + sumatoriay
print(Producto_Punto)
#Proyeccion
Proyeccion = Producto_Punto * Vector_uni
Proyeccionx = int(Proyeccion[0])
Proyecciony = int(Proyeccion[1])
print(Proyeccion)

#Visualización de los vectores - Pendiente
fig, ax = plt.subplots(figsize = (12, 7)) #Tamaño de la ventana
ax.quiver(0, 0, x, 0, 3) #VECTOR U X
ax.quiver(0, 0, 0, y) #Vector U Y
ax.quiver(0, 0, x, y) #No se que hace pero hace funcionar el código JSJSJS
ax.quiver(0, 0, Proyeccionx, Proyecciony, 3) #Vector proyección
ax.set_title('Vectores')
plt.ylim(-25, 25)
plt.xlim(-25, 25)
plt.show()

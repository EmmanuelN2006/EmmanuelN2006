#Regresión lineal de un archivo Excel

#Bibliotecas a utilizar
import pandas as pd #Lectura de archivos de columnas y filas
import matplotlib.pyplot as mpl #Creación de gráficas
from sklearn.linear_model import LinearRegression #Calculo de operaciones complejas

#Leer un documento de excel
archivo_leer = pd.read_csv('Python\Lectura de un archivo excel\Excelpython.csv') #Lectura del archivo
#La lectura del archivo dependerá de cual es el area de trabajo de tu Visual Studio Code, en mi caso
#Python\Lectura de un archivo excel\Excelpython.csv está dentro de la carpeta de área de trabajo
lista = list(archivo_leer)
Edad = archivo_leer['Edad'].to_list()
Altura = archivo_leer['Altura'].to_list()

#FUNCIÓN regresión lineal dada por comandos directamente
X = archivo_leer[['Edad']]  # Variable independiente (X)
y = archivo_leer['Altura']  # Variable dependiente (y)
# Crear el modelo de regresión lineal
modelo = LinearRegression()
# Ajustar el modelo con los datos
modelo.fit(X, y)
# Predecir los valores de y basados en X
y_pred = modelo.predict(X)
print(y_pred)
# Coeficiente de la regresión (pendiente) y el intercepto (b)
pendiente = modelo.coef_[0]
intercepto = modelo.intercept_
# Visualizar los datos y la línea de regresión
mpl.scatter(X, y, color='blue', label='Datos')
mpl.plot(X, y_pred, color='red', label='Línea de regresión')
mpl.xlabel('Edad')
mpl.ylabel('Altura')
mpl.legend()
mpl.show()

#Cálculo de regresion lineal
n=11 #xp = yp = x2p = xyp = 0
xp = 0 #Sumatoria de x
yp = 0 #Sumatoria de y
x2p = 0 #Sumatoria de x^2
xyp = 0 #Sumatoria de xy
#Sumatoria en x
for i in range (0, n):    #for i in range (0,n):
    xn = Edad[i]          #xp += xn
    xp += xn              #x2p += xn**2
#Sumatoria en y           #yp += yn
for i in range (0,n):     #xyp += xn*yn
    yn = Altura[i]
    yp += yn
#Sumatoria en x^2
for i in range (0,n):
    xn = Edad [i]
    x2p += xn*xn
#Sumatoria en xy
for i in range (0,n):
    xn = Edad[i]
    yn = Altura[i]
    xyp += xn*yn

#Operación para calcular el a de y=ax+b
a = ((n*xyp-xp*yp)/(n*x2p-(xp*xp)))
#Operación para calcular el b de y=ax+b
b = ((yp - a*xp)/n) #Parecido a b1, pero menos exacto
b1 = (((x2p*yp)-(xyp*xp))/(n*x2p-(xp)**2)) #Parecido a b, pero más exacto
#Coeficiente de correlación y coeficiente de determinación
xpro = 0
ypro = 0
for i in range(0,n):
    xpro += xn
    ypro += yn
x2prot = 0
y2prot = 0
xyprot = 0
for i in range (0,n):
    x2prot += (xn - xpro)**2
    y2prot += (yn - ypro)**2
    xyprot += (xn - xpro)*(yn - ypro)
#Cálculo de los coeficientes
r=((xyprot)/((x2prot)*(y2prot))**1/2) #Coeficiente de correlación
print(f"El coeficiente de correlación es {r}")
#Representación de la fórmula de regresión lineal
print(f"los valores de b y b1 son {b} y {b1}")
print(f"La fórmula de regresión lineal es y={a}x+{b}")
#Representación gráfica
y_formula = [a * x + b for x in Edad] #Para cada valor de 'Edad', calculamos el valor de 'y' con la fórmula
mpl.scatter(Edad, Altura, color='blue', label='Datos originales')  # Gráfico de puntos originales
mpl.plot(Edad, y_formula, color='green', label='Línea de regresión')  # Línea de regresión
#Label - Nombre para la linea
#mpl.scatter() ; Graficar puntos específicos
#mpl.legend() ; Graficar las etiquetas de label de las lineas
#Mostrar gráfica y nombrar ejes
mpl.xlabel('Edad')
mpl.ylabel('Altura')
mpl.legend()
mpl.show()
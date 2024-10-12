#Matrices tal vez

import numpy as np

n= 100
m1 = np.random.randint(0, 3, (n,n)) #Valores entre 0 a 3 para una matriz de n x n
m2 = np.random.randint(0, 3, (n,n)) #Valores entre 0 a 3 para una matriz de n x n
m3 = m1 @ m2 #@ es la multiplicación de matrices de algebra, osea, fila con columna o lo que sería producto punto, siempre y cuando las filas sean la misma cantidad que columnas
m4 = m1+m2 #Suma de matrices con las mismas características

print(m1)
print(m2)
print(m3)
print(m4)
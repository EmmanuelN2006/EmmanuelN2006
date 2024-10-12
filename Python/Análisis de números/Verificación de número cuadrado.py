#Variables a utilizar
n=int #Número entero a evaluar si tiene raíz cuadrada
secuencia=int #Valores posibles
i=int #Valores para comprobar si existe raíz o no

#Introducir variables
print("Por favor ingrese el número que quieras comprobar si tiene raíz")
n=int(input("="))
i=0 #Valor que aumentará de uno en uno hasta saber la base que da ese valor

#Proceso de encontrar la raíz, lo que se prueba es que a medida que secuencia aumente el x^2, si este llega a ser igual que n ya es la rta
for i in range(1, n+1, 1): 
    secuencia=i**2 #Representación de la potencia
    resultado=n/secuencia #Si la secuencia es igual a n, entonces sabremos cuál es el i correspondiente
    if secuencia==n or resultado==1:
        print("La raíz cuadrada es +/-"+" "+(str(i)))
        break
    elif secuencia>n: #En el caso que no lo diera es porque el resultado no es un número entero, por lo que usamos esto
        print("No hay raiz cuadrada en números enteros, por lo que el resultado original sería")
        import math 
        math.sqrt(n)
        print(math.sqrt(n))
        break

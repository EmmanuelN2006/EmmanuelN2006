##Un número es un cuadrado perfecto si su raíz cuadrada es un número exacto (sin decimales). Por ejemplo, el 4 es un cuadrado perfecto (2²), 
# al igual que lo son el 36 (6²) y el 3.500.641 (1871²). Todos los números que no son cuadrados perfectos pueden multiplicarse por otros para conseguir serlo. 
# Por ejemplo, el número 8 no es un cuadrado perfecto, pero al multiplicarlo por 2 se obtiene el 16, que sí lo es.Entradas del programa: La entrada comienza con un número 
# que indica cuántos casos de prueba tendrán que procesarse. Cada caso de prueba consiste en un número mayor que 0 y menor que 231.
# Salidas: Para cada caso de prueba, el programa escribirá por la salida estándar, en una línea independiente, el número más pequeño que al ser multiplicado por el número del 
# caso de prueba da como resultado un cuadrado perfecto.

n = int(input("inserte un numero entero: "))
c_perfc:0

# for i in range(1,n+1):
#   c_perfc=n*i
#   raiz=c_perfc**(1/2)
#   if raiz-int(raiz)==0:
#       print(i)
#       break


for i in range(n):
    a=int(input("Ingrese el número otra vez: "))
    for j in range(1, a+1):
        c_perfc= a*j
        raiz= c_perfc**(1/2)
        if raiz-int(raiz)==0:
            print(f"el numero mas pequeño que al multiplicar con {a} de un cuadrado perfecto es:{j}")
            break
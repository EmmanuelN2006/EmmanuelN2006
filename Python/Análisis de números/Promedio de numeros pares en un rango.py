
print("Escribe el número máximo donde se quiera evaluar los números pares")
vmax=int(input())
print("El número máximo será"); print(vmax)
divisor=int
suma=int
x=int
operar=float
sobrante=int

#Evaluamos desde 0 hasta vmax para saber que números son pares y vamos almacenandolos
divisor=vmax
suma=0
sobrante=0
for x in range (0, vmax+1, 1):
    if x / 2==sobrante:
        suma=suma+x
        sobrante=sobrante+1
operar=suma/divisor
print(operar)
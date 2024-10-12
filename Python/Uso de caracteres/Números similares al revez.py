#Escribir un programa que lea un número entero y determine si este es un palíndromo, 
#es decir, que se lee igual de izquierda a derecha que
#de derecha a izquierda. Estos números se conocen como como capicúas.
#12321, 454, 555, etc.
#Nota: asumir que el número dado no tendrá ceros a la derecha.

#Variables
print("Ingresar un número por favor") 
n=input() #Convierte el número en caracteres
x=len(n) #Mira cuántas cifras tiene
m='' #Espacio
z=int(n) #Convierte el número ingresado en números usables
print("Z es "+str(z)) #Muestra el número que ingresaste
    
#Comprobación de ceros
for i in range(0, x, 1): #Va volteando el número ingresado
    m=n[i]+m
m1=int(m) #El número invertido lo convierte en un valor 
if m1==z:
    print("Son capicúas") #El número ingresado y el número invertido son iguales
else:
    print("No son capricúas") #El número ingresado y el número invertido no son iguales
print(m1)
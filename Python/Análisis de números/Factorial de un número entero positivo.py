#Variables a utilizar
n=int #El número que se le sacará el factorial
factorial=int #Resultado
i=int #Variable para condicionar la repetición y la operación
#Introducir variables
print("Por favor introduzca el número entero que vaya a usar")
n=int(input("Valor de n"))
#Comprobación de número positivo y operación a utilizar
if n>=0: #Esto es para detener el uso de los números negativos en el factorial
    print("Entero positivo"+" "+(str(n))+" "+"es positivo")
else:
    print("El número no es positivo, intentelo de nuevo")
    exit()
#Comandos para calcular factorial
i=1
factorial=1 #Cuando n=0 o n=1 estos valores harán que den siempre 1 en la respuesta
while i<=n: #Finaliza el condicional cuando se haya cumplido el factorial
    factorial=factorial*i #Representación de la operación de la factorial
    i=i+1 #Aumentando el condicional de la operación
print("El factorial de"+" "+(str(n))+" "+"es"+" "+(str(factorial)))
#El código más corto que he hecho :D hasta que llego el ejercicio 8
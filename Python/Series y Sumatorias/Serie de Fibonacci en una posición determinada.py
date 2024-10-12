#Escribir un programa que escriba el termino N de la serie de Fibonacci, 
#donde N es un número dado por el usuario. Solo debe imprimir ese número.
#Variables
print("Ingresar un número desde 0 hasta infinito para la serie de Fibonacci")
i=2 # i=int
n=int(input()) #Esta serie a diferencia del otro Fibonacci que tengo, da el número que se encuentra en la posición
print("Para comprobar, su N es="+str(n))
#Anteriormente diriamos que 0=0, 1=1, 1=1, 2=1, 3=2, 4=3, 5=5, posición = número
#La serie es numero anterior + numero sumado y actualizar términos

if n==0: #Ahorra el proceso cuando pide la posición 0
    print("El número en la posición 0 de la serie de Fibonacci es 0")
    exit()
if n==1: #Ahorra el proceso cuando pide la posición 1
    print("El número en la posición 1 de la serie de Fabonacci es 1")
    exit()

if n>=2:#Aquí ya se parece al otro programa que tengo, solo que este calcula hasta un tope y da ese número
    numer_anterior=0
    numero_sum=1
    while i<=n:
        numer_total=numer_anterior+numero_sum
        numer_anterior=numero_sum
        numero_sum=numer_total
        i=i+1
    print(f"El número en la posición {n} de la serie de Fibonacci es {numer_total}")
    exit()

# numer_anterior=0
# numero_sum=1
# while i<=n: #Limitante para no pasar del valor
#     numer_total=numer_anterior+numero_sum #Suma el 0 y el 1
#     numer_anterior=numero_sum #Actualiza el 0 y lo vuelve el 1
#     numero_sum=numer_total #Convierte el 1 en la suma del penultimo 1 con el 1 ultimo y hace el ciclo
#     i=i+1 #Aumenta el limitador

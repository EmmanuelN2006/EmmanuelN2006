#El programa hace que lo que ingreses; ya sea palabra o números o letras con números, 
#voltearlos y agregar 0 entre los espacios

palabra=input("Ingresar la palabra") #Ingresar una palabra y/o números para convertirlos en cadena
n=len(palabra) #Describe la longitud de la palabra, por ejemplo hola son 4 y 1234 es 4
print(n) #Imprime la longitud
nulo= '0' #Caracter 0
separado= '' #Espacio
f=n-1 #Limitador para que solo ponga 0 entre los espacios exceptuando el inicio y el final 
print(f)
for i in range (0, n, 1):
    separado=palabra[i]+separado #agregar letra y espacio
    if i<f:
        separado=nulo+separado #agregar 0+letra y espacio
print(separado) #Palabra transformada
    
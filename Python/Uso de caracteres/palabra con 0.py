palabra=input("Ingresar la palabra")
n=len(palabra) #Mira la cantidad de letras de la palabra
print(n)
nulo= '0' #Caracter 0
separado= '' #Espacio
f=n-1 #Limitador para que solo ponga 0 entre los espacios exceptuando el inicio y el final 
print(f)
for i in range (0, n, 1):
    separado=separado+palabra[i] #agregar espacio y letra
    if i<f:
        separado=separado+nulo #agregar 0+espacio y letra
print(separado) #Palabra transformada
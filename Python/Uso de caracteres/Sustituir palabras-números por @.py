palabra=input("Ingresar la palabra")
n=len(palabra) #Mira la cantidad de letras y cifras de la palabra-número
print(n)
nulo= '@' #Símbolo a reemplazar
separado= '' #Espacio para reemplazar el valor
f=n-1 #Limitador
print(f)
for i in range (0, n, 1):
    if i<n:
        separado=separado+nulo #Agrega el espacio con el @ y lo hace tantas veces n
        #en relación a la cantidad de cifras
print(separado)
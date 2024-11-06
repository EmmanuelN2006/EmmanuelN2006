#Originalmente usamos el comando .count() para que python analice el elemento y mire cuantas veces existe en la lista
lista = [7,5,5,5,6,7,8]
lista.count(7) #El resultado es 2
lista.count(5) #El resultado es 3

#Pero si necesitas un código que haga ese trabajo sin utilizar eso es:
lista = [8, 7 , 6, 5, 4, 4 , 3] #numeros en la lista

# Contador manual
contador = 0
for i in range(len(lista)):
    contador = 0
    elemento = lista[i]
    for i in lista:
        if i == elemento:
            contador += 1
    print(f"la frecuencia del elemento {elemento} es {contador}")
         

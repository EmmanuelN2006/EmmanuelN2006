#Adivina el número

import random as rd
Jugar = bool; Jugar = True  

print("¡Hola!, ¿Cuál es tu nombre?")
Nombre = input("= ")
print(f"Hola {Nombre}, ¿Quieres jugar a un juego?")

Respuesta = input("Si/No: ").lower()
if Respuesta != "si":
    print("Okay... Chao")
    Jugar = False
    exit()

### Creación del número aleatorio y adivinanza ###
while Jugar: 
    print("Dime un número de 1 para adelante que quieras")
    Número_máximo = abs(int(input("= ")))
    print(f"Me he imaginado un número entre 1 a {Número_máximo}")

    Numero_elegido = rd.randint(1, Número_máximo)
    Adivinado = bool; Adivinado = False

    while not Adivinado:
        print("El número es..?")
        Numero_adivinado = int(input("= "))
        if Numero_adivinado == Numero_elegido:
            print("Acertaste!")
            Adivinado = True
        
        if Numero_adivinado < Numero_elegido:
            print("Frío Frío... es muy pequeño")
            
        if Numero_adivinado > Numero_elegido:
            print("Frío Frío... es muy grande")
        
    print("¿Quieres volver a jugar?")
    Respuesta = input("Si/No: ").lower()
    if Respuesta != "si":
        print("Okay :(, adiós")
        Jugar = False
        exit()
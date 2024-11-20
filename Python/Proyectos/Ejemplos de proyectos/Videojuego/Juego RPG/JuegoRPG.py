##El código muestra lo que es un juego RPG usando la terminal como medio de mostrar todo lo que pasa y lo que uno quiere hacer

import numpy as np
import random as rd
import time as tm

print("Hola! ¿Qué quieres hacer?"); print("Ajedrez / Fantasía") ##El ajedrez es un proyecto aparte, ya que esto es un conjunto de dos juegos
Modo = input("= ").lower()
                    
if Modo == "fantasía":
    ###Creamos inventario y variables###
    Enemigo_encuentro = int; Enemigos = {-4:"Dragón", -3:"Serpiente", -2:"Cocodrilo", -1:"Gorila", 0:"Slime",1:"Duende", 2:"Halcón", 3:"Caballero", 4:"Rey"}
    Daño_enemigos = {"Dragón":60, "Serpiente":15, "Cocodrilo":35, "Gorila":21, "Slime":1,"Duende":5, "Halcón":10, "Caballero":25, "Rey":50}
    Vida_enemigos = {"Dragón":260, "Serpiente":60, "Cocodrilo":105, "Gorila":110, "Slime":20,"Duende":25, "Halcón":40, "Caballero":160, "Rey":180}
    Loot_enemigos = {"Dragón":"Cuernos","Serpiente":"Dientes","Cocodrilo":"Piel", "Gorila":"Fruta", "Slime":"Baba","Duende":"Dinero","Halcón":"Plumas","Caballero":"Hierro","Rey":"Bendiciones"}
    Inventario = {}
    ### ### ###
    Jugar = True
    print("Bienvenido a este mundo de fantasía, ¿Qué quieres hacer?")
    while Jugar:
        Vida_usuario = 200
        print("Inventario, pelear o descansar")
        respuesta = input("= ").lower()
        if respuesta == "inventario":
            print("Este es tu inventario")
            print(Inventario)
        if respuesta == "pelear":
            print("Buscando enemigo...")
            tm.sleep(4)
            Enemigo_encuentro = rd.randint(-4,4)
            Actualenemigo = Enemigos[Enemigo_encuentro]
            print(f"¡Se ha cruzado un enemigo! {Actualenemigo} te quiere atacar!"); pelea = True
            Vida_usuario = Vida_usuario
            Vida_enemigo = Vida_enemigos[Actualenemigo]
            while pelea:
                print(f"Tu vida = {Vida_usuario}")
                print(f"Vida del enemigo = {Vida_enemigo}")
                print("Atacar o huir"); answer = input("= ").lower()
                if answer == "atacar":
                    ###Turno de ataque###
                    Velocidad = rd.randint(0,1)
                    if Velocidad == 0:
                        ##El turno es del jugador##
                        print("Has atacado primero")
                        tm.sleep(1)
                        Ataque = rd.randint(20,70)
                        if Ataque == 70:
                            print("Te has inspirado y sacaste un ataque crítico!")
                        Vida_enemigo = Vida_enemigo - Ataque
                        print(f"Has hecho {Ataque} de daño!")
                        tm.sleep(1)
                        ##Turno del enemigo
                        print("El enemigo se movió con velocidad")
                        Ataque_enemigo = Daño_enemigos[Actualenemigo] - rd.randint(0,10)
                        Vida_usuario = Vida_usuario - Ataque_enemigo
                        print(f"El enemigo te ha quitado {Ataque_enemigo}")
                        tm.sleep(1)
                        ###Comprueba si alguien murio###
                        if Vida_enemigo <= 0:
                            print("El enemigo ha muerto! Has ganado!")
                            Numero = rd.randint(2,5)
                            try:
                                Cantidad = Inventario[Loot_enemigos[Actualenemigo]] + Numero
                                Inventario[Loot_enemigos[Actualenemigo]] = Cantidad
                            except KeyError:
                                Inventario[Loot_enemigos[Actualenemigo]] = Numero
                            print(f"Has conseguido {Numero} {Loot_enemigos[Actualenemigo]}"); pelea = False
                            tm.sleep(2)
                        if Vida_usuario <= 0:
                            print("Has caído ante el enemigo! ... ..")
                            print("Has podido huir..."); pelea = False
                    if Velocidad == 1:
                        ##Turno del enemigo
                        print("El enemigo se movió primero!")
                        Ataque_enemigo = Daño_enemigos[Actualenemigo] - rd.randint(0,10)
                        Vida_usuario = Vida_usuario - Ataque_enemigo
                        print(f"El enemigo te ha quitado {Ataque_enemigo}")
                        tm.sleep(1)
                        ##El turno es del jugador##
                        print("Vas a atacar")
                        Ataque = rd.randint(20,70)
                        if Ataque == 70:
                            print("Te has inspirado y sacaste un ataque crítico!")
                        Vida_enemigo = Vida_enemigo - Ataque
                        print(f"Has hecho {Ataque} de daño!")
                        tm.sleep(1)
                        ###Comprueba si alguien murio###
                        if Vida_enemigo <= 0:
                            print("El enemigo ha muerto! Has ganado!")
                            Numero = rd.randint(2,5)
                            try:
                                Cantidad = Inventario[Loot_enemigos[Actualenemigo]] + Numero
                                Inventario[Loot_enemigos[Actualenemigo]] = Cantidad
                            except KeyError:
                                Inventario[Loot_enemigos[Actualenemigo]] = Numero
                            print(f"Has conseguido {Numero} {Loot_enemigos[Actualenemigo]}"); pelea = False
                            tm.sleep(2)
                        if Vida_usuario <= 0:
                            print("Has caído ante el enemigo! ... ..")
                            print("Has podido huir..."); pelea = False
                            tm.sleep(2)
                else:
                    print("Has huido!"); pelea = False
        if respuesta == "descansar":
            print("Te has ido a dormir... ZZZzzz .. zz")
            exit()

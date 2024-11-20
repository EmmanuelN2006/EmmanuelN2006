import numpy as np
import random as rd
import time as tm

print("Hola! ¿Qué quieres hacer?"); print("Ajedrez / Fantasía") ##El fantasía es otra modalidad que mostrare en otro proyecto
Modo = input("= ").lower()

if Modo == "ajedrez":
    ###Modalidad de ajedrez###
    print("Vamos a jugar ajedrez!")
    Fichasb_Posicion = {"Torre1":1, "Torre2":8, "Caballo1":2, "Caballo2":7, "Alfil1":3, "Alfil2":6, "Reina":4, "Rey":5} #Recordatorio
    Peonesb_Posicion = {"Peón1":10, "Peón2":11, "Peón3":12, "Peón4":13, "Peón5":14, "Peón6":15, "Peón7":16, "Peón8":17}
    Fichasn_Posicion = {"Torre1":20, "Torre2":27, "Caballo1":21, "Caballo2":26, "Alfil1":22, "Alfil2":25, "Reina":24, "Rey":23} #Recordatorio
    Peonesn_Posicion = {"Peón1":70, "Peón2":71, "Peón3":72, "Peón4":73, "Peón5":74, "Peón6":75, "Peón7":76, "Peón8":77}    
    Fichas = ["Torre1", "Caballo1", "Alfil1", "Reina", "Rey", "Alfil2", "Caballo2", "Torre2", "Peón1", "Peón2", "Peón3", "Peón4", "Peón5", "Peón6", "Peón7", "Peón8"]
    Fichasq = ["Torre", "Caballo", "Alfil", "Reina", "Rey", "Peón"] #Función preguntas
    Colores = ["Blanco", "Negro"]
    Dimensiones_tabla = [8, 8] #Tamaño de la tabla
    ## Establecer la tabla y jugador ##
    print("¿Qué equipo quieres ser?"); print("Blanco o Negro?")
    respuesta = False
    while not respuesta:
        Equipo = input("= ").lower()
        if Equipo == "blanco": 
            respuesta = True   
            continue  
        if Equipo == "negro":
            respuesta = True
            continue
        else:
            print("Respuesta no válida")
    ### Jugador establecido = Blanco y empieza el juego ###
    if Equipo == "blanco":
        Tablero = np.zeros(Dimensiones_tabla)
        print(f"Tus fichas son {Fichas}") #Mostrará las fichas que tengamos
        ##Fichas blancas
        for i in range(1): #Fila 1 de la tabla - Fichas principales
            for j in range(8): #Columna de la tabla
                Tablero[i,j] = Fichasb_Posicion[Fichas[j]]

        for i in range(1, 2, 1): #Fila 2 de la tabla - Peones
            for j in range(8): #Columna de la tabla
                Tablero[i, j] = 10 + j
        ###Fichas negras
        for i in range(7, 8, 1): #Fila 1 de la tabla - Fichas principales
            for j in range(8): #Columna de la tabla
                Tablero[i,j] = Fichasn_Posicion[Fichas[j]]

        for i in range(6, 7, 1): #Fila 2 de la tabla - Peones
            for j in range(8): #Columna de la tabla
                Tablero[i, j] = 70 + j

        while Equipo == "blanco":
            print(" [ 0   1   2   3   4   5   6   7  ] posición i")
            print(Tablero)
            print("¿Quieres buscar, mover o conocer una ficha, o rendirte?")
            respuesta = input("= ").lower()
            if respuesta == "buscar":
                print(f"¿Qué ficha necesitas buscar? {Fichas}")
                ficha = input("= ")
                for i in range(0, 2, 1): #Columnas
                    for j in range(8): #Filas
                        try:
                            if Tablero[i,j] == Fichasb_Posicion[ficha]:
                                print(f"La ficha {ficha} está en la posición {i,j}")
                        except KeyError:
                            if Tablero[i,j] == Peonesb_Posicion[ficha]:
                                print(f"La ficha {ficha} está en la posición {i,j}")
            elif respuesta == "mover":
                print(f"¿Cuál ficha quieres mover? {Fichas}")
                answer_info = input("= ")
                ficha = answer_info
                for i in range(0, 2, 1): #Columnas
                    for j in range(8): #Filas
                        try:
                            if Tablero[i,j] == Fichasb_Posicion[ficha]:
                                Tablero[i,j] = 0
                        except KeyError:
                            if Tablero[i,j] == Peonesb_Posicion[ficha]:
                                Tablero[i,j] = 0
                print("¿Dondé la quieres mover? [Columna, Fila]")
                columna = int(input("= ")); fila = int(input("= "))
                try:
                    Tablero[columna,fila] = Fichasb_Posicion[ficha]
                except KeyError:
                    Tablero[columna,fila] = Peonesb_Posicion[ficha]
            elif respuesta == "conocer":
                print(f"¿Sobre qué ficha quieres saber información? {Fichasq}")
                answer_info = input("=").lower()
                if answer_info == "peón":
                    print("Pieza sencilla que al principio se mueve dos casillas, luego se mueve una y mata en diagonal")
                elif answer_info == "torre":
                    print("Pieza que se desplaza de forma vertical u horizontal donde quiera, fichas en su camino perecen")
                elif answer_info == "caballo":
                    print("Pieza que se desplaza en forma de L, siendo 3 cuadros a los lados y luego 1 hacia la izquierda o derecha, donde cae es donde mata")
                elif answer_info == "alfil":
                    print("Pieza parecido a la torre, pero que se desplaza de forma diagonal")
                elif answer_info == "reina":
                    print("Pieza que tiene el movimiento de una torre y alfil juntos, es la más completa de las fichas")
                elif answer_info == "rey":
                    print("Pieza fundamental, se mueve un bloque hacia todos lados, si este muere, pierdes")
                else:
                    print("Esa ficha no existe")
            elif respuesta == "rendirse":
                exit()
            else:
                print("Respuesta no válida")
    ### Jugador establecido = Negro y empieza el juego ##
    if Equipo == "negro":
        Tablero = np.zeros(Dimensiones_tabla)
        print(f"Tus fichas son {Fichas}") #Mostrará las fichas que tengamos
        ##Fichas blancas
        for i in range(1): #Fila 1 de la tabla - Fichas principales
            for j in range(8): #Columna de la tabla
                Tablero[i,j] = Fichasb_Posicion[Fichas[j]]

        for i in range(1, 2, 1): #Fila 2 de la tabla - Peones
            for j in range(8): #Columna de la tabla
                Tablero[i, j] = 10 + j
        ###Fichas negras
        for i in range(7, 8, 1): #Fila 1 de la tabla - Fichas principales
            for j in range(8): #Columna de la tabla
                Tablero[i,j] = Fichasn_Posicion[Fichas[j]]

        for i in range(6, 7, 1): #Fila 2 de la tabla - Peones
            for j in range(8): #Columna de la tabla
                Tablero[i, j] = 70 + j

        while Equipo == "negro":
            print(" [ 0   1   2   3   4   5   6   7  ] posición i")
            print(Tablero)
            print("¿Quieres buscar, mover o conocer una ficha, o rendirte?")
            respuesta = input("= ").lower()
            if respuesta == "buscar":
                print(f"¿Qué ficha necesitas buscar? {Fichas}")
                ficha = input("= ")
                for i in range(6, 7, 1): #Columnas
                    for j in range(8): #Filas
                        try:
                            if Tablero[i,j] == Fichasn_Posicion[ficha]:
                                print(f"La ficha {ficha} está en la posición {i,j}")
                        except KeyError:
                            if Tablero[i,j] == Peonesn_Posicion[ficha]:
                                print(f"La ficha {ficha} está en la posición {i,j}")
            elif respuesta == "mover":
                print(f"¿Cuál ficha quieres mover? {Fichas}")
                answer_info = input("= ")
                ficha = answer_info
                for i in range(6, 8, 1): #Columnas
                    for j in range(8): #Filas
                        try: 
                            if Tablero[i,j] == Fichasn_Posicion[ficha]:
                                Tablero[i,j] = 0
                        except KeyError:
                            if Tablero[i,j] == Peonesn_Posicion[ficha]:
                                Tablero[i,j] = 0
                print("¿Dondé la quieres mover? [Columna, Fila]")
                columna = int(input("= ")); fila = int(input("= "))
                try:
                    Tablero[columna,fila] = Fichasn_Posicion[ficha]
                except KeyError:
                    Tablero[columna,fila] = Peonesn_Posicion[ficha]
            elif respuesta == "conocer":
                print(f"¿Sobre qué ficha quieres saber información? {Fichasq}")
                answer_info = input("=").lower()
                if answer_info == "peón":
                    print("Pieza sencilla que al principio se mueve dos casillas, luego se mueve una y mata en diagonal")
                elif answer_info == "torre":
                    print("Pieza que se desplaza de forma vertical u horizontal donde quiera, fichas en su camino perecen")
                elif answer_info == "caballo":
                    print("Pieza que se desplaza en forma de L, siendo 3 cuadros a los lados y luego 1 hacia la izquierda o derecha, donde cae es donde mata")
                elif answer_info == "alfil":
                    print("Pieza parecido a la torre, pero que se desplaza de forma diagonal")
                elif answer_info == "reina":
                    print("Pieza que tiene el movimiento de una torre y alfil juntos, es la más completa de las fichas")
                elif answer_info == "rey":
                    print("Pieza fundamental, se mueve un bloque hacia todos lados, si este muere, pierdes")
                else:
                    print("Esa ficha no existe")
            elif respuesta == "rendirse":
                exit()
            else:
                print("Respuesta no válida")

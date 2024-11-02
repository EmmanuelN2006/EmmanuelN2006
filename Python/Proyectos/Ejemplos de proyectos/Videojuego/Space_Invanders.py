#Videojuego space invaders en python con mecánicas de aleatoriedad y uso de las matrices

#Objetivos del proyecto
#1. Establecer la idea principal - Hecho: Videojuego
#2. Dar un enfoque especial al proyecto para que no parezca una simple copia - 
#3. Conocer las librerías que se planean utilizar para el desarrollo del mismo -
#4. Empezar con la estructura básica... -
    #La estructura básica para hacer el juego es:
    #El boceto inicial del juego y sus sprites -
    #Los sprites del juego -
    #Los scripts del juego -
    #La interfaz del juego -
    #La jugabilidad del juego -
    #La música del juego -
#5. Planeación de la exposición del juego -

#Librerías
import numpy as np
import math as mt
import pygame as py

#Definir la pantalla del juego principal - Pero hay que hacer un bucle para que se inicie y se termine
# def Pantalla(Jugando):  
#     while Jugando == True:
#         py.init() #Inicia la configuración del juego - Es como el comando ventana.mainloop() pero que se pone al principio
#         Ventana_principal = py.display.set_mode((720, 480)) #Establece el tamaño de la pantalla
#         Ventana_principal.fill(BLANCO)
#         py.display.set_caption("Videojuego") #Establece el nombre de la ventana
#         #####Cierre de la ventana####
#         for event in py.event.get(): #Comando fundamental para que funcione el botón cerrar
#             if event.type == py.QUIT: #Establece que si el comando evento sea salir, procede a decir que jugar es falso
#                 Jugando = False #Jugar se vuelve falso y se acaba el bucle 

#Itera hasta que el usuario pincha sobre el botón de cierre.
Instrucciones = bool; Instrucciones = True
Jugar = bool; Jugar = True
Jugando = bool; Jugando = True
Finalizar = bool; Finalizar = False #Saber si el usuario está jugando, va a jugar, quiere ver instrucciones..
BLANCO = (0xFF, 0xFF, 0xFF)
print("Variables cargadas") ##Validación 1##

###Boceto preferible###
print("Juego iniciado")
py.init() #Inicia la configuración del juego - Es como el comando ventana.mainloop() pero que se pone al principio
#Configuración de la pantalla#
Ventana_principal = py.display.set_mode((720, 480)) #Establece el tamaño de la pantalla
py.display.set_caption("Videojuego") #Establece el nombre de la ventana
print("Configuración de ventana cargada") ##Validación 2##
#Configuración del cierre de la pantalla#

#Configuración del jugador#
Sprite_jugador = py.image.load('Proyecto de estructuras - Videojuego\Personaje_ejemplo.png') #La dirección del archivo se pone usando la ruta de acceso relativa
print("Imagen cargada") #Validación 3#
Posicion_jugador = [320, 240]
Velocidad_jugador = [3, 3] #Límites de velocidad
Desplazamiento_jugador = Sprite_jugador.get_rect() #Hace que exista una linea imaginaria para el movimiento

# Se usa para gestionar cuan rápido se actualiza la pantalla
reloj = py.time.Clock()
print("Fps cargados") ##Validación 4##

########## -------- Bucle Principal del Programa - Partes esenciales -----------#########
while not Finalizar:
##### Eventos que incluyan acciones de condiciones y/o correciones, debajo de acá ######
    for evento in py.event.get(): # El usuario hizo algo
        if evento.type == py.QUIT: # Si el usuario pincha sobre cerrar
            Finalizar = True # Esto que indica que hemos acabado y sale de este bucle
            print("Cierre cargado") ##Validación 5##
    ##### Eventos que incluyan acciones de condiciones y/o correciones, arriba de acá ######
    
    #### Todas las mecánicas del juego deben ir debajo del comentario ####
    Desplazamiento_jugador = Desplazamiento_jugador.move(Velocidad_jugador)
    if Desplazamiento_jugador.left < 0 or Desplazamiento_jugador.right > 640: #Ancho
        Velocidad_jugador[0] = -Velocidad_jugador[0] #Movimiento de izquierda a derecha
    if Desplazamiento_jugador.top < 0 or Desplazamiento_jugador.bottom > 480: #Altura
        Velocidad_jugador[1] = -Velocidad_jugador[1] #Movimiento de arriba a abajo
    #### Todas las mecánicas del juego deben ir encima del comentario ####
    
    
    ### Todo el código de sprites, dibujos y música deben ir debajo del comentario ###
    #Configuración de la ventana
    Ventana_principal.fill(BLANCO) #Color de fondo
    Ventana_principal.blit(Sprite_jugador, Desplazamiento_jugador) #Imagen de los objetos
    py.display.flip()
    print("Ventana actualizada") #Validación 6#

    ### Todo el código de sprites, dibujos y música deben ir encima del comentario ###
    
    ### Limita a 60 fotogramas por segundo (Imágenes cargadas y pasadas por segundo) ###
    reloj.tick(60)
    print("60 Fps corriendo") ##Validación 7##
########################################################################################
py.quit() #Si no hay otra acción a realizar - Cerrar el juego
print("Se cerró el juego") 
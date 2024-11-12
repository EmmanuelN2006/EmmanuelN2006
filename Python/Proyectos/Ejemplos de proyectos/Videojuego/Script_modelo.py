#Código del videojuego: https://github.com/EmmanuelN2006/EmmanuelN2006/tree/main/Python/Proyectos/Ejemplos%20de%20proyectos/Videojuego
import pygame #pip install pygame
import random #pip install random

pygame.init() #Inicia la configuración del videojuego

Finalizar = False #Condición para cerrarlo

#Configuración de la pantalla
BLANCO = (0xFF, 0xFF, 0xFF)
Dimensiones = [720,480]
Ventana_principal = pygame.display.set_mode(Dimensiones); pygame.display.set_caption("Proyecto - Videojuego")
#Configura el tamaño de la ventana y el nombre de la ventana

#Configuración del jugador
Imagen_jugador = pygame.image.load('Proyecto de estructuras - Videojuego\Personaje_ejemplo2.png')
#Imagen_velozjugador = pygame.image.load('Proyecto de estructuras - Videojuego\Personaje_ejemplo.png') - Animación de acelerar
#Imagen_jugador = pygame.image.load('Proyecto de estructuras - Videojuego\Personaje_ejemplo.png') si quiere usar otra imagen
#Recordar que la imagen debe estar dentro del area de trabajo y deben dar click derecho encima de la imagen y darle a
#'Copia de ruta de acceso relativo
x = 720/2; y = 480/2; Posicion_jugador = [x,y] #Posición inicial del jugador
Velocidad_jugadorx = float; Velocidad_jugadorx = 1.7 #Velocidad en x
Velocidad_jugadory = float; Velocidad_jugadory = 1.7 #Velocidad en y

#Configuración de la velocidad y frames
reloj = pygame.time.Clock() #Importante en la actualización de imágenes

##Bucle##
while not Finalizar:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: #Cierra el juego cuando se usa el cerrar ventana
            Finalizar = True
            print("Se cerró el juego") 
            pygame.quit()
    ### Cierre alternativo ###
    Tecla_presionada = pygame.key.get_pressed()
    if Tecla_presionada[pygame.K_ESCAPE]: #Cierra el juego cuando le da a la tecla escape
        print("Se cerró el juego") 
        exit()
    ### Comprobación de situaciones ###
    ##Cuando el jugador se está moviendo o quiere moverse ###
    else: # Cuando no quiere correr #
        if Tecla_presionada[pygame.K_g]: #Centra al jugador si es que se pierde
            print("Centrando jugador")
            Centro = 360; Centro2 = 240
            x = Centro; y = Centro2
            Posicion_jugador = [x, y]
        ###Configuración con controles duales flecha arriba-izquierda ejemplo
        if Tecla_presionada[pygame.K_UP] and Tecla_presionada[pygame.K_RIGHT]: #Diagonal arriba derecha
            Derecha = x + 1.5
            x = Derecha
            Arriba = y - 1.5
            y = Arriba
            Posicion_jugador = [x, y]
        if Tecla_presionada[pygame.K_UP] and Tecla_presionada[pygame.K_LEFT]: #Diagonal arriba izquierda
            Izquierda = x - 1.5
            x = Izquierda
            Arriba = y - 1.5
            y = Arriba
            Posicion_jugador = [x, y] 
        if Tecla_presionada[pygame.K_DOWN] and Tecla_presionada[pygame.K_RIGHT]: #Diagonal abajo derecha
            Derecha = x + 1.5
            x = Derecha
            Abajo = y + 1.5
            y = Abajo
            Posicion_jugador = [x, y]
        if Tecla_presionada[pygame.K_DOWN] and Tecla_presionada[pygame.K_LEFT]: #Diagonal abajo izquierda
            Izquierda = x - 2
            x = Izquierda
            Abajo = y + 2
            y = Abajo
            Posicion_jugador = [x, y]
        ###Configuración con controles duales flecha W-A ejemplo
        if Tecla_presionada[pygame.K_w] and Tecla_presionada[pygame.K_d]: #Diagonal arriba derecha
            Arriba = y - 1.5
            y = Arriba
            Derecha = x + 1.5
            x = Derecha
            Posicion_jugador = [x, y]
        if Tecla_presionada[pygame.K_w] and Tecla_presionada[pygame.K_a]: #Diagonal arriba izquierda
            Arriba = y - 1.5
            y = Arriba
            Izquierda = x - 1.5
            x = Izquierda
            Posicion_jugador = [x, y] 
        if Tecla_presionada[pygame.K_s] and Tecla_presionada[pygame.K_d]: #Diagonal abajo derecha
            Abajo = y + 1.5
            y = Abajo
            Derecha = x + 1.5
            x = Derecha
            Posicion_jugador = [x, y]
        if Tecla_presionada[pygame.K_s] and Tecla_presionada[pygame.K_a]: #Diagonal abajo izquierda
            Abajo = y + 2
            y = Abajo
            Izquierda = x - 2
            x = Izquierda
            Posicion_jugador = [x, y]
        ##Configuración de controles con flechas
        elif Tecla_presionada[pygame.K_UP]:
            Arriba = y - 2
            y = Arriba #Obliga a la variable y a ser igual al valor de Arriba
            Posicion_jugador = [x, y]
            # print(y)
        elif Tecla_presionada[pygame.K_LEFT]:
            Izquierda = x - 2
            x = Izquierda #Obliga a la variable x a hacer igual de Izquierda
            Posicion_jugador = [x, y]
            # print(x)
        elif Tecla_presionada[pygame.K_RIGHT]:
            Derecha = x + 2
            x = Derecha #Obliga a la variable x a hacer igual de Derecha
            Posicion_jugador = [x, y]
            # print(x)
        elif Tecla_presionada[pygame.K_DOWN]:
            Abajo = y + 2
            y = Abajo #Obliga a la variable y a ser igual al valor de Abajo
            Posicion_jugador = [x, y]
            # print(y)
        ###Configuración con controles WSAD
        elif Tecla_presionada[pygame.K_w]:
            Arriba = y - 2
            y = Arriba #Obliga a la variable y a ser igual al valor de Arriba
            Posicion_jugador = [x, y]
            # print(y)
        elif Tecla_presionada[pygame.K_a]:
            Izquierda = x - 2
            x = Izquierda #Obliga a la variable x a hacer igual de Izquierda
            Posicion_jugador = [x, y]
            # print(x)
        elif Tecla_presionada[pygame.K_d]:
            Derecha = x + 2
            x = Derecha #Obliga a la variable x a hacer igual de Derecha
            Posicion_jugador = [x, y]
            # print(x)
        elif Tecla_presionada[pygame.K_s]:
            Abajo = y + 2
            y = Abajo #Obliga a la variable y a ser igual al valor de Abajo
            Posicion_jugador = [x, y]
            # print(y)
    ### Situación de correr ###
    if Tecla_presionada[pygame.K_LSHIFT] or Tecla_presionada[pygame.K_RSHIFT]:  #Opción de correr con el L_Shift o el shift izquierdo 
        Correr = bool; Correr = True
        while Correr == True: #Cuando el shift lo hayan presionado, correra la distancia 1 * 1.7
            if Tecla_presionada[pygame.K_UP]:
                Arriba = y - 2* Velocidad_jugadory #Agrega una variación mayor para tener velocidad
                y = Arriba #Obliga a la variable y a ser igual al valor de Arriba
                Posicion_jugador = [x, y]
                # print(y)
            elif Tecla_presionada[pygame.K_LEFT]:
                Izquierda = x - 2* Velocidad_jugadorx #Agrega una variación mayor para tener velocidad
                x = Izquierda #Obliga a la variable x a hacer igual de Izquierda
                Posicion_jugador = [x, y]
                # print(x)
            elif Tecla_presionada[pygame.K_RIGHT]:
                Derecha = x + 2* Velocidad_jugadorx #Agrega una variación mayor para tener velocidad
                x = Derecha #Obliga a la variable x a hacer igual de Derecha
                Posicion_jugador = [x, y]
                # print(x)
            elif Tecla_presionada[pygame.K_DOWN]:
                Abajo = y + 2* Velocidad_jugadory #Agrega una variación mayor para tener velocidad
                y = Abajo #Obliga a la variable y a ser igual al valor de Abajo
                Posicion_jugador = [x, y]
                # print(y)
            if Tecla_presionada[pygame.K_w]:
                Arriba = y - 2* Velocidad_jugadory #Agrega una variación mayor para tener velocidad
                y = Arriba #Obliga a la variable y a ser igual al valor de Arriba
                Posicion_jugador = [x, y]
                # print(y)
            elif Tecla_presionada[pygame.K_a]:
                Izquierda = x - 2* Velocidad_jugadorx #Agrega una variación mayor para tener velocidad
                x = Izquierda #Obliga a la variable x a hacer igual de Izquierda
                Posicion_jugador = [x, y]
                # print(x)
            elif Tecla_presionada[pygame.K_d]:
                Derecha = x + 2* Velocidad_jugadorx #Agrega una variación mayor para tener velocidad
                x = Derecha #Obliga a la variable x a hacer igual de Derecha
                Posicion_jugador = [x, y]
                # print(x)
            elif Tecla_presionada[pygame.K_s]:
                Abajo = y + 2* Velocidad_jugadory #Agrega una variación mayor para tener velocidad
                y = Abajo #Obliga a la variable y a ser igual al valor de Abajo
                Posicion_jugador = [x, y]
                # print(y)
            if Tecla_presionada[pygame.K_LSHIFT] or Tecla_presionada[pygame.K_RSHIFT]: #Cuando se deja de presionar el shift izquierdo, el L-shift
                Correr = False
    ##### Eventos que incluyan acciones de condiciones y/o correciones, arriba de acá ######

    #Configuración de la ventana
    Ventana_principal.fill(BLANCO) #Color de fondo
    Ventana_principal.blit(Imagen_jugador, Posicion_jugador) #Imagen del objeto y su posicion para siempre
    pygame.display.flip()
    # print("Ventana actualizada") #Validación 6#
    ### Todo el código de sprites, dibujos y música deben ir encima del comentario ###
    
    ### Limita a 60 fotogramas por segundo (Imágenes cargadas y pasadas por segundo) ###
    reloj.tick(60)
    # print("60 Fps corriendo") ##Validación 7##
########################################################################################
pygame.quit() #Si no hay otra acción a realizar - Cerrar el juego
print("Se cerró el juego") 

#Objetivos del proyecto
#1. Establecer la idea principal - Hecho: Videojuego
#2. Dar un enfoque especial al proyecto para que no parezca una simple copia - 
#3. Conocer las librerías que se planean utilizar para el desarrollo del mismo -
#4. Empezar con la estructura básica... -
    #La estructura básica para hacer el juego es:
    #El boceto inicial del juego y sus sprites - Hecho
    #Movimiento del jugador - Hecho
    #Los sprites del juego -
    #Los scripts del juego - Hecho
    #La interfaz del juego -
    #La jugabilidad del juego -
    #La música del juego -
#5. Planeación de la exposición del juego -

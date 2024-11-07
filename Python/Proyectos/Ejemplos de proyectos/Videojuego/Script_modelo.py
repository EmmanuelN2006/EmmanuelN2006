#Código del videojuego: https://github.com/EmmanuelN2006/EmmanuelN2006/tree/main/Python/Proyectos/Ejemplos%20de%20proyectos/Videojuego
import pygame
import random 

pygame.init()

Finalizar = False

#Configuración de la pantalla
BLANCO = (0xFF, 0xFF, 0xFF)
Dimensiones = [720,480]
Ventana_principal = pygame.display.set_mode(Dimensiones); pygame.display.set_caption("Proyecto - Videojuego")

#Configuración del jugador
Imagen_jugador = pygame.image.load('Proyecto de estructuras - Videojuego\Personaje_ejemplo2.png')
#Imagen_jugador = pygame.image.load('Proyecto de estructuras - Videojuego\Personaje_ejemplo.png') si quiere usar otra imagen
#Recordar que la imagen debe estar dentro del area de trabajo y deben dar click derecho encima de la imagen y darle a
#'Copia de ruta de acceso relativo
x = 720/2; y = 480/2; Posicion_jugador = [x,y]
Velocidad_jugadorx = float; Velocidad_jugadorx = 1.7
Velocidad_jugadory = float; Velocidad_jugadory = 1.7

#Configuración de la velocidad y frames
reloj = pygame.time.Clock()

##Bucle##
while not Finalizar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            Finalizar = True
            print("Se cerró el juego") 
            pygame.quit()
    ###
    Tecla_presionada = pygame.key.get_pressed()
    if Tecla_presionada[pygame.K_ESCAPE]:
        print("Se cerró el juego") 
        exit()
    ### Comprobación de situaciones ##
    if Tecla_presionada[pygame.K_LSHIFT]:  #Opción de correr con el L_Shift o el shift izquierdo 
        Correr = bool; Correr = True
        while Correr == True: #Cuando el shift lo hayan presionado, correra la distancia 1 * 1.7
            if Tecla_presionada[pygame.K_UP]:
                Arriba = y - 1* Velocidad_jugadory #Agrega una variación mayor para tener velocidad
                y = Arriba #Obliga a la variable y a ser igual al valor de Arriba
                Posicion_jugador = [x, y]
                # print(y)
            elif Tecla_presionada[pygame.K_LEFT]:
                Izquierda = x - 1* Velocidad_jugadorx #Agrega una variación mayor para tener velocidad
                x = Izquierda #Obliga a la variable x a hacer igual de Izquierda
                Posicion_jugador = [Izquierda, y]
                # print(x)
            elif Tecla_presionada[pygame.K_RIGHT]:
                Derecha = x + 1* Velocidad_jugadorx #Agrega una variación mayor para tener velocidad
                x = Derecha #Obliga a la variable x a hacer igual de Derecha
                Posicion_jugador = [Derecha, y]
                # print(x)
            elif Tecla_presionada[pygame.K_DOWN]:
                Abajo = y + 1* Velocidad_jugadory #Agrega una variación mayor para tener velocidad
                y = Abajo #Obliga a la variable y a ser igual al valor de Abajo
                Posicion_jugador = [x, Abajo]
                # print(y)
            if Tecla_presionada[pygame.K_LSHIFT]: #Cuando se deja de presionar el shift izquierdo, el L-shift
                Correr = False
    else: #Cuando no quiere correr
        if Tecla_presionada[pygame.K_UP]:
            Arriba = y - 1
            y = Arriba #Obliga a la variable y a ser igual al valor de Arriba
            Posicion_jugador = [x, y]
            # print(y)
        elif Tecla_presionada[pygame.K_LEFT]:
            Izquierda = x - 1
            x = Izquierda #Obliga a la variable x a hacer igual de Izquierda
            Posicion_jugador = [Izquierda, y]
            # print(x)
        elif Tecla_presionada[pygame.K_RIGHT]:
            Derecha = x + 1
            x = Derecha #Obliga a la variable x a hacer igual de Derecha
            Posicion_jugador = [Derecha, y]
            # print(x)
        elif Tecla_presionada[pygame.K_DOWN]:
            Abajo = y + 1
            y = Abajo #Obliga a la variable y a ser igual al valor de Abajo
            Posicion_jugador = [x, Abajo]
            # print(y)
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

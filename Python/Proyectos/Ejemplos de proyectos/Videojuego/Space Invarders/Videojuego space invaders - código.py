#Código del videojuego: https://github.com/EmmanuelN2006/EmmanuelN2006/blob/main/Python/Proyectos/Ejemplos%20de%20proyectos/Videojuego/Space%20Invarders/Videojuego%20space%20invaders%20-%20c%C3%B3digo.py
#Deben usar la carpeta del proyecto como área de trabajo

import pygame #pip install pygame
import random #pip install random
import time #Viene pre-isntalado pero se instala con pip install time
from pygame import mixer
print("Cargando juego") #Indica que el juego se pondrá a cargar si no hay errores posteriores

pygame.init() #Inicia la configuración del videojuego

#Configuración de la pantalla
Colorfondo = (35,50,25) #Por ahora el fondo que incluirá la pantalla
Dimensiones = [720,480] #Ancho / Alto
Ventana_principal = pygame.display.set_mode(Dimensiones); pygame.display.set_caption("Proyecto - Space Invaders")
#Configura el tamaño de la ventana y el nombre de la ventana

#Configuración del texto como puntuación, vidas, etc...
Vidas = 3 #Vidas totales que debe haber
Puntuacion = 0 #Puntuación que se va a ganar durante el combate contra los enemigos
Vidas_png = {
    1:pygame.image.load('Enemigos/Vidas.png'),
    2:pygame.image.load('Enemigos/Vidas.png'),
    3:pygame.image.load('Enemigos/Vidas.png')}
Vida1 = Vidas_png[1]; Vida2 = Vidas_png[2]; Vida3 = Vidas_png[3]
Pos1 = [680, 30]; Pos2 = [680, 20]; Pos3 = [680, 10]

def mostrar_puntuacion(): #Muestra y desarrollla la puntuación que saldrá
    """Muestra la puntuación en pantalla."""
    fuente = pygame.font.Font(None, 24) #Establece un texto con una fuente predeterminada en tamaño 24 de letra
    texto = fuente.render(f"Puntuación: {Puntuacion}", True, (255, 255, 255)) #Renderiza el texto que se escribirá con la fuente y su posición y si se debe mostrar
    Ventana_principal.blit(texto, (10, 10)) #Lo carga dentro de la imagen

def mostrar_vidas(Vidas): #Define cuales son las vidas que le falta al jugador antes de perder
    if Vidas == 3:
        Ventana_principal.blit(Vida3, Pos3)
    if Vidas == 2:
        Ventana_principal.blit(Vida2, Pos2)
    if Vidas == 1:
        Ventana_principal.blit(Vida1, Pos1)
    if Vidas <= 0:
        Finalizar = True

#Configuración del jugador
Frames_jugador = {
    1:pygame.image.load('Nave/Nave_estatica.png'), #Nave cuando no se mueve a la izquierda ni derecha 
    2:pygame.image.load('Nave/Nave_acelerando.png'), #Nave cuando no se mueve a la izquierda ni derecha y acelerando
    3:pygame.image.load('Nave/Nave_girandoizq.png'), #Nave cuando se mueve a la derecha
    4:pygame.image.load('Nave/Nave_girandoizq_veloz.png'), #Nave cuando se mueve a la derecha acelerando
    5:pygame.image.load('Nave/Nave_girandoder.png'), #Nave cuando se mueve a la izquierda
    6:pygame.image.load('Nave/Nave_girandoder_veloz.png')} #Nave cuando se mueve a la izquierda acelerando
Imagen_jugador = Frames_jugador[1] #Imagen inicial
#Copia de ruta de acceso relativo, deben usar la carpeta del proyecto como area de trabajo
x = 720/2; y = 480/2; Posicion_jugador = [x,y] #Posición inicial del jugador

#Configuración de la bala
Frames_disparo = {
    1:pygame.image.load('Disparo/Disparo1.png'), #Frame 1 del disparo
    2:pygame.image.load('Disparo/Disparo2.png'), #Frame 2 del disparo
    3:pygame.image.load('Disparo/Disparo3.png')} #Frame final del disparo
Disparo = Frames_disparo[1]; #Imagen inicial con posición fuera de la ventana visible
Disparos_activos = [] #Muestra cuáles son los disparos que se encuentran en el juego

#Configuración de los enemigos
Enemigos_posibles = {
    1:pygame.image.load('Enemigos/Enemigo1.png'), #Sprite 1 de un posible enemigo
    2:pygame.image.load('Enemigos/Enemigo2.png')} #Sprite 2 de un posible enemigo
Enemigos = [] #Muestra los enemigos actuales en el juego
Enemigos2 = [] #Muestra los enemigos tipo 2 actuales en el juego
Enemigos_muertos = [] #Clasifica los enemigos muertos

#Configuración de las muertes
Muerte = pygame.image.load('Enemigos/Muerte.png') #Imagen de muerte

#Condicionales para el juego
Choque = False #Cuando el jugador este en las limitaciones de la ventana
Daño = False #Cuando el jugador toque al enemigo o elementos del enemigo
Finalizar = False #Condición para cerrarlo

#Funciones para el funcionamiento del juego
def mover_jugador(Tecla_presionada, pos):
    Imagen = Frames_jugador[1]
    velocidad_actual = 5 * (1.2 if Tecla_presionada[pygame.K_LSHIFT] or Tecla_presionada[pygame.K_RSHIFT] else 1)

    if Tecla_presionada[pygame.K_UP] or Tecla_presionada[pygame.K_w]:
        pos[1] -= velocidad_actual
        Imagen = Frames_jugador[2]

    if Tecla_presionada[pygame.K_DOWN] or Tecla_presionada[pygame.K_s]:
        pos[1] += velocidad_actual
        Imagen = Frames_jugador[2]

    if Tecla_presionada[pygame.K_LEFT] or Tecla_presionada[pygame.K_a]:
        pos[0] -= velocidad_actual
        Imagen = Frames_jugador[5] if velocidad_actual == 5 else Frames_jugador[6]

    if Tecla_presionada[pygame.K_RIGHT] or Tecla_presionada[pygame.K_d]:
        pos[0] += velocidad_actual
        Imagen = Frames_jugador[3] if velocidad_actual == 5 else Frames_jugador[4]

    #Evita que la nave se salga de la pantalla o vista del jugador
    pos[0] = max(0, min(Dimensiones[0] - Imagen.get_width(), pos[0])) #Verificar en Ancho
    pos[1] = max(0, min(Dimensiones[1] - Imagen.get_height(), pos[1])) #Verificar en Alto
    return Imagen

def generar_enemigos():
    """Genera enemigos en posiciones aleatorias en la parte superior."""
    if len(Enemigos) < 6:  # Máximo 6 enemigos en pantalla
        x = random.randint(0, Dimensiones[0] - 50) #Elige un x aleatorio
        Enemigos.append([x, -50])  # Añade el enemigo fuera de la pantalla

def mover_enemigos():
    """Mueve enemigos hacia abajo y los elimina si salen de pantalla."""
    for enemigo in Enemigos[:]:
        enemigo[1] += 3  # Velocidad de movimiento
        if enemigo[1] > Dimensiones[1]:  # Si el enemigo pasa el límite
            Enemigos.remove(enemigo)

def generar_enemigos2():
    if len(Enemigos2) < 3:  # Máximo 3 enemigos en pantalla
        y = random.randint(0, Dimensiones[1] - 50)
        Enemigos2.append([-50, y])  # Añade el enemigo fuera de la pantalla

def mover_enemigos2():
    for enemigo2 in Enemigos2[:]:
        enemigo2[0] += 5 #Velocidad del enemigo
        if enemigo2[0] > Dimensiones[0]:
            Enemigos2.remove(enemigo2)

# Contador para animar disparos
Frame_disparo_actual = 1

def actualizar_disparos():
    """Actualiza la posición y la animación de los disparos."""
    global Puntuacion, Frame_disparo_actual
    Frame_disparo_actual += 1  # Avanza al siguiente frame
    if Frame_disparo_actual > 3:
        Frame_disparo_actual = 1  # Vuelve al primer frame

    for disparo in Disparos_activos[:]:
        disparo[1] -= 10  # Movimiento hacia arriba
        if disparo[1] < 0:
            Disparos_activos.remove(disparo)
        else:
            # Detectar colisión con enemigos con las balas
            for enemigo in Enemigos[:]:
                if enemigo[0] < disparo[0] < enemigo[0] + 50 and enemigo[1] < disparo[1] < enemigo[1] + 50:
                    Ventana_principal.blit(Muerte, enemigo)
                    Enemigos.remove(enemigo)
                    Disparos_activos.remove(disparo)
                    Puntuacion += 5
                    break
            for enemigo2 in Enemigos2[:]:
                if enemigo2[0] < disparo[0] < enemigo2[0] + 50 and enemigo2[1] < disparo[1] < enemigo2[1] + 50:
                    Ventana_principal.blit(Muerte, enemigo2)
                    Enemigos2.remove(enemigo2)
                    Disparos_activos.remove(disparo)
                    Puntuacion += 10
                    break

def animar_muertes():
    """Dibuja y actualiza las animaciones de muerte."""
    for enemigo in Enemigos_muertos[:]:
        Ventana_principal.blit(Muerte, (enemigo[0], enemigo[1]))
        enemigo[2] -= 1
        if enemigo[2] <= 0:  # Elimina animación si el tiempo termina
            Enemigos_muertos.remove(enemigo)

        
#Configuración de la velocidad y frames
reloj = pygame.time.Clock() #Importante en la actualización de imágenes
print("Configuración cargada") #Medidas a tomar

#Preparando la pantalla
Ventana_principal.fill(Colorfondo)
pygame.display.flip() #Actualiza la pantalla del juego
pygame.mixer.music.load('Música/Batallando.mp3') #Carga la música almacenada en las carpetas
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1) #Hace que el juego reproduzca el juego de forma ilimitada

##Bucle##
while not Finalizar:
    Fondo = pygame.image.load('Fondo.jpg')
    Fondo = pygame.transform.scale(Fondo, (800,800))
    for evento in pygame.event.get(): #Cuando el jugador cierra la ventana
        if evento.type == pygame.QUIT: #Cierra el juego cuando se usa el cerrar ventana
            Finalizar = True
            print("Se cerró el juego") 
        if evento.type == pygame.KEYDOWN: #Si alguna tecla es presionada
            if evento.key == pygame.K_SPACE:  #Si la tecla es espacio, dispara
                sonido_disparo = pygame.mixer.Sound("disparo.mp3")
                sonido_disparo.set_volume(0.5)  # Ajusta el volumen
                sonido_disparo.play()
                Disparos_activos.append([Posicion_jugador[0] + 20, Posicion_jugador[1]]) #Agrega un disparo con sus coordenadas respecto al jugador

    ### Cierre alternativo ###
    Tecla_presionada = pygame.key.get_pressed() #Variable del tipo bool
    if Tecla_presionada[pygame.K_ESCAPE]: #Cierra el juego cuando le da a la tecla escape
        print("Se cerró el juego") 
        Finalizar = True

    ### CONFIGURACIÓN DE LOS CONTROLES ###
    if Tecla_presionada[pygame.K_g]: #Centra al jugador si es que se pierde en prueba
        print("Centrando jugador")
        Centro = 360; Centro2 = 240
        x = Centro; y = Centro2
        Posicion_jugador = [x, y]
    Imagen_jugador = mover_jugador(Tecla_presionada, Posicion_jugador) #Ocasiona el movimiento del jugador 

    # Actualizar elementos del juego
    generar_enemigos()
    mover_enemigos()
    generar_enemigos2()
    mover_enemigos2()
    actualizar_disparos()
    
    #Configuración de la ventana y los dibujos
    Ventana_principal.fill(Colorfondo) #Color de fondo de pantalla
    Ventana_principal.blit(Fondo, (0,0))
    Ventana_principal.blit(Imagen_jugador, Posicion_jugador) #Imagen del objeto y su posicion para siempre - elemento en capa mayor

    for disparo in Disparos_activos: #Actualiza cada disparo
        Ventana_principal.blit(Frames_disparo[3], disparo)

    for enemigo in Enemigos: #Actualiza cada enemigo tipo 1
        Ventana_principal.blit(Enemigos_posibles[1], enemigo)
    
    for enemigo2 in Enemigos2: #Actualiza cada enemigo tipo 2
        Ventana_principal.blit(Enemigos_posibles[2], enemigo2) 

    animar_muertes()
    mostrar_puntuacion()
    mostrar_vidas(Vidas)
    pygame.display.flip()
    # print("Ventana actualizada") #Validación 6#
    ### Todo el código de sprites, dibujos y música deben ir encima del comentario ###
    
    ### Limita a 60 fotogramas por segundo (Imágenes cargadas y pasadas por segundo) ###
    reloj.tick(60)
    # print("60 Fps corriendo") ##Validación 7##
########################################################################################
if Finalizar:
    Ventana_principal.fill((0, 0, 0))
    pygame.mixer.music.stop()
    fuente2 = pygame.font.Font(None, 36)
    texto2 = fuente2.render(f"Game Over", True, (255, 255, 255))
    Ventana_principal.blit(texto2, (300, 240))
    pygame.display.flip()  
    time.sleep(3)
pygame.quit() #Si no hay otra acción a realizar - Cerrar el juego
print("Cerrado") 

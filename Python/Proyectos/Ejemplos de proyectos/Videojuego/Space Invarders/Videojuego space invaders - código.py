#Código del videojuego: https://github.com/EmmanuelN2006/EmmanuelN2006/blob/main/Python/Proyectos/Ejemplos%20de%20proyectos/Videojuego/Space%20Invarders/Videojuego%20space%20invaders%20-%20c%C3%B3digo.py
#Deben usar la carpeta del proyecto como área de trabajo

import pygame #pip install pygame
import random #pip install random
import time #Viene pre-isntalado pero se instala con pip install time
from pygame import mixer #pip install mixer - librería incluida en pygame
print("Cargando juego") #Indica que el juego se pondrá a cargar si no hay errores posteriores

pygame.init() #Inicia la configuración del videojuego

#Configuración de la pantalla
Colorfondo = (35,50,25) #Por ahora el fondo que incluirá la pantalla
Dimensiones = [720,480] #Ancho / Alto
Ventana_principal = pygame.display.set_mode(Dimensiones) #Establece el tamaño de la ventana
pygame.display.set_caption("Proyecto - Space Invaders") #Establece el nombre de la ventana al abrirse
Icono = pygame.image.load("Nave_icon.png") #Establece la imagen
pygame.display.set_icon(Icono) #Establece que el icono sea el icono de la ventana
#Configura el tamaño de la ventana y el nombre de la ventana

#Configuración del texto como puntuación, vidas, etc...
Vidas = 3 #Vidas o veces que el jugador puede recibir daño antes de morir
Puntuacion = 0 #Puntuación que se va a ganar durante el combate contra los enemigos
Vidas_png = {
    1:pygame.image.load('Enemigos/Vidas.png')}
Vida1 = Vidas_png[1];  Vida2 = Vidas_png[1]; Vida3 = Vidas_png[1] #Imágenes que usarán las vidas para visualizarse
Pos1 = [680, 30]; Pos2 = [680, 20]; Pos3 = [680, 10] #Posiciones que ocuparan

#Configuración del jugador
Frames_jugador = { #Frames/Sprites del jugador y sus diferentes modos
    1:pygame.image.load('Nave/Nave_estatica.png'), #Nave cuando no se mueve a la izquierda ni derecha 
    2:pygame.image.load('Nave/Nave_acelerando.png'), #Nave cuando no se mueve a la izquierda ni derecha y está acelerando
    3:pygame.image.load('Nave/Nave_girandoizq.png'), #Nave cuando se mueve a la derecha
    4:pygame.image.load('Nave/Nave_girandoizq_veloz.png'), #Nave cuando se mueve a la derecha acelerando
    5:pygame.image.load('Nave/Nave_girandoder.png'), #Nave cuando se mueve a la izquierda
    6:pygame.image.load('Nave/Nave_girandoder_veloz.png')} #Nave cuando se mueve a la izquierda acelerando
Imagen_jugador = Frames_jugador[1] #Imagen inicial
x = 720/2; y = 480/2; Posicion_jugador = [x,y] #Posición inicial del jugador

#Configuración de la bala
Frames_disparo = { #Los diferentes sprites que hay para los disparos
    1:pygame.image.load('Disparo/Disparo1.png'), #Frame 1 del disparo para enemigos 1
    2:pygame.image.load('Disparo/Disparo2.png'), #Frame 2 del disparo para enemigo 2
    3:pygame.image.load('Disparo/Disparo3.png')} #Frame final del disparo para jugador
Disparo = Frames_disparo[1]; #Imagen inicial con posición fuera de la ventana visible
Disparos_activos = [] #Muestra cuáles son los disparos que se encuentran en el juego para el jugador
Disparos_enemigos_activos = [] #Muestra cuáles disparos de enemigos tipo 1 se encuentran activos
Disparos_enemigos_activos2 = [] #Muestra cuáles disparos de enemigos tipo 2 se encuentran activos

#Configuración de los enemigos
Enemigos_posibles = { #Muestra los sprites de los posibles enemigos
    1:pygame.image.load('Enemigos/Enemigo1.png'), #Sprite 1 de un posible enemigo
    2:pygame.image.load('Enemigos/Enemigo2.png')} #Sprite 2 de un posible enemigo
Enemigos = [] #Muestra los enemigos actuales en el juego
Enemigos2 = [] #Muestra los enemigos tipo 2 actuales en el juego
Enemigos_muertos = [] #Clasifica los enemigos muertos

#Configuración de las muertes
Muerte = pygame.image.load('Enemigos/Muerte.png') #Imagen de muerte

#Condicionales para el juego
Finalizar = False #Condición para cerrarlo

#Funciones para el funcionamiento del juego
def mover_jugador(Tecla_presionada, pos): #La función detecta que la tecla haya sido presionada y toma pos como la posición
    Imagen = Frames_jugador[1] #Sprite inicial del jugador cuando no se detecte movimiento
    velocidad_actual = 5 * (1.2 if Tecla_presionada[pygame.K_LSHIFT] or Tecla_presionada[pygame.K_RSHIFT] else 1)
    #Indicará la velocidad que aumentará el movimiento del jugador cuando el shift sea pulsado

    if Tecla_presionada[pygame.K_UP] or Tecla_presionada[pygame.K_w]: #Cuando el jugador quiera subir
        pos[1] -= velocidad_actual #La posición y disminuirá de manera negativa su desplazamiento 
        Imagen = Frames_jugador[2] #Cambia el sprite del jugador por el movimiento

    if Tecla_presionada[pygame.K_DOWN] or Tecla_presionada[pygame.K_s]: #Cuando el jugador quiera bajar
        pos[1] += velocidad_actual #La posición y aumentará de manera positiva su desplazamiento
        Imagen = Frames_jugador[2] #Cambia el sprite del jugador por el movimiento

    if Tecla_presionada[pygame.K_LEFT] or Tecla_presionada[pygame.K_a]:
        pos[0] -= velocidad_actual #La posición x disminuirá de manera negativa su desplazamiento
        Imagen = Frames_jugador[5] if velocidad_actual == 5 else Frames_jugador[6]
        #El sprite de la imagen cambiará dependiendo de la variable velocidad

    if Tecla_presionada[pygame.K_RIGHT] or Tecla_presionada[pygame.K_d]:
        pos[0] += velocidad_actual #La posición y aumentará de manera positiva su desplazamiento
        Imagen = Frames_jugador[3] if velocidad_actual == 5 else Frames_jugador[4]
        #El sprite de la imagen cambiará dependiendo de la variable velocidad

    #Evita que la nave se salga de la pantalla o vista del jugador
    pos[0] = max(0, min(Dimensiones[0] - Imagen.get_width(), pos[0])) #Verifica en que posición está el jugador en x
    pos[1] = max(0, min(Dimensiones[1] - Imagen.get_height(), pos[1])) #Verifica en que posición está el jugador en y
    return Imagen

def generar_enemigos():
    if len(Enemigos) < 6:  # Máximo 6 enemigos en pantalla
        x = random.randint(0, Dimensiones[0] - 50) #Elige un x aleatorio
        Enemigos.append([x, -50])  # Añade el enemigo fuera de la pantalla

def mover_enemigos():
    for enemigo in Enemigos[:]: #Recorre los elementos como enemigo
        enemigo[1] += 2  # Velocidad de movimiento del enemigo
        if enemigo[1] > Dimensiones[1]:  # Si el enemigo pasa el límite
            Enemigos.remove(enemigo) #Remueve el enemigo

def generar_enemigos2():
    if len(Enemigos2) < 3:  # Máximo 3 enemigos en pantalla
        y = random.randint(0, Dimensiones[1] - 200) #Elige un y aleatorio
        Enemigos2.append([-50, y])  # Añade el enemigo fuera de la pantalla

def mover_enemigos2():
    for enemigo2 in Enemigos2[:]: #Recorre los elementos como enemigo2
        enemigo2[0] += 6 #Velocidad del enemigo
        if enemigo2[0] > Dimensiones[0]: # Si el enemigo pasa el límite
            Enemigos2.remove(enemigo2) #Remueve el enemigo

def enemigo_disparo():
    if len(Disparos_enemigos_activos) < 5: #Establece el máximo de disparos posibles
        x = random.randint(0, Dimensiones[0] - 50) #Elige un x aleatorio
        Disparos_enemigos_activos.append([x, -50])  # Añade el disparo del enemigo fuera de la pantalla
    for disparoe in Disparos_enemigos_activos[:]: #Recorre los elementos como disparoe
        disparoe[1] += 4  # Velocidad de movimiento
        if disparoe[1] > Dimensiones[1]:  # Si el enemigo pasa el límite
            Disparos_enemigos_activos.remove(disparoe) #Elimina el disparo

def enemigo_disparo2():
    for enemigo2 in Enemigos2: #Mientras recorre a los enemigos tipo2
        if enemigo2[0] > Posicion_jugador[0] - 50: #Cuando el enemigo detecte que su distancia sea cercana al jugador
            if len(Disparos_enemigos_activos2) < 5: #Creará 5 disparos hacia el jugador desde la posición del enemigo 2
                x = enemigo2[0]; y = enemigo2[1] #Iguala las coordenadas
                Disparos_enemigos_activos2.append([x,y]) #Agrega la configuración del disparo
        for disparoe2 in Disparos_enemigos_activos2: #Recorre los elementos de la lista de los disparos2
            disparoe2[1] += 2 #La velocidad del disparo
            if disparoe2[1] > Dimensiones[1]: #Si el disparo se pasa del límite
                Disparos_enemigos_activos2.remove(disparoe2) #Elimina el disparo

def actualizar_disparos():
    global Puntuacion #Deja que el valor de Puntuacion entre a la función
    for disparo in Disparos_activos[:]: #Recorre las configuraciones de los disparos del jugador
        disparo[1] -= 10  # Movimiento del disparo hacia arriba
        if disparo[1] < 0: #Si la bala supera el límite
            Disparos_activos.remove(disparo) #Es eliminado
        else:
            # Detectar colisión con enemigos con las balas del jugador donde se compara las posiciones 
            for enemigo in Enemigos[:]: #Para enemigos del tipo 1
                if enemigo[0] < disparo[0] < enemigo[0] + 50 and enemigo[1] < disparo[1] < enemigo[1] + 50:
                    Ventana_principal.blit(Muerte, enemigo) #Actualiza el frame del enemigo
                    Enemigos.remove(enemigo) #Elimina al enemigo
                    try: #Intenta eliminar la bala
                        Disparos_activos.remove(disparo)
                    except ValueError:
                        pass
                    Puntuacion += 5 
                    break
            for enemigo2 in Enemigos2[:]: #Para enemigos del tipo 2
                if enemigo2[0] < disparo[0] < enemigo2[0] + 50 and enemigo2[1] < disparo[1] < enemigo2[1] + 50:
                    Ventana_principal.blit(Muerte, enemigo2) #Actualiza el frame del enemigo
                    Enemigos2.remove(enemigo2) #Elimina al enemigo
                    try: #Intenta eleminar la bala
                        Disparos_activos.remove(disparo)
                    except ValueError:
                        pass
                    Puntuacion += 10
                    break
            for disparoe in Disparos_enemigos_activos[:]:
                if disparoe[0] < disparo[0] < disparoe[0] + 50 and disparoe[1] < disparo[1] < disparoe[1] + 50:
                    Disparos_enemigos_activos.remove(disparoe) #Elimina la bala del enemigo 1
                    try: #Intenta eliminar la bala
                        Disparos_activos.remove(disparo) 
                    except ValueError:
                        pass
                    Puntuacion += 2
                    break
            for disparoe2 in Disparos_enemigos_activos2[:]:
                if disparoe2[0] < disparo[0] < disparoe2[0] + 50 and disparoe2[1] < disparo[1] < disparoe2[1] + 50:
                    Disparos_enemigos_activos2.remove(disparoe2) #Elimina la bala del enemigo2
                    try: #Intenta eliminar la bala
                        Disparos_activos.remove(disparo)
                    except ValueError:
                        pass
                    Puntuacion += 20
                    break

def Choque_jugador():
    global Puntuacion #Ingresa el valor de la variable a la función
    global Vidas #Ingresa el valor de la variable a la función
    global Posicion_jugador #Ingresa el valor de la variable a la función
    # Detectar colisión del jugador con los enemigos del entorno
    for enemigo in Enemigos[:]: # Detectar colisión con enemigos con el jugador donde se compara las posiciones
        if enemigo[0] < Posicion_jugador[0] < enemigo[0] + 50 and enemigo[1] < Posicion_jugador[1] < enemigo[1] + 50:
            Ventana_principal.blit(Muerte, enemigo) #Actualiza el frame del enemigo
            Enemigos.remove(enemigo)  #Elimina al enemigo
            Puntuacion -= 5
            Posicion_jugador = [300, 460] #Lleva al jugador a una posición
            break
    for enemigo2 in Enemigos2[:]:
        if enemigo2[0] < Posicion_jugador[0] < enemigo2[0] + 50 and enemigo2[1] < Posicion_jugador[1] < enemigo2[1] + 50:
            Ventana_principal.blit(Muerte, enemigo2) #Actualiza el frame del enemigo
            Enemigos2.remove(enemigo2) #Elimina al enemigo
            Puntuacion -= 10
            Posicion_jugador = [300, 460] #Lleva al jugador a una posición
            break
    for disparoe in Disparos_enemigos_activos[:]:
        if disparoe[0] < Posicion_jugador[0] < disparoe[0] + 50 and disparoe[1] < Posicion_jugador[1] < disparoe[1] + 50:
            Disparos_enemigos_activos.remove(disparoe) #Elimina la bala del enemigo1
            Vidas -= 1
            Posicion_jugador = [300, 460] #Lleva al jugador a una posición
            break
    for disparoe2 in Disparos_enemigos_activos2[:]:
        if disparoe2[0] < Posicion_jugador[0] < disparoe2[0] + 50 and disparoe2[1] < Posicion_jugador[1] < disparoe2[1] + 50:
            Disparos_enemigos_activos2.remove(disparoe2) #Elimina la bala del enemigo2
            Vidas -= 1
            Posicion_jugador = [300, 460] #Lleva al jugador a una posición
            break

def animar_muertes():
    for enemigo in Enemigos_muertos[:]: #Recorriendo los elementos
        Ventana_principal.blit(Muerte, (enemigo[0], enemigo[1])) #Cambia el frame del enemigo
        enemigo[2] -= 1
        if enemigo[2] <= 0:  # Elimina animación si el tiempo termina
            Enemigos_muertos.remove(enemigo) #Elimina el enemigo muerto

def mostrar_puntuacion(): #Muestra y desarrollla la puntuación que saldrá
    fuente = pygame.font.Font(None, 24) #Establece un texto con una fuente predeterminada en tamaño 24 de letra
    texto = fuente.render(f"Puntuación: {Puntuacion}", True, (255, 255, 255)) #Renderiza el texto que se escribirá con la fuente y su posición y si se debe mostrar
    Ventana_principal.blit(texto, (10, 10)) #Lo carga dentro de la imagen

def mostrar_vidas(Vidas): #Define cuales son las vidas que le falta al jugador antes de perder
    if Vidas == 3:
        Ventana_principal.blit(Vida3, Pos3)
        Ventana_principal.blit(Vida2, Pos2)
        Ventana_principal.blit(Vida1, Pos1)
    if Vidas == 2:
        Ventana_principal.blit(Vida2, Pos2)
        Ventana_principal.blit(Vida1, Pos1)
    if Vidas == 1:
        Ventana_principal.blit(Vida1, Pos1)
    if Vidas <= 0:
        Finalizar = True

#Configuración de la velocidad y frames
reloj = pygame.time.Clock() #Importante en la actualización de imágenes
print("Configuración cargada") #Medidas a tomar

#Preparando la pantalla
Ventana_principal.fill(Colorfondo)
pygame.display.flip() #Actualiza la pantalla del juego
pygame.mixer.music.load('Música/Batallando.mp3') #Carga la música almacenada en las carpetas
pygame.mixer.music.set_volume(0.4) #Establece el volumen un 40%
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
                sonido_disparo = pygame.mixer.Sound("Música/Disparo_sonido.mp3") #Carga el sonido 
                sonido_disparo.set_volume(0.5)  # Ajusta el volumenal 50%
                sonido_disparo.play() #Ejecuta el sonido
                Disparos_activos.append([Posicion_jugador[0] + 20, Posicion_jugador[1]]) #Agrega un disparo con sus coordenadas respecto al jugador

    ### Cierre alternativo ###
    Tecla_presionada = pygame.key.get_pressed() #Variable del tipo bool
    if Tecla_presionada[pygame.K_ESCAPE]: #Cierra el juego cuando le da a la tecla escape
        print("Se cerró el juego") 
        Finalizar = True

    ### CONFIGURACIÓN DE LOS CONTROLES ###
    if Tecla_presionada[pygame.K_g]: #Centra al jugador si es que se pierde en prueba
        print("Centrando jugador")
        Posicion_jugador = [0, 0]
    Imagen_jugador = mover_jugador(Tecla_presionada, Posicion_jugador) #Ocasiona el movimiento del jugador 

    # Actualizar elementos del juego - funciones esenciales
    generar_enemigos()
    mover_enemigos()
    generar_enemigos2()
    mover_enemigos2()
    enemigo_disparo()
    enemigo_disparo2()
    actualizar_disparos()
    Choque_jugador()
    
    #Configuración de la ventana y los dibujos
    Ventana_principal.fill(Colorfondo) #Color de fondo de pantalla
    Ventana_principal.blit(Fondo, (0,0)) #Actualiza el fondo de pantalla
    Ventana_principal.blit(Imagen_jugador, Posicion_jugador) #Imagen del objeto y su posicion para siempre - elemento en capa mayor

    for disparo in Disparos_activos: #Actualiza cada disparo
        Ventana_principal.blit(Frames_disparo[3], disparo)

    for disparoe in Disparos_enemigos_activos: #Actualiza los disparos enemigos
        Ventana_principal.blit(Frames_disparo[2], disparoe)

    for disparoe2 in Disparos_enemigos_activos2: #Actualiza los disparos enemigos 2
        Ventana_principal.blit(Frames_disparo[1], disparoe2)

    for enemigo in Enemigos: #Actualiza cada enemigo tipo 1
        Ventana_principal.blit(Enemigos_posibles[1], enemigo)
    
    for enemigo2 in Enemigos2: #Actualiza cada enemigo tipo 2
        Ventana_principal.blit(Enemigos_posibles[2], enemigo2) 

    animar_muertes()
    mostrar_puntuacion()
    mostrar_vidas(Vidas)

    if Vidas == 0: #Comprueba si el jugador tiene 3 vidas
        Finalizar = True
    else: #En el caso que continue con mas de vidas
        if Puntuacion >= 1500:
            Ventana_principal.fill((0, 0, 0))
            fuente3 = pygame.font.Font(None, 40)
            texto3 = fuente3.render(f"¡Ganaste!", True, (255, 255, 255))
            Ventana_principal.blit(texto3, (300,240))  
            pygame.display.flip()
            time.sleep(5)
            pygame.quit()
        else:
            pygame.display.flip()
        
    # print("Ventana actualizada") #Validación 6#
    ### Todo el código de sprites, dibujos y música deben ir encima del comentario ###
    
    ### Limita a 60 fotogramas por segundo (Imágenes cargadas y pasadas por segundo) ###
    reloj.tick(60)
    # print("60 Fps corriendo") ##Validación 7##
########################################################################################
if Finalizar: #Si finaliza pero ve que no hay pantalla de ganador, ejecuta un Game Over
    Ventana_principal.fill((0, 0, 0))
    pygame.mixer.music.stop()
    fuente2 = pygame.font.Font(None, 36)
    texto2 = fuente2.render(f"Game Over", True, (255, 255, 255))
    Ventana_principal.blit(texto2, (300, 240))
    pygame.display.flip()    
    time.sleep(3)
pygame.quit() #Si no hay otra acción a realizar - Cerrar el juego
print("Cerrado") 

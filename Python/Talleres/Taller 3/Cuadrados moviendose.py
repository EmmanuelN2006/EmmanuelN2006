#Cuadrados moviendose
import pygame, sys, time
from pygame.locals import *
Jugar = bool; Jugar = True

pygame.init() #Inicia el juego

#Ventana
Ancho = 640
Alto = 480
ventana = pygame.display.set_mode((Ancho, Alto), 0, 32) #Establece la ventana
pygame.display.set_caption('Cuadrados moviendose')

#Valores de movimiento
Abajo_izquierda = 1
Abajo_derecha = 3
Arriba_izquierda = 7
Arriba_derecha = 9
Velocidad = 4

#Colores
Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)
Verde = (0, 255, 0)
Azul = (0, 0, 255)

#Configuración de los cuadrados - Usar pygame.Rect(posicion x, posicion y, ancho, alto)
c1 = {'dimension':(320, 240, 35, 45), 'Color': Verde, 'Direccion': Arriba_derecha}
c2 = {'dimension':(134, 400, 60, 60), 'Color': Azul, 'Direccion' : Abajo_izquierda}
c3 = {'dimension':(400, 100, 40, 50), 'Color': Blanco, 'Direccion' : Arriba_izquierda}
Cuadrados = [c1, c2, c3]

#Bucle para actualizar y usar el programa
while Jugar:
    #Para poder cerrar la ventana del juego
    for evento in pygame.event.get():
        if evento.type == QUIT:
            Jugar = False
    
    #Movimiento de los cuadrados
    
    #Para colorear la pantalla de otro color
    pygame.display.fill(Negro)
    ventana.fill(Negro)
    
    #Actualiza la ventana
    pygame.display.update()
    ventana.update() #Actualiza la pantalla
    time.sleep(0.05) #Descanso para la actualización de la pantalla
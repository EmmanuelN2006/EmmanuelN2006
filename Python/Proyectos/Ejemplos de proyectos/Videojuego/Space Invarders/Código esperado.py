import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuración de pantalla
Colorfondo = (35, 50, 25)
Dimensiones = [720, 480]
Ventana_principal = pygame.display.set_mode(Dimensiones)
pygame.display.set_caption("Proyecto - Space Invaders")

# Variables globales
Finalizar = False
vidas = 3
puntuacion = 0
disparos_activos = []
enemigos = []

# Frames del jugador
Frames_jugador = {
    1: pygame.Surface((50, 50)),  # Sustituye esto con tus imágenes
}
Frames_jugador[1].fill((0, 255, 0))  # Verde como marcador de jugador

# Frames de enemigos
Frames_enemigo = pygame.Surface((50, 50))  # Sustituye con tus imágenes
Frames_enemigo.fill((255, 0, 0))  # Rojo como marcador de enemigos

# Frames de disparos
Frames_disparo = pygame.Surface((10, 20))  # Sustituye con tus imágenes
Frames_disparo.fill((255, 255, 0))  # Amarillo como marcador de disparos

# Jugador
Posicion_jugador = [Dimensiones[0] // 2, Dimensiones[1] - 60]
Velocidad_jugador = 5

# Reloj para controlar FPS
reloj = pygame.time.Clock()

# Funciones
def generar_enemigos():
    """Genera enemigos en posiciones aleatorias en la parte superior."""
    if len(enemigos) < 5:  # Máximo 5 enemigos en pantalla
        x = random.randint(0, Dimensiones[0] - 50)
        enemigos.append([x, -50])  # Añade el enemigo fuera de la pantalla

def mover_enemigos():
    """Mueve enemigos hacia abajo y los elimina si salen de pantalla."""
    global vidas
    for enemigo in enemigos[:]:
        enemigo[1] += 3  # Velocidad de movimiento
        if enemigo[1] > Dimensiones[1]:  # Si el enemigo pasa el límite
            enemigos.remove(enemigo)

def actualizar_disparos():
    """Actualiza la posición de los disparos y elimina los que están fuera."""
    global puntuacion
    for disparo in disparos_activos[:]:
        disparo[1] -= 10  # Movimiento hacia arriba
        if disparo[1] < 0:
            disparos_activos.remove(disparo)
        else:
            # Detectar colisión con enemigos
            for enemigo in enemigos[:]:
                if enemigo[0] < disparo[0] < enemigo[0] + 50 and enemigo[1] < disparo[1] < enemigo[1] + 50:
                    enemigos.remove(enemigo)
                    disparos_activos.remove(disparo)
                    puntuacion += 10
                    break

def mostrar_puntuacion():
    """Muestra la puntuación en pantalla."""
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render(f"Puntuación: {puntuacion} | Vidas: {vidas}", True, (255, 255, 255))
    Ventana_principal.blit(texto, (10, 10))

# Pantalla inicial
Ventana_principal.fill(Colorfondo)
pygame.display.flip()

# Bucle principal del juego
Finalizar = False
while not Finalizar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            Finalizar = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:  # Disparo
                disparos_activos.append([Posicion_jugador[0] + 20, Posicion_jugador[1]])

    # Controles del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and Posicion_jugador[0] > 0:
        Posicion_jugador[0] -= Velocidad_jugador
    if teclas[pygame.K_RIGHT] and Posicion_jugador[0] < Dimensiones[0] - 50:
        Posicion_jugador[0] += Velocidad_jugador

    # Actualizar elementos del juego
    generar_enemigos()
    mover_enemigos()
    actualizar_disparos()

    # Dibujar todo
    Ventana_principal.fill(Colorfondo)
    Ventana_principal.blit(Frames_jugador[1], Posicion_jugador)

    for disparo in disparos_activos:
        Ventana_principal.blit(Frames_disparo, disparo)

    for enemigo in enemigos:
        Ventana_principal.blit(Frames_enemigo, enemigo)

    mostrar_puntuacion()
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

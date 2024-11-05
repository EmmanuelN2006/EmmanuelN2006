"""Ejemplo de videojuegos"""

import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Paletas
paddle_width = 10
paddle_height = 100
player_pos = [screen_width - 20, screen_height // 2 - paddle_height // 2]
opponent_pos = [10, screen_height // 2 - paddle_height // 2]
paddle_speed = 7

# Pelota
ball_size = 15
ball_pos = [screen_width // 2, screen_height // 2]
ball_speed = [5, 5]

# Puntuación
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True
while running:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN] and player_pos[1] < screen_height - paddle_height:
        player_pos[1] += paddle_speed

    # Movimiento del oponente
    if opponent_pos[1] < ball_pos[1]:
        opponent_pos[1] += paddle_speed - 3
    if opponent_pos[1] > ball_pos[1]:
        opponent_pos[1] -= paddle_speed - 3

    # Movimiento de la pelota
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Colisiones de la pelota
    if ball_pos[1] <= 0 or ball_pos[1] >= screen_height - ball_size:
        ball_speed[1] = -ball_speed[1]

    if (ball_pos[0] >= player_pos[0] - ball_size and 
        player_pos[1] < ball_pos[1] < player_pos[1] + paddle_height):
        ball_speed[0] = -ball_speed[0]

    if (ball_pos[0] <= opponent_pos[0] + paddle_width and 
        opponent_pos[1] < ball_pos[1] < opponent_pos[1] + paddle_height):
        ball_speed[0] = -ball_speed[0]

    # Puntaje y reinicio de pelota
    if ball_pos[0] < 0:
        player_score += 1
        ball_pos = [screen_width // 2, screen_height // 2]
        ball_speed[0] = -ball_speed[0]
    elif ball_pos[0] > screen_width:
        opponent_score += 1
        ball_pos = [screen_width // 2, screen_height // 2]
        ball_speed[0] = -ball_speed[0]

    # Dibujar en pantalla
    screen.fill(black)
    pygame.draw.rect(screen, white, (*player_pos, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (*opponent_pos, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (*ball_pos, ball_size, ball_size))
    pygame.draw.aaline(screen, white, (screen_width // 2, 0), (screen_width // 2, screen_height))

    # Mostrar puntaje
    player_text = font.render(f"{player_score}", True, white)
    opponent_text = font.render(f"{opponent_score}", True, white)
    screen.blit(player_text, (screen_width // 2 + 20, 20))
    screen.blit(opponent_text, (screen_width // 2 - 40, 20))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

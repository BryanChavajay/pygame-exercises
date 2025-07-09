import pygame
import random

# Configuraciones de pygame
pygame.init()  # Inicializamos pygame
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800  # Medidas de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Creamos la pantalla
clock = pygame.time.Clock()  # Reloj interno
running = True

# Fuente para dibujar los componentes
font = pygame.font.SysFont("Couries", 40)

x, y, velocity = 400, 400, 10

# Bucle del juego
while running:
    # Pull de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Evento para cerrar la ventana
            running = False

    screen.fill((0, 0, 0))  # Color de la pantalla

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - 40:
        x += velocity
    if keys[pygame.K_UP] and y > 0:
        y -= velocity
    if keys[pygame.K_DOWN] and y < SCREEN_HEIGHT - 40:
        y += velocity

    spaceship = font.render("-^-", True, (255, 255, 255))
    screen.blit(spaceship, (x, y))

    pygame.display.flip()  # Actualizamos la pantalla
    clock.tick(60)  # Limitamos a 60 FPS

pygame.quit()

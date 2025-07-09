import pygame

# Configuraciones de pygame
pygame.init()  # Inicializamos pygame
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800  # Medidas de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Creamos la pantalla
clock = pygame.time.Clock()  # Reloj interno
running = True

# Bucle del juego
while running:
    # Pull de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Evento para cerrar la ventana
            running = False

    screen.fill((255, 255, 255))  # Color de la pantalla

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    pygame.display.flip()  # Actualizamos la pantalla
    clock.tick(60)  # Limitamos a 60 FPS

pygame.quit()

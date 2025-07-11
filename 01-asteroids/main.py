import pygame
import random

# Configuraciones de pygame
pygame.init()  # Inicializamos pygame
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800  # Medidas de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Creamos la pantalla
clock = pygame.time.Clock()  # Reloj interno
running = True

x, y, velocity, git_box = 400, 400, 10, 40

# Fuente para dibujar los componentes
font = pygame.font.SysFont("Couries", git_box)
spaceship = font.render("-^-", True, (255, 255, 255))
bullet = font.render("!", True, (255, 255, 255))
asteroid = font.render("#", True, (255, 255, 55))


def generate_bullet(x: float, y: float):
    return (bullet, (x, y))


def generate_asteroid(x: float, y: float):
    return (asteroid, (x, y))


bullets = []
asteroids = []
count = 0

# Bucle del juego
while running:
    # Pull de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Evento para cerrar la ventana
            running = False

        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            bullets.append(generate_bullet(x + (git_box / 4), y - git_box))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - git_box:
        x += velocity
    if keys[pygame.K_UP] and y > 0:
        y -= velocity
    if keys[pygame.K_DOWN] and y < SCREEN_HEIGHT - git_box:
        y += velocity

    if count >= 25:
        asteroids.append(
            generate_asteroid(random.randint(git_box, SCREEN_WIDTH - git_box), git_box)
        )
        count = 0

    count += 1

    if len(asteroids) > 0:
        for i, item in enumerate(asteroids):
            surface, position = item
            if position[1] + velocity < SCREEN_HEIGHT:
                asteroids[i] = (
                    surface,
                    (position[0], (position[1] + velocity)),
                )
            else:
                running = False

    if len(bullets) > 0:
        for i, item in enumerate(bullets):
            surface, position = item
            if position[1] - velocity < 0:
                bullets.pop(i)
                pass
            else:
                bullets[i] = (
                    surface,
                    (position[0], (position[1] - velocity)),
                )

            bullet_rect = pygame.Rect(
                position[0], position[1] - velocity, git_box, git_box
            )

            for j, item_2 in enumerate(asteroids):
                surface_2, position_2 = item_2
                asteroid_rect = pygame.Rect(
                    position_2[0], position_2[1], git_box, git_box
                )
                if asteroid_rect.colliderect(bullet_rect):
                    bullets.pop(i)
                    asteroids.pop(j)

    screen.fill((0, 0, 0))  # Color de la pantalla

    screen.blit(spaceship, (x, y))  # Renderizamos la nave espacial
    screen.blits(bullets)  # Renderizamos las balas
    screen.blits(asteroids)  # Renderizamos los asteroides

    pygame.display.flip()  # Actualizamos la pantalla
    clock.tick(30)  # Limitamos a 60 FPS

pygame.quit()

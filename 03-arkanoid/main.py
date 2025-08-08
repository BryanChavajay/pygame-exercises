import pygame

import config
from entities.starbase import Starbase
from entities.ball import Ball

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()


background_image = pygame.image.load(config.paths["background"])


# Entities
starbase = Starbase()
ball = Ball()


running = True
while running:
    clock.tick(config.FPS)
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()

    starbase.move(keys_pressed)
    starbase.draw(screen)
    ball.move()
    ball.draw(screen)

    if ball.get_rect().colliderect(starbase.get_rect()):
        ball.velocity_y = -ball.velocity_y

    if ball.y >= config.SCREEN_HEIGHT:
        running = False

    pygame.display.flip()

pygame.quit()

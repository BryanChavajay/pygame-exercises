import pygame

import config
from entities.starbase import Starbase
from entities.ball import Ball
from generatebricks import generate_bricks

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()


background_image = pygame.image.load(config.paths["background"])


# Entities
starbase = Starbase()
ball = Ball()

bricks = generate_bricks(cols=config.BRICK_COLS, rows=config.BRICK_ROWS)

running = True
while running:
    clock.tick(config.FPS)
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()

    starbase.move(keys_pressed)
    ball.move()

    for brick in bricks:
        brick.draw(screen)

    starbase.draw(screen)
    ball.draw(screen)

    if ball.get_rect().colliderect(starbase.get_rect()):
        ball.velocity_y = -ball.velocity_y

    if ball.y >= config.SCREEN_HEIGHT:
        running = False

    pygame.display.flip()

pygame.quit()

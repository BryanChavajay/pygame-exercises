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

IN_ACTION = False
running = True
while running:
    clock.tick(config.FPS)
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                IN_ACTION = not IN_ACTION

    keys_pressed = pygame.key.get_pressed()

    starbase.move(keys_pressed)

    for brick in bricks:
        brick.draw(screen)

    starbase.draw(screen)

    if IN_ACTION:
        ball.move()
    else:
        ball.x = starbase.x + starbase.surface.get_width() // 2
        if ball.x < config.SCREEN_WIDTH // 2:
            ball.velocity_x = -ball.velocity_x
        else:
            ball.velocity_x = abs(ball.velocity_x)

    ball.draw(screen)

    if ball.get_rect().colliderect(starbase.get_rect()):
        ball.velocity_y = -ball.velocity_y

    if ball.y >= config.SCREEN_HEIGHT:
        running = False

    for brick in bricks:
        if brick.get_rect().colliderect(ball.get_rect()):
            brick.hit()
            ball.velocity_y = -ball.velocity_y
        if brick.life <= 0:
            bricks.remove(brick)
            break

    pygame.display.flip()

pygame.quit()

import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
GIT_BOX = 40
VELOCITY = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont("Couries", GIT_BOX)


class Starship:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.velocity = VELOCITY
        self.surface = font.render("-^-", True, WHITE)

    def draw(self):
        screen.blit(self.surface, (self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.velocity
        if keys[pygame.K_d] and self.x < SCREEN_WIDTH:
            self.x += self.velocity
        if keys[pygame.K_w] and self.y < 0:
            self.y -= self.velocity
        if keys[pygame.K_s] and self.y < SCREEN_HEIGHT:
            self.y += self.velocity


starship = Starship()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()
    starship.move(keys_pressed)

    screen.fill(BLACK)
    starship.draw()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

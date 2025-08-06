import pygame
import os


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
HOME, IN_GAME, GAME_OVER = "HOME", "INGAME", "GAME_OVER"
FONT_HIT_BOX = 40
VELOCITY = 10
FPS = 30

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()


background_path = os.path.join(os.getcwd(), "03-arkanoid", "assets", "background.png")
background_image = pygame.image.load(background_path)


class Starbase:
    def __init__(self) -> None:
        self.x = (SCREEN_WIDTH // 2) - 50
        self.y = SCREEN_HEIGHT - 100
        self.surface = pygame.image.load("./03-arkanoid/assets/starbase.png")

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def get_rect(self):
        return self.surface.get_rect(topleft=(self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= VELOCITY
        if keys[pygame.K_RIGHT] and self.x < (SCREEN_HEIGHT - self.surface.get_width()):
            self.x += VELOCITY


starbase = Starbase()


running = True
while running:
    clock.tick(FPS)
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()

    starbase.move(keys_pressed)
    starbase.draw(screen)

    pygame.display.flip()

pygame.quit()

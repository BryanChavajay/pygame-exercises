import pygame

import config


class Starbase:
    def __init__(self) -> None:
        self.x = (config.SCREEN_WIDTH // 2) - 50
        self.y = config.SCREEN_HEIGHT - 100
        self.surface = pygame.image.load(config.paths["starbase"])

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def get_rect(self):
        return self.surface.get_rect(topleft=(self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= config.VELOCITY
        if keys[pygame.K_RIGHT] and self.x < (
            config.SCREEN_HEIGHT - self.surface.get_width()
        ):
            self.x += config.VELOCITY

import pygame

import config


class Brick:
    def __init__(self, x: int, y: int, color: str) -> None:
        self.x = x
        self.y = y
        self.surface = pygame.image.load(config.paths[color])
        self.life = 3

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def get_rect(self):
        return self.surface.get_rect(topleft=(self.x, self.y))

import pygame

import config


class Ball:
    def __init__(self) -> None:
        self.x = config.SCREEN_WIDTH // 2
        self.y = config.SCREEN_HEIGHT - 135
        self.surface = pygame.image.load(config.paths["ball"])
        self.velocity_x = config.VELOCITY
        self.velocity_y = -config.VELOCITY

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def get_rect(self):
        return self.surface.get_rect(topleft=(self.x, self.y))

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Bounce off the walls
        if self.x <= 0 or self.x + self.surface.get_width() >= config.SCREEN_WIDTH:
            self.velocity_x = -self.velocity_x
        if self.y <= 0:
            self.velocity_y = -self.velocity_y

import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
HIT_BOX = 40
VELOCITY = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont("Couries", HIT_BOX)


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
        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.velocity
        if keys[pygame.K_s] and self.y < SCREEN_HEIGHT:
            self.y += self.velocity

    def get_rect(self):
        return pygame.Rect(self.x, self.y, 3 * HIT_BOX, HIT_BOX)


class Bullet:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.surface = font.render("!", True, WHITE)

    def draw(self):
        screen.blit(self.surface, (self.x, self.y))

    def move(self):
        self.y -= VELOCITY

    def get_rect(self):
        return pygame.Rect(self.x, self.y, HIT_BOX, HIT_BOX)


class Asteroid:
    def __init__(self):
        self.x = random.randint(HIT_BOX, SCREEN_WIDTH - HIT_BOX)
        self.y = HIT_BOX
        self.surface = font.render("#", True, WHITE)

    def draw(self):
        screen.blit(self.surface, (self.x, self.y))

    def move(self):
        self.y += VELOCITY

    def get_rect(self):
        return pygame.Rect(self.x, self.y, HIT_BOX, HIT_BOX)


starship = Starship()
bullets: list[Bullet] = []
asteroids_time = 0
asteroids: list[Asteroid] = []


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            bullets.append(Bullet(starship.x + (HIT_BOX / 3), starship.y - HIT_BOX))

    keys_pressed = pygame.key.get_pressed()
    starship.move(keys_pressed)

    screen.fill(BLACK)

    for bullet in bullets:
        bullet.move()
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.draw()

    if asteroids_time >= 50:
        asteroids.append(Asteroid())
        asteroids_time = 0
    else:
        asteroids_time += 1

    for asteroid in asteroids:
        asteroid.move()
        asteroid.draw()
        if asteroid.y >= SCREEN_HEIGHT:
            running = False
        for bullet in bullets:
            if bullet.get_rect().colliderect(asteroid.get_rect()):
                bullets.remove(bullet)
                asteroids.remove(asteroid)

    starship.draw()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

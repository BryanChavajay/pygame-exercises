import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
HIT_BOX = 40
VELOCITY = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOME, IN_GAME, GAME_OVER = "HOME", "INGAME", "GAME_OVER"

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
status = HOME
msg_welcome = font.render(
    "PRECIONA LA TECLA [Y] PARA COMENZAR EL JUEGO", True, WHITE
)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if (
            event.type == pygame.KEYUP
            and event.key == pygame.K_SPACE
            and status == IN_GAME
        ):
            bullets.append(Bullet(starship.x + (HIT_BOX / 3), starship.y - HIT_BOX))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_y and status == HOME:
            status = IN_GAME

    keys_pressed = pygame.key.get_pressed()

    screen.fill(BLACK)

    if status == HOME:
        screen.blit(msg_welcome, (40, 380))
    elif status == IN_GAME:
        starship.move(keys_pressed)

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

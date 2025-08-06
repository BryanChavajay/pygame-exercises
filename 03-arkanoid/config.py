import os

HOME, IN_GAME, GAME_OVER = "HOME", "INGAME", "GAME_OVER"

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
FONT_HIT_BOX = 40
VELOCITY = 10
FPS = 30

# Paths
paths = {
    "background": os.path.join(os.getcwd(), "03-arkanoid", "assets", "background.png"),
    "starbase": os.path.join(os.getcwd(), "03-arkanoid", "assets", "starbase.png"),
}

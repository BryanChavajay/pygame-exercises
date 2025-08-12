import os

HOME, IN_GAME, GAME_OVER = "HOME", "INGAME", "GAME_OVER"

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
FONT_HIT_BOX = 40
VELOCITY = 10
FPS = 30

ASSETS_PATH = os.path.join(os.getcwd(), "03-arkanoid", "assets")

# Paths
paths = {
    "background": os.path.join(ASSETS_PATH, "background.png"),
    "starbase": os.path.join(ASSETS_PATH, "starbase.png"),
    "ball": os.path.join(ASSETS_PATH, "ball.png"),
    "blue_brick": os.path.join(ASSETS_PATH, "blue_brick.png"),
    "green_brick": os.path.join(ASSETS_PATH, "green_brick.png"),
    "orange_brick": os.path.join(ASSETS_PATH, "orange_brick.png"),
    "pink_brick": os.path.join(ASSETS_PATH, "pink_brick.png"),
    "red_brick": os.path.join(ASSETS_PATH, "red_brick.png"),
}

# Brick configuration
BRICK_ROWS = 8
BRICK_COLS = 4
POSITION_X_FIRST_BRICK = 80
POSITION_Y_FIRST_BRICK = 50

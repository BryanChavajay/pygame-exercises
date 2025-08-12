import random

from entities.brick import Brick
import config

defult_brick = Brick(0, 0, "blue_brick")


def generate_bricks(rows: int, cols: int) -> list[Brick]:
    colors = ["blue_brick", "green_brick", "orange_brick", "pink_brick", "red_brick"]

    bricks = []
    brick_width = defult_brick.surface.get_width()
    brick_height = defult_brick.surface.get_height()

    for row in range(rows):
        for col in range(cols):
            x = config.POSITION_X_FIRST_BRICK + (col * brick_width)
            y = config.POSITION_Y_FIRST_BRICK + (row * brick_height)
            color = random.choice(colors)
            brick = Brick(x, y, color)
            bricks.append(brick)

    return bricks

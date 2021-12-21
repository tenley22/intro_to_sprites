# color constants
import pygame.font
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLOCK_COLOR = (100, 0, 100)
PINK = (250, 120, 240)

# font size constants
SMALL_FONT = pygame.font.Font("assets/unifont.ttf", 25)
MEDIUM_FONT = pygame.font.Font("assets/unifont.ttf", 35)
LARGE_FONT = pygame.font.Font("assets/unifont.ttf", 45)

# game constants
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 700
FPS = 60
MISSILE_DELAY = 300
BOMB_DELAY = 500

# for missile/bomb
MISSILE_WIDTH = 4
MISSILE_HEIGHT = 15
BOMB_HW = 6

# explosion images
EXPLOSIONS = []
for i in range(8):
    image_path = pygame.image.load(f"assets/sprite_{i}.png")
    EXPLOSIONS.append(image_path)

# images
PLAYER = "assets/player.png"
RED_ALIEN = "assets/red.png"
GREEN_ALIEN = "assets/green.png"
YELLOW_ALIEN = "assets/yellow.png"


SHEILDS = [
    "  xxxxxxx",
    " xxxxxxxxx",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
    "xxx     xxx",
    "xx       xx",
]

BLOCK_HEIGHT = 7
BLOCK_WIDTH = 7

UFO_SCORE = 100
YELLOW_SCORE = 10
GREEN_SCORE = 15
RED_SCORE = 20

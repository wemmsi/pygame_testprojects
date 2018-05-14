# All game options and settings
# platformer/settings.py

# Game options/settings
TITLE = "Unicorns"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'courier new'
HS_FILE = 'highscore.txt'
SPRITESHEET = 'spritesheet_jumper.png'

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

# Game properties
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOBS_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 60),
                (WIDTH / 2 -50, HEIGHT * 3 / 4 - 50),
                (125, HEIGHT - 350),
                (350, 200),
                (175, 100)]

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
LIGHTPINK = (255, 198, 233)
PINK = (255, 43, 145)
BGCOLOR = PINK

import os

base_dir = os.path.dirname(__file__)
colors_folder = os.path.join(base_dir, "colors_folder")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

color_list = [
    "red", "orange", "yellow", "green", "blue",
    "purple", "white", "hot pink", "black",
    "navy", "light pink"
]

PINK_OPTIONS = ["hot pink", "light pink"]

PLAYER_MAX_HEALTH = 100
OPPONENT_MAX_HEALTH = 100

PLAYER_HEALTH_DECAY = 0.35

PLAYER_START_X = 100
PLAYER_START_Y = 300

OPPONENT_START_X = 500
OPPONENT_START_Y = 300

PLAYER_SPEED = 1
OPPONENT_SPEED = 3

MONSTER_SUFFIX = "_monster.jpeg"

PINK_MONSTER_FILE = "pink_monster.jpeg"

POOL_NOODLE_FILE = "pool_noodle.jpeg"
PINK_GUN_FILE = "pink_gun.jpeg"

HOT_PINK_SCREEN = "hot_pink.jpg"
LIGHT_PINK_SCREEN = "light_pink.jpg"

CHARACTER_WIDTH = 120
CHARACTER_HEIGHT = 120

POOL_NOODLE_SIZE = (80, 20)
PINK_GUN_SIZE = (60, 30)

PLAYER_WEAPON_OFFSET_X = -10
PLAYER_WEAPON_OFFSET_Y = -10

OPPONENT_WEAPON_OFFSET_X = -30
OPPONENT_WEAPON_OFFSET_X_DIVISOR = 3

OPPONENT_WEAPON_OFFSET_X = -30
OPPONENT_WEAPON_OFFSET_Y_DIVISOR = 3

HEALTH_BAR_WIDTH = 150
HEALTH_BAR_HEIGHT = 15

PLAYER_HEALTH_BAR_POS = (50, 50)
OPPONENT_HEALTH_BAR_POS = (400, 50)

OPPONENT_BASE_SPEED = 2
OPPONENT_RANDOM_RANGE = 2
STOP_DISTANCE = 80

PINK = (255, 105, 180)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)

def get_monster_image_path(color):
    file_name = f"{color.replace(' ', '_')}{MONSTER_SUFFIX}"
    return os.path.join(colors_folder, file_name)

def get_pink_monster_path():
    return os.path.join(colors_folder, PINK_MONSTER_FILE)

def get_weapon_path(file_name):
    return os.path.join(colors_folder, file_name)

def get_celebration_image(pink_type):
    if pink_type == "hot pink":
        return os.path.join(colors_folder, HOT_PINK_SCREEN)
    elif pink_type == "light pink":
        return os.path.join(colors_folder, LIGHT_PINK_SCREEN)
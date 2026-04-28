import os

base_dir = os.path.dirname(__file__)
colors_folder = os.path.join(base_dir, "colors_folder")

screen_width = 800
screen_height = 600
FPS = 60

color_list = [
    "red", "orange", "yellow", "green", "blue",
    "purple", "white", "hot pink", "black",
    "navy", "light pink"
]

pink_options = ["hot pink", "light pink"]

player_max_health = 100
opponent_max_health = 100

player_health_decay = 0.5

player_start_x = 100
player_start_y = 300

opponent_start_x = 500
opponent_start_y = 300

player_speed = 1
opponent_speed = 3

monster_suffix = "_monster.jpeg"

pink_monster_file = "pink_monster.jpeg"

pool_noodle_file = "pool_noodle.jpeg"
pink_gun_file = "pink_gun.jpeg"

hot_pink_screen = "hot_pink.jpg"
light_pink_screen = "light_pink.jpg"

character_width = 120
character_height = 120

pool_noodle_size = (80, 20)
pink_gun_size = (60, 30)

player_weapon_offset_x = -10
player_weapon_offset_Y = -10

opponent_weapon_offset_x = -30
opponent_weapon_offset_y_divisor = 3

health_bar_width = 150
health_bar_height = 15

player_health_bar_pos = (50, 50)
opponent_health_bar_pos = (400, 50)

def get_monster_image_path(color):
    file_name = f"{color.replace(' ', '_')}{monster_suffix}"
    return os.path.join(colors_folder, file_name)

def get_pink_monster_path():
    return os.path.join(colors_folder, pink_monster_file)

def get_weapon_path(file_name):
    return os.path.join(colors_folder, file_name)

def get_celebration_image(pink_type):
    if pink_type == "hot pink":
        return os.path.join(colors_folder, hot_pink_screen)
    elif pink_type == "light pink":
        return os.path.join(colors_folder, light_pink_screen)
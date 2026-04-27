import os

base_dir = os.path.dirname(__file__)
colors_folder = os.path.join(BASE_DIR, "colors_folder")

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
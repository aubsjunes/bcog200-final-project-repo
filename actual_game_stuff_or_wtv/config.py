import os

instructions_background_color = "#FFB5E6"
instructions_font = ("Arial", 20)
instructions_font_color = "#000000"

def scale_image(image, width, height):
    image = scale_image(image, 120, 120)
    weapon = scale_image(weapon, 60, 20)

BASE_DIR = os.path.dirname(__file__)
colors_folder = os.path.join(BASE_DIR, "colors_folder")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
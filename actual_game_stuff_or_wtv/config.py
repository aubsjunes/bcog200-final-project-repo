import pygame

window_height = 800
window_width = 1600

instructions_background_color = "#FFB5E6"
instructions_font = ("Arial", 20)
instructions_font_color = "#000000"

def scale_image(image, width, height):
    image = scale_image(image, 120, 120)
    weapon = scale_image(weapon, 60, 20)
    return pygame.transform.scale(image, (width, height))
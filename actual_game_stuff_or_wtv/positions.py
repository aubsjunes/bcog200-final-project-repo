import pygame
import os

COLORS_FOLDER = "colors_folder"

def load_image(file_name):
    path = os.path.join(COLORS_FOLDER, file_name)
    image = pygame.image.load(path).convert_alpha()
    return image


def create_player(color):
    file_name = f"{color.replace(' ', '_')}_monster.jpeg"

    image = load_image(file_name)
    weapon = load_image("pool_noodle.jpeg")

    player = {
        "x": 100,
        "y": 300,
        "image": image,
        "weapon": weapon,
        "width": image.get_width(),
        "height": image.get_height(),
        "health": 100
    }

    return player

def create_pink():
    image = load_image("pink_monster.jpeg")
    weapon = load_image("pink_gun.jpeg")

    opponent = {
        "x": 500,
        "y": 300,
        "image": image,
        "weapon": weapon,
        "width": image.get_width(),
        "height": image.get_height(),
        "health": 9999
    }

    return opponent

def get_player_weapon_pos(player):
    weapon_x = player["x"] + player["width"] - 10
    weapon_y = player["y"] + player["height"] // 2 - 10

    return weapon_x, weapon_y
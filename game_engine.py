import pygame
import config

def load_image(path, size=None):
    image = pygame.image.load(path).convert_alpha()

    if size:
        image = pygame.transform.scale(image, size)

    return image

def create_player(color):
    image_path = config.get_monster_image_path(color)

    player = {
        "x": config.player_start_x,
        "y": config.player_start_y,
        "image": load_image(
            image_path,
            (config.character_width, config.character_height)
        ),
        "weapon": load_image(
            config.get_weapon_path(config.pool_noodle_file),
            config.pool_noodle_size
        ),
        "width": config.character_width,
        "height": config.character_height,
        "health": config.player_max_health
    }

    return player

def create_pink_opponent():
    image_path = config.get_pink_monster_path()

    opponent = {
        "x": config.opponent_start_x,
        "y": config.opponent_start_y,
        "image": load_image(
            image_path,
            (config.character_width, config.character_height)
        ),
        "weapon": load_image(
            config.get_weapon_path(config.pink_gun_file),
            config.pink_gun_size
        ),
        "width": config.character_width,
        "height": config.character_height,
        "health": config.opponent_max_health
    }

    return opponent
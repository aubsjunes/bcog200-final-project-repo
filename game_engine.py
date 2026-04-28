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

def get_player_weapon_pos(player):
    weapon_x = (
        player["x"]
        + player["width"]
        + config.player_weapon_offset_x
    )

    weapon_y = (
        player["y"]
        + player["height"] // 2
        + config.player_weapon_offset_y
    )

    return weapon_x, weapon_y


def get_pink_weapon_pos(opponent):
    weapon_x = opponent["x"] + config.opponent_weapon_offset_x

    weapon_y = (
        opponent["y"]
        + opponent["height"] // config.opponent_weapon_offset_y_divisor
    )

    return weapon_x, weapon_y

def update_health(player, opponent):

    player["health"] -= config.player_health_decay
    opponent["health"] = config.opponent_max_health

def handle_player_input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        pass
    if keys[pygame.K_RIGHT]:
        pass
    if keys[pygame.K_SPACE]:
        pass

def enemy_behavior(opponent):
    opponent["x"] -= config.OPPONENT_SPEED

def render_scene(screen, player, opponent):
    screen.fill(config.WHITE)
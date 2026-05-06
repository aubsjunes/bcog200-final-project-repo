import pygame
import config
from ui_display import draw_instructions
import random

def load_image(path, size=None):
    image = pygame.image.load(path).convert_alpha()

    if size:
        image = pygame.transform.scale(image, size)

    return image

def load_image(path, size=None):
    image = pygame.image.load(path).convert_alpha()

    if size:
        image = pygame.transform.scale(image, size)

    return image

def create_player(color):
    image_path = config.get_monster_image_path(color)

    player = {
        "x": config.PLAYER_START_X,
        "y": config.PLAYER_START_Y,
        "image": load_image(
            image_path,
            (config.CHARACTER_WIDTH, config.CHARACTER_HEIGHT)
        ),
        "weapon": load_image(
            config.get_weapon_path(config.POOL_NOODLE_FILE),
            config.POOL_NOODLE_SIZE
        ),
        "width": config.CHARACTER_WIDTH,
        "height": config.CHARACTER_HEIGHT,
        "health": config.PLAYER_MAX_HEALTH
    }

    return player

def create_pink_opponent():
    image_path = config.get_pink_monster_path()

    opponent = {
        "x": config.OPPONENT_START_X,
        "y": config.OPPONENT_START_Y,
        "image": load_image(
            image_path,
            (config.CHARACTER_WIDTH, config.CHARACTER_HEIGHT)
        ),
        "weapon": load_image(
            config.get_weapon_path(config.PINK_GUN_FILE),
            config.PINK_GUN_SIZE
        ),
        "width": config.CHARACTER_WIDTH,
        "height": config.CHARACTER_HEIGHT,
        "health": config.OPPONENT_MAX_HEALTH
    }

    return opponent

def create_pink_opponent():
    image_path = config.get_pink_monster_path()

    opponent = {
        "x": config.OPPONENT_START_X,
        "y": config.OPPONENT_START_Y,
        "image": load_image(
            image_path,
            (config.CHARACTER_WIDTH, config.CHARACTER_HEIGHT)
        ),
        "weapon": load_image(
            config.get_weapon_path(config.PINK_GUN_FILE),
            config.PINK_GUN_SIZE
        ),
        "width": config.CHARACTER_WIDTH,
        "height": config.CHARACTER_HEIGHT,
        "health": config.OPPONENT_MAX_HEALTH
    }

    return opponent

def update_health(player, opponent):
    player["health"] -= config.PLAYER_HEALTH_DECAY

    opponent["health"] = config.OPPONENT_MAX_HEALTH

def update_health(player, opponent):
    player["health"] -= config.PLAYER_HEALTH_DECAY

    opponent["health"] = config.OPPONENT_MAX_HEALTH

def handle_player_input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        pass
    if keys[pygame.K_RIGHT]:
        pass
    if keys[pygame.K_SPACE]:
        pass

def enemy_behavior(opponent, player):
    distance = abs(opponent["x"] - player["x"])

    if distance <= config.STOP_DISTANCE:
        return

    random_x = random.randint(-config.OPPONENT_RANDOM_RANGE, config.OPPONENT_RANDOM_RANGE)
    random_y = random.randint(-1, 1)

    if opponent["x"] > player["x"]:
        opponent["x"] -= config.OPPONENT_BASE_SPEED
    else:
        opponent["x"] += config.OPPONENT_BASE_SPEED

    opponent["x"] += random_x
    opponent["y"] += random_y

def draw_health_bar(screen, x, y, health, max_health):
    ratio = max(health / max_health, 0)

    pygame.draw.rect(
        screen,
        config.RED,
        (x, y, config.HEALTH_BAR_WIDTH, config.HEALTH_BAR_HEIGHT)
    )

    pygame.draw.rect(
        screen,
        config.GREEN,
        (
            x,
            y,
            config.HEALTH_BAR_WIDTH * ratio,
            config.HEALTH_BAR_HEIGHT
        )
    )

def get_player_weapon_pos(player):
    weapon_x = (
        player["x"]
        + player["width"]
        + config.PLAYER_WEAPON_OFFSET_X
    )

    weapon_y = (
        player["y"]
        + player["height"] // 2
        + config.PLAYER_WEAPON_OFFSET_Y
    )

    return weapon_x, weapon_y

def get_pink_weapon_pos(opponent):
    weapon_x = opponent["x"] + config.OPPONENT_WEAPON_OFFSET_X

    weapon_y = (
        opponent["y"]
        + opponent["height"] // config.OPPONENT_WEAPON_OFFSET_Y_DIVISOR
    )

    return weapon_x, weapon_y

def render_scene(screen, player, opponent):
    screen.fill(config.PINK)

    screen.blit(player["image"], (player["x"], player["y"]))
    px, py = get_player_weapon_pos(player)
    screen.blit(player["weapon"], (px, py))

    screen.blit(opponent["image"], (opponent["x"], opponent["y"]))
    ox, oy = get_pink_weapon_pos(opponent)

    rotated_gun = pygame.transform.rotate(opponent["weapon"], -20)
    screen.blit(rotated_gun, (ox, oy))

    draw_instructions(screen)

    draw_health_bar(
        screen,
        config.PLAYER_HEALTH_BAR_POS[0],
        config.PLAYER_HEALTH_BAR_POS[1],
        player["health"],
        config.PLAYER_MAX_HEALTH
    )

    draw_health_bar(
        screen,
        config.OPPONENT_HEALTH_BAR_POS[0],
        config.OPPONENT_HEALTH_BAR_POS[1],
        opponent["health"],
        config.OPPONENT_MAX_HEALTH
    )

    pygame.display.flip()

def start_fight(player_color):
    pygame.init()

    screen = pygame.display.set_mode(
        (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
    )
    pygame.display.set_caption("Aubrey's Game of Mystical Wonder and the Color Pink")

    clock = pygame.time.Clock()

    player = create_player(player_color)
    opponent = create_pink_opponent()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_player_input()

        enemy_behavior(opponent, player)

        update_health(player, opponent)

        render_scene(screen, player, opponent)

        opponent["y"] = max(0, min(config.SCREEN_HEIGHT - opponent["height"], opponent["y"]))

        if player["health"] <= 0:
            running = False

        clock.tick(config.FPS)

    pygame.quit()
    return "lose"
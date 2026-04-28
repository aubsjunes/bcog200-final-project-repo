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
    opponent["x"] -= config.opponent_speed

def render_scene(screen, player, opponent):
    screen.blit(player["image"], (player["x"], player["y"]))
    px, py = get_player_weapon_pos(player)
    screen.blit(player["weapon"], (px, py))

    screen.blit(opponent["image"], (opponent["x"], opponent["y"]))
    ox, oy = get_pink_weapon_pos(opponent)

    gun = pygame.transform.rotate(opponent["weapon"], -20)
    screen.blit(gun, (ox, oy))

    draw_health_bar(
        screen,
        config.player_health_bar_pos[0],
        config.player_health_bar_pos[1],
        player["health"],
        config.player_max_health
    )

    draw_health_bar(
        screen,
        config.opponent_health_bar_pos[0],
        config.opponent_health_bar_pos[1],
        opponent["health"],
        config.opponent_max_health
    )

    pygame.display.flip()

def draw_health_bar(screen, x, y, health, max_health):
    ratio = max(health / max_health, 0)

    pygame.draw.rect(
        screen,
        config.red,
        (x, y, config.HEALTH_BAR_WIDTH, config.HEALTH_BAR_HEIGHT)
    )
 
    pygame.draw.rect(
        screen,
        config.green,
        (
            x,
            y,
            config.health_bar_width * ratio,
            config.health_bar_height
        )
    )
 
    pygame.draw.rect(
        screen,
        config.black,
        (x, y, config.health_bar_width, config.health_bar_height),
        2
    )

def start_fight(player_color):
    pygame.init()

    screen = pygame.display.set_mode(
        (config.screen_width, config.screen_height)
    )
    pygame.display.set_caption("What color is the best???")

    clock = pygame.time.Clock()

    player = create_player(player_color)
    opponent = create_pink_opponent()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_player_input()
        enemy_behavior(opponent)
        update_health(player, opponent)

        render_scene(screen, player, opponent)

        if player["health"] <= 0:
            running = False

        clock.tick(config.FPS)

    pygame.quit()
    return "lose"
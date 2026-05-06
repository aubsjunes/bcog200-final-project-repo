import pygame
import config

def load_image(path, size=None):
    image = pygame.image.load(path).convert_alpha()

    if size:
        image = pygame.transform.scale(image, size)

    return image

def display_intro():
    print("===================================")
    print("     Aubrey's Mystical Game of Fighting and Wonder!     ")
    print("===================================")
    print("Choose your favorite color...")
    print("Enter the arena if you dare :] \n")

def draw_instructions(screen):
    font = pygame.font.SysFont(None, 28)

    lines = [
        "CONTROLS:",
        "Arrow Keys = Move",
        "Space = Attack",
    ]

    y = config.SCREEN_HEIGHT - 120

    for line in lines:
        text = font.render(line, True, config.BLACK)
        screen.blit(text, (20, y))
        y += 25

def show_instruction_screen():
    pygame.init()

    screen = pygame.display.set_mode(
        (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
    )
    pygame.display.set_caption("How to Play")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 40)
    small_font = pygame.font.SysFont(None, 28)

    title = font.render("HOW TO PLAY", True, config.BLACK)

    lines = [
        "Use arrow keys to move",
        "Press SPACE to attack",
        "",
        "Defeat pink to win!",
        "Press any key to start"
    ]

    waiting = True

    while waiting:
        screen.fill(config.PINK)

        # Draw title
        screen.blit(title, (config.SCREEN_WIDTH // 2 - 120, 50))

        # Draw instructions
        y = 150
        for line in lines:
            text = small_font.render(line, True, config.BLACK)
            screen.blit(text, (config.SCREEN_WIDTH // 2 - 150, y))
            y += 40

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                waiting = False

        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()

def celebration_screen(pink_type):
    """
    Displays themed celebration screen when pink is chosen
    """

    pygame.init()

    screen = pygame.display.set_mode(
        (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
    )
    pygame.display.set_caption("Pink Victory")

    clock = pygame.time.Clock()

    # Load correct image (hot_pink.jpg or light_pink.jpg)
    image_path = config.get_celebration_image(pink_type)
    background = load_image(
        image_path,
        (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
    )

    font = pygame.font.SysFont(None, 60)
    sub_font = pygame.font.SysFont(None, 30)

    title_text = font.render("PINK WINS!!!", True, config.BLACK)
    subtitle_text = sub_font.render(
        f"You chose {pink_type}... of course you win.",
        True,
        config.BLACK
    )

    running = True

    while running:
        screen.fill(config.PINK)

        screen.blit(background, (0, 0))

        screen.blit(title_text, (config.SCREEN_WIDTH // 2 - 150, 50))
        screen.blit(subtitle_text, (config.SCREEN_WIDTH // 2 - 180, 120))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
from game_logic import get_player_choice, is_pink
from fight_engine import start_fight
from ui_display import display_intro, celebration_screen


COLOR_LIST = [
    "red", "orange", "yellow", "green", "blue",
    "purple", "white", "hot pink", "black",
    "navy", "light pink"
]

def main():
    display_intro()

    choice = get_player_choice(COLOR_LIST)

    if is_pink(choice):
        celebration_screen(choice)
    else:
        result = start_fight(choice)
        print(f"Game Over: You {result}")


if __name__ == "__main__":
    main()

def game_loop(screen, player, opponent):
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        opponent["x"] -= 1  # pink slowly approaches

        player["health"] -= 0.1

        render_scene(screen, player, opponent)

        if player["health"] <= 0:
            running = False

        clock.tick(60)
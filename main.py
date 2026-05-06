import config
from game_logic import get_player_choice, determine_game_path
from fight_engine import start_fight
from ui_display import display_intro, celebration_screen, show_instruction_screen

def main():
    display_intro()

    choice = get_player_choice()

    path = determine_game_path(choice)

    if path == "celebration":
        # Pink chosen → instant win
        celebration_screen(choice)

    elif path == "fight":
       
        show_instruction_screen()

        result = start_fight(choice)

        print("\n===================================")
        print("WOMP WOMP!!   GAME OVER")
        print("===================================")
        print(f"Your color ({choice}) lost :P")
        print("Pink wins. As expected. ")
        print("Better luck next time JKKKK")
        print("===================================\n")

if __name__ == "__main__":
    main()
import config

def get_player_choice():
    while True:
        print("\nAvailable colors:")
        for color in config.color_list:
            print(f"- {color}")

        choice = input("\nChoose your favorite color: ").strip().lower()

        if validate_input(choice):
            return choice
        else:
            print("BRUH. Stop trying to be different. Please choose from the list.")

def validate_input(choice):
    return choice in config.color_list

def is_pink(choice):
    return choice in PINK_OPTIONS

def is_pink(choice):
    return choice in config.PINK_OPTIONS
    
def determine_game_path(choice):
    if is_pink(choice):
        return "celebration"
    else:
        return "fight"

def normalize_choice(choice):
    return choice.strip().lower()
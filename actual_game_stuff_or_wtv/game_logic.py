def get_player_choice(color_list):
    while True:
        choice = input("What's your favorite color (choose between black, blue, green, hot pink, navy, light pink, orange, purple, red, white, or yellow): ").lower()

        if choice in color_list:
            return choice
        else:
            print("Umm that wasn't on the list. Stop trying to be different.")


def is_pink(choice):
    return choice in ["hot pink", "light pink"]
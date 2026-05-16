# pink-fighter-game

My planned project is a rigged color-versus-color fighting game made in Python using the pygame library. The player chooses their favorite color from a list of colors, and if they choose a non-pink color, their character is forced into a battle against a powerful pink opponent. The game appears to give the player control through movement and attack instructions, but the controls intentionally do not work because pink is designed to always win. If the player chooses hot pink or light pink, they instead receive a celebration screen themed around the pink color they selected (designed by me!).

Make sure to download pygame before getting started

# program structure
The project is divided into several Python files to separate game logic, configuration settings, visual rendering, and gameplay systems.
Main Files:
main.py — starts and controls the overall game flow
config.py — stores settings, file paths, colors, and constants
game_logic.py — handles player choices and determines game outcomes
fight_engine.py — manages the battle system, movement, rendering, and health mechanics
ui_display.py — displays instructions, intro screens, and celebration screens

# important functions
get_player_choice()
Located in: game_logic.py
Prompts the player to input a color choice from the approved list of colors. The function validates the input and returns the selected color as a string.

determine_game_path(color)
Located in: game_logic.py
Determines whether the player enters the rigged fight or the celebration screen depending on the selected color.
Parameters:
color (string) — the player’s chosen color

start_fight(player_color)
Located in: fight_engine.py
Runs the main pygame battle loop. This function creates the player and opponent characters, updates health bars, renders weapons and images, and controls the rigged gameplay behavior.
Parameter:
player_color (string) — selected player color

celebration_screen(pink_type)
Located in: ui_display.py
Displays a themed celebration screen if the player chooses hot pink or light pink.
Parameter:
pink_type (string) — either "hot pink" or "light pink"

enemy_behavior(opponent, player)
Located in: fight_engine.py
Controls the pink opponent’s movement during battle, including slowing movement, stopping near the player, and moving erratically.
Parameters:
opponent (dictionary) — opponent character data
player (dictionary) — player character data

# testing
The program can be tested by running the main.py file after ensuring that all required Python files and image assets are included in the project folder. The project requires files such as main.py, config.py, fight_engine.py, game_logic.py, ui_display.py, and a colors_folder directory containing all monster and weapon images. Example image files include blue_monster.jpeg, pink_monster.jpeg, pool_noodle.jpeg, pink_gun.jpeg, hot_pink.jpg, and light_pink.jpg. When the program starts, the user is prompted to choose a color from a list of approved options. If the player selects a non-pink color such as blue or green, the game launches a rigged battle scene in which the chosen monster fights against a pink opponent. The selected monster appears with a pool noodle weapon while the pink opponent appears with a pink gun. Instructions explaining the controls are displayed on screen, but the controls intentionally do not work as part of the game design. During gameplay, the player’s health bar slowly decreases while the pink opponent’s health remains full, resulting in the player always losing the battle. If the user instead chooses “hot pink” or “light pink,” the battle is skipped entirely and a themed celebration screen appears using the corresponding pink image. Invalid inputs, such as colors not included in the approved list, should cause the program to reject the entry and ask the user to input a valid color before continuing. These tests verify the program’s user input validation, image loading, pygame rendering, health bar system, opponent movement, celebration screens, and overall game flow.

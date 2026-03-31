# bcog200-final-project-repo
The goal is to set up a program that functions as a rigged video game.
It is a color versus color video game.
The program asks the player to pick their favorite color from a list:
red, orange, yellow, green, blue, purple, white, hot pink, black, navy, light pink
There are two outcomes that can happen, if the player picks a color other than pink, 
their color will be recorded and entered into a fighter game with pink (each color will represented as a monster flavor. there is a jpeg for each monster flavor.)
the selected color will be given a pool noodle to fight with light pink.
The catch is that light pink will be faster and also have a pink gun
ANother catch is that there will instructions (use the arrows to control movement and use space to hit pink with the pool noodle) on how to play but none of the controls will work because pink must win no matter what.
There will be health bars but pink can take no damage so the player just helplessly watches their color slowly loss all their health
The color (that is not pink) will try to run away and the player will try to control the game and help their color but it will not work.
If pink of any kind is chosen there will just be a screen of celebration with themes relating to the type of pink chosen (designed by me!).

Basically:
The game follows this basic flow:
The player selects a color from a predefined list.
The program checks whether the selected color is a shade of pink.
Based on the choice:
Non-pink color → enters a “fight” against light pink.
Pink color → triggers a celebration screen.
In the fight:
The player is shown controls but cannot actually affect gameplay.
The opponent (light pink) is overpowered and cannot lose.
The player’s character slowly loses health regardless of input.

List of functions to be used:
main() (duh!)

get_player_choice(color_list)
Prompts the user to choose a color.
color_list (list of strings): Available color options
choice (string): Player’s selected color

is_pink(choice)
Checks if the selected color is a shade of pink.
choice (string)
True if the color is "hot pink" or "light pink"
False otherwise

start_fight(player_color)
Starts the rigged fight sequence.
player_color (string)
Loads character sprites (JPEG images)
Displays instructions (non-functional controls)
Runs fight loop where player always loses

display_instructions()
Shows gameplay controls to the player.
Arrow keys → movement
Spacebar → attack
(These controls do not actually work.)

update_health(player, opponent)
Updates health bars during the fight.
player (object or dict)
opponent (object or dict)
Player health decreases over time
Pink opponent health never decreases

celebration_screen(pink_type)
Displays a themed celebration if a pink color is chosen.
pink_type (string): "hot pink" or "light pink"
Shows custom visuals and theme based on pink type :P

Could be used if someone wants to play a funny, unexpected game or a developer is demonstrating game design concepts.

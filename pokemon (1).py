#Milan Hill
#nov 21 2024

#intialize
#global variables
import random
pokemon_level=0
pokemon_name ="pichu"
day = 1
#functions

def Train():
    global pokemon_level
    print("your pokemon did 50 jumping jacks!")
    pokemon_level = pokemon_level + 1


def GymBattle ():
    global pokemon_level
    outcome = random.randint(1,2) #50% chance to win or lose
    if outcome == 1:
        print ("you won a batle against Charizard, your level increased by 2")
        pokemon_level = pokemon_level + 2

    else:
        print("you lost a battle against Charizard, your level didn't change")
        pokemon_level= pokemon_level + 0


def Rest():
    print("your pokemon name is: " + str (pokemon_name))
    print("your pokemon level is: " + str(pokemon_level))


def evolve():
    global pokemon_level
    if pokemon_level <10:
        pokemon_name = "pichu"
        print("your pokemon's name is: " + str(pokemon_name))
        print("your pokemon's level is " + str(pokemon_level))
    elif pokemon_level >=10  and pokemon_level <20:
        pokemon_name = "pikachu"
        print("you leveled up! your pokemon's level is " + str(pokemon_level))
        print("your pokemon's name is " + str(pokemon_name))
    elif pokemon_level >=20 and pokemon_level <50:
        pokemon_name = "riachu"
        print(" you leveled up! your pokemon's level is " + str(pokemon_level))
        print("your pokemon's name is " + str(pokemon_name))
    elif pokemon_level >=50:
        print("you have reached the end of the game. To secure your victory you must beat the final boss, fireball")
        finalboss()


def finalboss():
    global pokemon_level
    outcome = random.randint(1,2) #50% chance to win or lose
    if outcome == 1:
        print("you won a battle against fireball, the final boss, you beat the game!")

    else:
        print("you lost a battle against fireball, the final boss, you haven't secured your vistory yet")
    quit()

# The name of the file where the game data will be saved
save_file = "pokemon_game_save.txt"

# Function to save the current game state
def save_game():
    with open(save_file, "w") as file:  # Open the save file in write mode
        file.write(pokemon_name + "\n")  # Write the Pokémon's name
        file.write(str(pokemon_level) + "\n")  # Write the Pokémon's level (converted to string), followed by a newline
    print("Game saved successfully!")

# Function to load a previously saved game state
def load_game():
    global pokemon_name, pokemon_level  # Declare these as global
    try:
        with open(save_file, "r") as file:  # Open the save file in read mode
            pokemon_name = file.readline().strip()  # Read the Pokémon's name and remove any extra whitespace
            pokemon_level = int(file.readline().strip())  # Read the Pokémon's level and convert it to an integer
        print("Game loaded successfully!")
    except FileNotFoundError:
        # If the save file doesn't exist, display this message
        print("No save file found. Start a new game!")
    except ValueError:
        # If the file data is corrupted, display this message
        print("Save file is corrupted. Start a new game!")



    #Main
while True:
    print("Welcome to Pokeman Evolultion")
    print("Choose an activity for the day: " + str(day))
    print("""
    1.Train
    2.GymBattle
    3.Rest
    4.Quit
    5.SaveGame
    6.LoadGame
    """)
    activity = int(input("Activity for the day: "))
    if activity == 1:
        Train()
        evolve()
        day = day + 1
    elif activity == 2:
        GymBattle()
        evolve()
        day = day + 1
    elif activity == 3:
        Rest ()
    elif activity == 4:
        break
    elif activity == 5:
        save_game()
    elif activity == 6:
        load_game()


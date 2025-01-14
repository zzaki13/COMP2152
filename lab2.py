import random

# List of weapons
weapons = ["Use Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
print("Weapons: ", weapons)

# Function to get a valid integer input
def get_valid_int_input(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= 6:  
                return choice
            else:
                print("Error: Please enter a number between 1 and 6.")
        except ValueError:
            print("Error: Please enter a valid integer!")

try:

    weapons_selected = get_valid_int_input("Enter a number to choose a weapon (1-6): ")
    
    selected_weapon = weapons[weapons_selected - 1]

    weaponRoll = random.randint(1, 6)
    
    # Print the selected weapon and dice roll
    print(f"You chose: {selected_weapon}")
    print(f"Weapon roll result: {weaponRoll}")
    
    # Print the result based on the dice roll
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend")
    elif weaponRoll <= 4:
        print("Your weapon is meh")
    else:
        print("Thank goodness you didn't roll the Fist...")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

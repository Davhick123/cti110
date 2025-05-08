#David Hicks

#4/27/25

# P5HW_HicksDavid.py

#Making a game using ai/ Turn based fight





import random

def create_character():
    """
    Creates a new character with random name and user input for health and attack points.
    Returns:
        dict: A dictionary containing character attributes.
    """
    name_options = ["Shadow", "Blaze", "Storm", "Frost", "Ember", "Viper", "Hunter", "Phantom", "Sparrow", "Titan"]
    name = random.choice(name_options)
    print(f"Generated character name: {name}")
    health = int(input("Enter character health (number): "))
    attack_points = int(input("Enter character attack points (number): "))
    
    character = {
        "name": name,
        "health": health,
        "attack_points": attack_points
    }
    
    return character

def display_character(character):
    """
    Displays the attributes of a character.
    Args:
        character (dict): The character to display.
    """
    print("\n--- Character Info ---")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")
    print("----------------------\n")

def attack(attacker, defender):
    """
    Simulates an attack where higher attack points cause higher random damage.
    Args:
        attacker (dict): The attacking character.
        defender (dict): The defending character.
    """
    base_attack = attacker["attack_points"]
    # Damage is random between 50% and 100% of attack points
    damage = random.randint(int(base_attack * 0.5), base_attack)
    
    defender["health"] -= damage
    print(f"{attacker['name']} attacks {defender['name']} for {damage} damage!")

    if defender["health"] <= 0:
        defender["health"] = 0
        print(f"{defender['name']} has been defeated!")
    else:
        print(f"{defender['name']}'s health is now {defender['health']}.")

def heal(character):
    """
    Heals a character by a random amount.
    Args:
        character (dict): The character to heal.
    """
    heal_amount = random.randint(5, 15)
    character["health"] += heal_amount
    print(f"{character['name']} heals for {heal_amount} health points!")

def main():
    """
    Main function to run the Character Creation Game.
    """
    characters = []
    while True:
        print("\n==== Character Creation Game ====")
        print("1. Create a Character")
        print("2. Display Characters")
        print("3. Attack a Character")
        print("4. Heal a Character")
        print("5. Exit Game")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            new_character = create_character()
            characters.append(new_character)
        elif choice == "2":
            if not characters:
                print("No characters to display.")
            else:
                for character in characters:
                    display_character(character)
        elif choice == "3":
            if len(characters) < 2:
                print("Need at least two characters to attack!")
            else:
                print("Choose attacker:")
                for idx, char in enumerate(characters):
                    print(f"{idx + 1}. {char['name']}")
                attacker_idx = int(input("Enter attacker number: ")) - 1

                print("Choose defender:")
                for idx, char in enumerate(characters):
                    if idx != attacker_idx:
                        print(f"{idx + 1}. {char['name']}")
                defender_idx = int(input("Enter defender number: ")) - 1

                attack(characters[attacker_idx], characters[defender_idx])

                if characters[defender_idx]["health"] == 0:
                    print(f"{characters[defender_idx]['name']} has been removed from the game.")
                    characters.pop(defender_idx)
        elif choice == "4":
            if not characters:
                print("No characters to heal.")
            else:
                print("Choose a character to heal:")
                for idx, char in enumerate(characters):
                    print(f"{idx + 1}. {char['name']}")
                char_idx = int(input("Enter character number: ")) - 1
                heal(characters[char_idx])
        elif choice == "5":
            print("Exiting game. Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

# Call the main function to start the game
main()
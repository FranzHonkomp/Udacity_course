# Import Libs
import time
import random

#  Setup Lists
enemies = ["Butt Bowser", "Army Archer", "Flex Falcon", "Dusty Duster"]
weapons = ["pencil", "piece of wood", "firelighter", "sword"]


#  Define Function Blocks
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def start_game():
    weapon = "dagger"
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a 'dragon' is somewhere around"
                " here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not"
                " very effective) dagger.")
    first_question(weapon)


def take_new_weapon(weapon, weapon2):
    print_pause(f"Do you want to take the {weapon2} with you (1) or"
                f" discard this item and stay with the {weapon} (2)?")
    decision = check_input("(Please enter 1 or 2.)\n")
    if decision == "1":
        weapon = weapon2
    return weapon


def check_input(prompt):
    decision = input(prompt)
    while decision != "1" and decision != "2":
        decision = input(prompt)
    return decision


def first_question(weapon):
    print_pause("\nEnter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    decision = check_input("(Please enter 1 or 2.)\n")
    if decision == "1":
        house(weapon)
    elif decision == "2":
        carve(weapon)


def go_back(weapon):
    print_pause("You walk back out to the field.")
    first_question(weapon)


def fight_question(weapon, enemy):
    decision = check_input("Would you like to (1) fight or (2) run away?\n")
    if decision == "1":
        if weapon != "sword":
            print_pause("You do your best...")
            print_pause(f"but your {weapon} is no match for the {enemy}.")
            print_pause("You have been defeated!")
            repeat_game()
        if weapon == "sword":
            print_pause(f"As the {enemy} moves to attack, you unsheath your"
                        f" {weapon}.")
            print_pause(f"The {weapon} shines brightly in your hand as you"
                        " brace yourself for the attack.")
            print_pause(f"But the {enemy} takes one look at your shiny new "
                        "toy and runs away.")
            print_pause(f"You have rid the town of the {enemy}. You are vict"
                        "orious!")
            repeat_game()
    elif decision == "2":
        print_pause("You run back into the field. Luckily, you don't seem to "
                    "have been followed.")
        first_question(weapon)


def house(weapon):
    enemy = random.choice(enemies)
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens an out steps a "
                f"{enemy}.")
    print_pause(f"Eap! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    if weapon == "dagger":
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.")
        fight_question(weapon, enemy)
    elif weapon != "dagger":
        fight_question(weapon, enemy)


def carve(weapon):
    print_pause("You peer cautiously into the cave.")
    print_pause("It's seems to be a place of magic.")
    if weapon == "dagger":
        weapon = random.choice(weapons)
        print_pause("Your eye catches a glint of strongness behind a rock.")
        print_pause(f"You have found the magical {weapon}!")
        print_pause(f"You discard your silly old dagger and take the {weapon} "
                    "with you.")
        go_back(weapon)
    else:
        weapon2 = random.choice(weapons)
        print_pause("You have been here before, but let's see if there is some"
                    "thing more powerful in.")
        print_pause(f"You have found the magical {weapon2}!")
        weapon = take_new_weapon(weapon, weapon2)
        go_back(weapon)


def repeat_game():
    repeat = input("\nWould you like to play again? (y/n)\n")
    if repeat == "y":
        print_pause("Excellent! Restarting the game ...")
        start_game()
    elif repeat != "n":
        repeat_game()


# Start game
start_game()

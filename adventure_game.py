import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(name, item):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {name} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger.")
    print_pause("")


def house(name, item):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the"
                "door opens and out steps a {name}.")
    print_pause(f"Eep! This is the {name}'s house!")
    print_pause(f"The {name} attacks you!")
    print_pause("You feel a bit under-prepared for this, "
                "what with only having a tiny dagger.")


def cave(name, item):
    print_pause("You peer cautiously into the cave.")
    if "sword" in item:
        print_pause("You've been here before, "
                    "and gotten all the good stuff."
                    "It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    "and take the sword with you.")
        item.append("sword")
    print_pause("You walk back out to the field.")
    print_pause("")
    house_or_cave(name, item)


def fight(name, item):
    if "sword" in item:
        print_pause(f"As the {name} moves to attack, "
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause(f"But the {name} takes one look at "
                    "your shiny new toy and runs away!")
        print_pause(f"You have rid the town of the {name}. "
                    "You are victorious!")
        print_pause("")
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {name}.")
        print_pause("You have been defeated!")
        print_pause("")


def field():
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.")
    print_pause("")


def play_again(name, item):
    response = input("Would you like to play again? (y/n)")
    if response == "y":
        print_pause("Excellent! Restarting the game ...")
        adventure_game()
    elif response == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again(name, item)


def fight_or_run_away(name, item):
    response = input("Would you like to (1) fight or (2) run away?")
    if response == "1":
        fight(name, item)
        play_again(name, item)
    elif response == "2":
        field()
        house_or_cave(name, item)
    else:
        fight_or_run_away(name, item)


def house_or_cave(name, item):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    response = input("What would you like to do?\n(Please enter 1 or 2.)\n")
    if response == "1":
        house(name, item)
        fight_or_run_away(name, item)
    elif response == "2":
        cave(name, item)
    else:
        house_or_cave(name, item)


def adventure_game():
    item = []
    owners = ["pirate", "dragon", "wicked fairie", "troll"]
    name = random.choice(owners)
    intro(name, item)
    house_or_cave(name, item)


adventure_game()

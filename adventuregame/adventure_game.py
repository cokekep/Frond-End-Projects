import time
import random


enemies = ["wicked fairie", "troll", "pirate", "dragon", "gorgon"]


def print_pause(message):
    print(message)
    time.sleep(1)


def field():
    print_pause("You find yourself standing in an open field, filled with"
                " grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, and"
                " has been terrifying the nearby village")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def enter():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do")


def house():
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out steps"
                f" a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and take the"
                " sword with you.")
    print_pause("You walk back out to the field.")


def attack():
    print_pause(f"As the {enemy} moves to attack, you unsheath"
                " your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your hand as you "
                "brace yourself for the attack.")
    print_pause(f"But the {enemy} takes one look at your shiny"
                " new toy and runs away!")
    print_pause(f"You have rid the town of the {enemy}. You are victorious!")


def again():
    while True:
        play_again = input("Would you like to play again? (y/n)").lower()
        if play_again == 'y':
            print_pause("Excellent! Restarting the game . . .")
            break
        elif play_again == 'n':
            print_pause("Thanks for playing! See you next time.")
            exit(0)
        else:
            print_pause("Invalid entry")


while True:
    count = []
    enemy = random.choice(enemies)
    field()
    while True:
        enter()
        response = input("(Please enter 1 or 2.)\n")
        if response == '1':
            house()
            if (response == '1' and count == []):
                # I created a list here using the count variable which
                # gets appended only when the
                # player peers into the cave. if this list is empty,
                # it means the palyer has not been to the cave and hence
                # the enemy defeats the player
                print_pause("You feel a bit under-prepared for this,"
                            " with only having a tiny dagger.")

                while True:
                    resp = input("would you like to (1) fight or (2) "
                                 "run away?\n")
                    if resp == '1':
                        print_pause("You do your best....")
                        print_pause(f"but your dagger is no match for "
                                    f"the {enemy}.")
                        print_pause("You have been defeated")
                        print_pause(f"*** The {enemy} won you ***")
                        break
                    elif resp == '1':
                        print_pause("You run back into the field. Luckily, you"
                                    " don't seem to have been followed.")
                        break
                    else:
                        print_pause("invalid input")

                again()

            elif (response == '1' and count != []):
                attack()
                if count != []:
                    print_pause(f"*** You won the {enemy} ***")
                again()
        elif response == '2':
            if count == []:
                cave()
                count.append("sword")
            # once the player visits the cave, the list is appended.
            # It serves two purposes.
            # The first one is to let the player defeat if this list is
            # not empty and to let the code in the else block below
            # run to indicate
            # the cave has been visited before
            else:
                print_pause("You peer cautiously into the cave.")
                print_pause("You've been here before, and gotten all"
                            " the good stuff. It's just an empty cave now.")
                print_pause("You walk back out to the field.\n")

        else:
            print_pause("Invalid input")
        break

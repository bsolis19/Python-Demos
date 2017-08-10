# This program gives the player 30 points to spend on 4 attributes:
# strength, health, wisdom, and dexterity. The player
# can also remove points from an attribute back into the pool

# The program shows how to implement dictionaries
pointsAvailable = 30
character = {"Strength": 0, "Health": 0, "Wisdom": 0, "Dexterity": 0}
title = "welcome to character creator!"

print("\t\t" + title.title() + "\n")
print("You have ", pointsAvailable, end=" points available. ")
print("Here are the points for each attribute:\n")
for attr in character:
    print(attr + ": " + str(character.get(attr)))
print()
choice = None
while choice != "0":
    print("You have ", pointsAvailable, end=" points available.")
    print("""
            0 - Quit
            1 - View Attributes
            2 - Add Points to an Attribute
            3 - Remove Points from an Attribute

    """)
    choice = input("Choice: ")
    print()

    if choice == "0":
        print("Good-Bye")
    elif choice == "1":
        print("Here are the points for each attribute:\n")
        for attr in character:
            print(attr + ": " + str(character.get(attr)))
        print()
    elif choice == "2":
        attr = input("What attribute do you want to add to?: ")
        points = input("How many points would you like to add?: ")
        character[attr] += int(points)
        pointsAvailable -= int(points)

    elif choice == "3":
        attr = input("What attribute do you want to remove points from?: ")
        points = input("How many points would you like to remove?: ")
        character[attr] -= int(points)
        pointsAvailable += int(points)
    else:
        print("Sorry, that choice is invalid")

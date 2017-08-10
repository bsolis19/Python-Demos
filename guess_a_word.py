# This game is played by allowing
# the user to guess a random word
# The computer is responsible for
# telling the user how many letters
# are in the word, then the user
# must guess the word within 5
# hints. The hints are the 5 chances
# the user gets to ask if a letter
# is in the word

# The program demonstrates how to implement tuples

import random

words = ("hi", "bye", "arrivederci", "italy")

title = "welcome to guess a word!"
print("\t\t" + title.title() + "\n")
print("Please fill in the blank to guess a letter.")

i = random.randint(0, 3)

word = words[i]

chances = 5

while chances:
    temp = input("The letter _ is in the word?: ")
    if temp.lower() in word.lower():
        print("yes")
    else:
        print("no")
    chances -= 1

guess = input("Ok, now guess the word: ");

if guess.lower() == word.lower():
    print("Congratulations, you guessed correctly!")
else:
    print("Sorry, but the word is " + word + ".")

input("\n\nPress the enter key to exit.")



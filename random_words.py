# This program is used to print a list of words in random order

# This demonstrates the use of lists
import random

title = "welcome to the random word chooser!"
print("\t\t" + title.title() + "\n")

words = ["hi", "bye", "arrivederci", "python"]

size = len(words)

while size:
    print(words.pop(random.randint(0, size - 1)))
    size -= 1
input("\n\nPress the enter key to exit.")


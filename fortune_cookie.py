#This program emulates a fortune cookie with 5 possible statements.

#This show the use of control flow clauses as the if elif and else
import random

title = "\t\twelcome to the fortune cookie teller!"
print(title.title())

rand = random.randint(1, 5)
msg1 = "a friend will reunite with you"
msg2 = "you are admired by someone"
msg3 = "finances are your strength"
msg4 = "your gentleness will take you far"
msg5 = "your needs will be met"
print()
if rand == 1:
    print(msg1.title())
elif rand == 2:
    print(msg2.title())
elif rand == 3:
    print(msg3.title())
elif rand == 4:
    print(msg4.title())
elif rand == 5:
    print(msg5.title())
else:
    print("True love awaits")
input("\n\nPlease press the enter key to exit.")

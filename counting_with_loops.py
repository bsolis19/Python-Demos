# This program counts according to the user's input

# The program demonstrates how to implement for-loops



# Print out a welcome message
message = "welcome to counting with loops"
print("\t\t" + message.title() + "\n")

# Prompt the user for input
start = input("Please enter a starting number: ")
end = input("Now enter the ending number: ")
factor = input("Lastly, enter the amount by which to count: ")

# Work with the input
for i in range(int(start), int(end) + 1, int(factor)):
    # Show the counting results
    print(i, end=" ")

input("\n\nPress the enter key to exit.")

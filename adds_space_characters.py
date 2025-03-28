#Prog06:Create a program that adds space characters at
#the end of the string without using the .ljust() function

# Function to left-justify the string by padding spaces on the right
def left_justify(string, width):
    # Add spaces to the right of the string to match the desired width
    return string + ' ' * (width - len(string))

# Get user input (the string to justify)
user_input = input("Enter a string: ")
# Get user input (the width for the left-justified string)
width = int(input("Enter the width for left-justification: "))
# Print the string after left-justifying it
print("Left-justified string:", left_justify(user_input, width))
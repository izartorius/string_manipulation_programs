#Prog07: Create a program that adds space characters
#in the left and rightmost part of the string so that the
#string is printed in the center without using the
#center() function

# Function to center the string by adding spaces before and after
def center_string(string, width):
    # Calculate the total padding needed
    total_padding = width - len(string)
    # Calculate how much padding goes to the left side
    left_padding = total_padding // 2
    # The rest of the padding goes to the right side
    right_padding = total_padding - left_padding
    # Return the string centered with the appropriate amount of padding
    return ' ' * left_padding + string + ' ' * right_padding

# Get user input (the string to center)
user_input = input("Enter a string: ")
# Get user input (the width for centering the string)
width = int(input("Enter the width for centering: "))
# Print the centered string
print("Centered string:", center_string(user_input, width))
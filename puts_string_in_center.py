#Prog07: Create a program that adds space characters
#in the left and rightmost part of the string so that the
#string is printed in the center

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


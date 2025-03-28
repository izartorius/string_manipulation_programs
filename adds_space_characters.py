#Prog06:Create a program that adds space characters at
#the end of the string without using the .ljust() function

# Function to left-justify the string by padding spaces on the right
def left_justify(string, width):
    # Add spaces to the right of the string to match the desired width
    return string + ' ' * (width - len(string))


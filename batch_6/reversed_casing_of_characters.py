#Prog08: Create a program that reverses the current cases
#of characters in the given string without using the
#.swapcase() function

# Function to swap the case of each character in the string
def swap_case(string):
    # Use list comprehension to swap the case of each character
    return ''.join([char.lower() if 'A' <= char <= 'Z' else char.upper() for char in string])

# Get user input (string to swap case)
user_input = input("Enter a string to swap its case: ")
# Print the string with swapped case
print("String with swapped case:", swap_case(user_input))

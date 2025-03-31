#Prog04: Create a program that checks if
#characters are in lowercase without using
#the islower() function.

def check_if_all_lowercase(input_string):
    # Loop through each character in the string
    for char in input_string:
        # If a character is not a lowercase letter (e.g., it's uppercase or not alphabetic)
        if not ('a' <= char <= 'z'):
            # Return False if any character is not lowercase
            return False
    # If all characters are lowercase, return True
    return True


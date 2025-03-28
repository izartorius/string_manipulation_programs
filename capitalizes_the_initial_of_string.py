#Prog09: Creates a program that will capitalize the initial
#of the given string without using the .capitalize() function

# Function to capitalize the first letter of the string
def capitalize_first(string):
    # If the string is not empty, capitalize the first letter and lowercase the rest
    if string:
        return string[0].upper() + string[1:].lower()
    return string


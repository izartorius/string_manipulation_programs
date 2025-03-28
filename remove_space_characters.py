#Prog01: Create a program that features a function similar to .lstrip()
#without using the actual .lstrip() function

#Define function to remove leading spaces
def remove_leading_spaces(string):
    while string and string[0] == ' ': #Checks if the leading characters are space
        string = string[1:] #Removes the first character if it's a space
        # and continues to check until there are no more spaces
    return string #Returns the string without the leading spaces

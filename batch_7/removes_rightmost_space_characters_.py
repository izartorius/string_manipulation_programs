#Prog01: Create a program that removes space characters
#in the rightmost side of the string without using the
#rstrip function.

#Define function to remove spaces at the end
def remove_trailing_spaces(input_string):
    # Initialize an empty string to hold the new string without trailing spaces
    result = ""
    # Loop through the string from the end, ignoring spaces
    for i in range(len(input_string)-1, -1, -1):
        if input_string[i] != ' ':
            # If a non-space character is found, stop the loop
            result = input_string[:i+1]
            break
    return result



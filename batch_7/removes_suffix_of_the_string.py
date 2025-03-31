#Prog02: Create a program that removes the
#specified suffix of the word without using
#the removesuffix() function

#Define function to remove suffix of the string
def remove_suffix(input_string, suffix):
    # Check if the string ends with the specified suffix
    if input_string.endswith(suffix):
        # Return the string without the suffix
        return input_string[:-len(suffix)]
    return input_string



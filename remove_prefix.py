#Prog02: Create a program that removes the prefix of a string
#without using the .removeprefix() function

# Function to remove a specified prefix from the string
def remove_prefix(string, prefix):
    # Check if the string starts with the given prefix
    if string.startswith(prefix):
        # Remove the prefix by slicing the string from the length of the prefix onwards
        return string[len(prefix):]
    # If the string doesn't start with the prefix, return the string as is
    return string
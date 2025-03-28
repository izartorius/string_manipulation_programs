#Prog03: Create a program that converts all string characters
#to lowercase without using the .lower() function

#Define function to convert characters to lowercase
def to_lowercase(string):
    # Initialize an empty result string to store the final lowercase string
    result = ''

    # Iterate over each character in the string
    for char in string:
        # Check if the character is an uppercase letter (ASCII range 'A' to 'Z')
        if 'A' <= char <= 'Z':
            # Convert the character to lowercase by adding 32 to its ASCII value
            result += chr(ord(char) + 32)
        else:
            # If it's not an uppercase letter, add the character as is
            result += char

    # Return the resulting string after conversion
    return result

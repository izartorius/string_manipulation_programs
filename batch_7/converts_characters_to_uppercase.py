#Prog03: Create a program that converts the
#characters of the string to uppercase letters
#without the use of the upper() function.

def convert_to_uppercase(input_string):
    # Initialize an empty string to store the result
    result = ""

    # Loop through each character of the string
    for char in input_string:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase by adjusting its ASCII value
            result += chr(ord(char) - 32)
        else:
            # If the character is not lowercase, add it as is (e.g., upper case or non-alphabetic)
            result += char

    # Return the result with all characters in uppercase
    return result


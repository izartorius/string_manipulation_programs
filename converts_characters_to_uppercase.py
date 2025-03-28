#Prog04: Create a program that converts all string characters
#to uppercase without using the .isupper() function

# Function to check if all alphabetic characters in the string are uppercase
def is_all_uppercase(string):
    # Use all() to check if every letter in the string is uppercase
    return all('A' <= char <= 'Z' for char in string if char.isalpha())



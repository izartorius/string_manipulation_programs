#Prog05: Create a program that checks if
#the given string starts with the specified
#prefix without using the .startswith() function.

def check_starts_with(input_string, prefix):
    # Compare the beginning of the string with the prefix
    return input_string[:len(prefix)] == prefix

# Get user input for the main string
input_string = input("Enter a string: ")
# Get user input for the prefix to check
prefix = input("Enter prefix to check: ")
# Call the function and print the result
print(f"Starts with '{prefix}': {check_starts_with(input_string, prefix)}")
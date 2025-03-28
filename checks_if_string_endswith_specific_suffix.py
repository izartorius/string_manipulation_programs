#Prog05: Create a program that checks if a string ends with a specific suffix

# Function to check if the string ends with the given suffix
def ends_with(string, suffix):
    # Use slicing to check if the last part of the string matches the suffix
    return string[-len(suffix):] == suffix if len(suffix) <= len(string) else False


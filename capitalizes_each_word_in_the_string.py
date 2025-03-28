#Prog10: Create a program that converts all initials of each word
#in the given string into uppercase with the rest of the characters
#in lowercase without using the title() function

# Function to capitalize the first letter of each word in the string
def title_case(string):
    # Split the string into words, then capitalize each word and join them back together
    words = string.split()
    return ' '.join([word[0].upper() + word[1:].lower() if word else '' for word in words])


# Prog06: Create a program that adds space
# characters to the rightmost part of the
# given string without using the rstrip() function

# Get user input
text = input("Enter a string: ")
width = int(input("Enter total width: "))
# Calculate needed spaces and prepend them
rjust_text = " " * (width - len(text)) + text
print("rjust() equivalent:", rjust_text)
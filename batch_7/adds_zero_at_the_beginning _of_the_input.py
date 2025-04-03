#Prog07: Create a program that adds zeroes
#to the beginning of the string to complete
#the number of characters specified without
#the use of zfill() function.

# Get user input
text = input("Enter a string: ")
width = int(input("Enter total width: "))
# Calculate needed zeros and prepend them
zfill_text = "0" * (width - len(text)) + text
print("zfill() equivalent:", zfill_text)

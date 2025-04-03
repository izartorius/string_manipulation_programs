#Prog09: Create a program that returns the
#location of the specified character without
#the use of the index() function.

# Get user input
text = input("Enter a string: ")
substring = input("Enter substring to find: ")
found = False
# Loop through the string to find the first occurrence
for i in range(len(text) - len(substring) + 1):
    if text[i:i+len(substring)] == substring:
        print("index() equivalent:", i)
        found = True
        break
if not found:
    print("Substring not found")
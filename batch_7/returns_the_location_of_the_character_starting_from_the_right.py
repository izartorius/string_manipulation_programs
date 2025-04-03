#Prog10: Create a program that returns the
#location of the specified character starting
#from the rightmost part of the string without
#the use of the rindex() function.

# Get user input
text = input("Enter a string: ")
substring = input("Enter substring to find from right: ")
found = False
# Loop through the string in reverse to find the last occurrence
for i in range(len(text) - len(substring), -1, -1):
    if text[i:i+len(substring)] == substring:
        print("rindex() equivalent:", i)
        found = True
        break
if not found:
    print("Substring not found")
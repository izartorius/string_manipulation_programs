#Prog08: Create a program that counts the frequency
#of a certain character in the given input without
#the use of the count() function.

#Get user input
text = input("Enter a string: ")
substring = input("Enter substring to count: ")
count = 0 #Empty variable list to store the
# count of the specified characters

# Loop through the string and count occurrences of substring
for i in range(len(text) - len(substring) + 1):
    if text[i:i+len(substring)] == substring:
        count += 1
print("count() equivalent:", count)
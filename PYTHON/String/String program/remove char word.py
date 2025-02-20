# Write a program to remove a character or word from string accepted by the user.

string1 = input("Enter a string: ")
remove = input("Enter a character or word to remove: ")

string2 = string1.replace(remove,'')

print(string2)
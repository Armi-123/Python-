# Program to remove leading and trailing spaces and replace spaces with underscores.


input_string = input("Enter a string: ")

string1 = input_string.strip()


string2 = string1.replace(" ", "_")
print("Formatted string:", string2)

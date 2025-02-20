# Find the character with mentioned index of a the string accepted by the user.

 
input_string = input("Enter a string: ")

index = int(input("Enter the index to find the character: "))


if 0 <= index < len(input_string):
    character_at_index = input_string[index]
    print(character_at_index)
else:
    print("Invalid index, Please enter a valid index.")

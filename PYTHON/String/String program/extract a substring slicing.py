# Write a program to reverse a string accepted by the user.

input_string = input("Enter a string: ")

start_index = int(input("Enter the starting index: "))
end_index = int(input("Enter the ending index: "))

substring = input_string[start_index:end_index]
print(substring)

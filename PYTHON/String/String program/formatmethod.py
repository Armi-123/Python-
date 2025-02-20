# Write a program to format a string using the format() method.

name = input("Enter your name: ")
age = int(input("Enter your age: "))


format = "Hello, {}!! You are {} years old.".format(name, age)
print(format)
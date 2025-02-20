# Check whether the entered string is palindrome or not.

string = input("Enter a string: ")

if string == string[::-1]:
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
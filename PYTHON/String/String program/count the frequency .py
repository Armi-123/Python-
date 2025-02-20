# Accept the string from the user and count the frequency of it.


user_input = input("Enter a string: ")
char_frequency = {}

for char in user_input:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

for char, frequency in char_frequency.items():
    # print(f"The character '{char}' appears {frequency} times in the string.")
    print(char,frequency)
# Write a program to display the words from the given string which are starting with the alphabet "i" or "I".

input_string = "I have an interesting idea to implement in my project."

words = input_string.split()

selected_words = [word for word in words if word.startswith('i') or word.startswith('I')]

print("Original string:", input_string)
print("Words starting with 'i' or 'I':", selected_words)

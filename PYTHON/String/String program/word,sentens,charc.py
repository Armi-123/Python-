#Write a program that analyzes a text document, counting the number of words, sentences, and characters without using functions.

text=input("Enter text document:")

doc_word=text.split(".")
word=text.count(".")

len_char=text.count("")

sentences=text.count(".") + text.count(",") + text.count("?")

print("word length:",doc_word)
print("word:",word)
print("sentences:",sentences)
print("length character:",len_char)

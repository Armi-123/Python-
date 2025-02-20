# Write a program to check two words are anagrams or not(ignore letter casing.print)

word1 = "night"
word2 = "thing"

if (sorted(word1) == sorted(word2)):
    print("Anagrams")
else:
    print("Not anagrams")

# Count the frequency of each vowels in the given string.

input_string = "Hello, how are you doing?"
input_string_lower = input_string.lower()

count_a = count_e = count_i = count_o = count_u = 0

for char in input_string_lower:
    if char == 'a':
        count_a += 1
    elif char == 'e':
        count_e += 1
    elif char == 'i':
        count_i += 1
    elif char == 'o':
        count_o += 1
    elif char == 'u':
        count_u += 1

print("Original string:", input_string)
print("Frequency of 'a':", count_a)
print("Frequency of 'e':", count_e)
print("Frequency of 'i':", count_i)
print("Frequency of 'o':", count_o)
print("Frequency of 'u':", count_u)
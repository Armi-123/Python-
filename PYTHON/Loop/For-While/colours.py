# "Take a list of atleast 7 colours and print them like this :
# Blue
# B
# L
# U
# E"


# for loop
colors = ["Red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for color in colors:
    print(color)
    for letter in color:
        print(letter)

# while loop      
colors = ["Red", "orange", "yellow", "green", "blue", "indigo", "violet"]
index = 0

while index < len(colors):
    color = colors[index]
    print(color)

    letter_index = 0
    while letter_index < len(color):
        print(color[letter_index])
        letter_index += 1
    print()
    index += 1

# Take 1-100 numbers and Find the all numbers which are divisible by 5 and increase by 5 then print the all numbrs

# for loop
for number in range(1, 101):
    if number % 5 == 0:
        result = number + 5
        print(result)


# while loop
number = 1

while number <= 100:
    if number % 5 == 0:
        result = number + 5
        print(result)
    number += 1
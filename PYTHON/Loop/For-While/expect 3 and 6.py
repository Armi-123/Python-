# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

# for loop
for number in range(7):
    if number == 3 or number == 6:
        continue
    print(number)


for num in range(7):
    if num != 3 and num != 6:
        print(num)



# while loop
    
number = 0
while number <= 6:
    if number != 3 and number != 6:
        print(number)
    number += 1


num = 0
while num <= 6:
    if num == 3 or num == 6:
        num += 1
        continue
    print(num)
    num += 1

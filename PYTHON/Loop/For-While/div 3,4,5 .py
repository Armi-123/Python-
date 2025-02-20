#  Take a 1-100 numbers and the number which is divisable by 3,4,5 print all numbers in diffrent list

divisible_by_3 = []
divisible_by_4 = []
divisible_by_5 = []

for number in range(1, 101):
    if number % 3 == 0:
        divisible_by_3.append(number)
    if number % 4 == 0:
        divisible_by_4.append(number)
    if number % 5 == 0:
        divisible_by_5.append(number)

print("Numbers divisible by 3:", divisible_by_3)
print("Numbers divisible by 4:", divisible_by_4)
print("Numbers divisible by 5:", divisible_by_5)

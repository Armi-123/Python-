
list1 = []
list2 = []
list3 = []

for number in range(1,101):
    if number % 3 == 0:
        list1.append(number)

    if number % 4 == 0:
        list2.append(number)

    if number % 5 == 0:
        list3.append(number)

print(list1)
print(list2)
print(list3)
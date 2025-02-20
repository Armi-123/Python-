# Find minimum number of list Without using inbuilt methods

number_list = [23, 56, 12, 78, 45, 92, 37]
min_number=number_list[0]

for number in number_list:
        if number < min_number:
            min_number = number

print("List:", number_list)
print("Minimum number:", min_number)
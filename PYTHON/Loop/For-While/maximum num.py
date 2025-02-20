# Find maximum number of list Without using inbuilt method


number_list = [23, 56, 12, 78, 45, 92, 37]
max_number=0

for number in number_list:
    if number > max_number:
        max_number = number

print("List:", number_list)
print("Maximum number:", max_number)
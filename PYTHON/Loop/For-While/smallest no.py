# write a program to smallest number in a list..
# my_list=[34,56,12,89,7,42]

my_list=[34,56,12,89,7,42]
min_number=my_list[0]

for number in my_list:
        if number < min_number:
            min_number = number

print("List:", my_list)
print("Minimum number:", min_number)
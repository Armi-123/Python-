# list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]] remove duplicates from this list

original_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
unique_list = []

for inner_list in original_list:
    if inner_list not in unique_list:
        unique_list.append(inner_list)

print("Original List:", original_list)
print("List after removing duplicates:", unique_list)

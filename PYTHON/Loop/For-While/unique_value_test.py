# unique value print in list

list=[1,2,3,4,5,2,3,6,7,5]

# remove duplicates from this list
orignal_list=[1,2,3,4,5,2,3,6,7,5]
unique_list=[]

for i in orignal_list:
    if i not in unique_list:
        unique_list.append(i)

print("orignal list:",orignal_list)
print("unique list:",unique_list)


# only unique remove all duplicate value
for i in range(len(list)):
    if list.count(list[i]) == 1:
        print(list[i])

# 2 list compare define unique list

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[6,7,8,9,10,11,12,13,14,15]

combined_list = list1 + list2
unique_list = []

for i in combined_list:
    if i not in unique_list:
        unique_list.append(i)
print("unique list: ",unique_list)


# unique list without not in , use flag
list1=[1,2,3,4,5,3,6,7,8,1]
unique_list=[]
duplicate_list=[]
flag=True

for i in range(len(list1)):
    flag=True
    for j in range(len(unique_list)):
        if unique_list[j] == list1[i]:
            flag=False
            duplicate_list.append(list1[i])
    if flag:
        unique_list.append(list1[i])

print("Duplicate list:",duplicate_list)
print("Unique list:",unique_list)
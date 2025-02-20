# 2 list compare define duplicate list

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[6,7,8,9,10,11,12,13,14,15]
duplicate=[ ]


for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            duplicate.append(list2[j])        
print(duplicate)

# minimum value in list

list=[10,67,4,20,60]
min_num=list[0]

for i in list:
    if i < min_num:
        min_num=i
       
print("minimum value in list:",min_num)
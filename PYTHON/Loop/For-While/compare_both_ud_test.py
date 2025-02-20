# compare 2 list print unique and duplicate

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[6,7,8,9,10,11,12,13,14,15]

a=list1+list2
# 1,2,3,4,5,6,7,8,9,10,6,7,8,9,10,11,12,13,14,15

min_num=a[0]
for i in range(len(a)):
    for j in (i+1,len(a)):
        if j < min_num:
            min_num = j
    print()
    
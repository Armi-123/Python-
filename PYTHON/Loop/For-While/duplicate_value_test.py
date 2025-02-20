# print duplicate value in list

# list=[1,2,3,4,2,3,5,6,7,4,8,9]

orignal_list=[1,2,3,4,2,3,5,6,7,4,8,9]
duplicate_list=[]

for i in range(len(orignal_list)):
    for j in range(i+1,len(orignal_list)):
        if orignal_list[i]==orignal_list[j]:
            duplicate_list.append(orignal_list[i])


print("orignal list:",orignal_list)
print("duplicate list:",duplicate_list)
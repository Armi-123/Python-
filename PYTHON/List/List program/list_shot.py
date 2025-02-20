# myArr = [1,5,2,3,10,6,20,7] Shot this list
# All program do without using inbuilt method
myArr=[1,5,2,3,10,6,20,7]

# short,incresing
for i in range(len(myArr)):
    for j in range(len(myArr)-i-1):
        if myArr[j] > myArr[j+1]:
            myArr[j], myArr[j + 1] = myArr[j + 1], myArr[j]
print("incresing order:", myArr)

# decresing
for i in range(len(myArr)):
    for j in range(len(myArr)-i-1):
        if myArr[j] < myArr[j+1]:
            myArr[j],myArr[j+1]=myArr[j+1],myArr[j]
print("decresing order:", myArr)
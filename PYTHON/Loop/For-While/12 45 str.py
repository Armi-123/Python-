# "Write a Python program to extract numbers from a given string.           
# Sample Output:
# Original string: red 12 black 45 green
# Extract numbers from the said string: [12, 45]"

numList=[]
string="red 12 black 45 green"
list1=string.split()
print(list1)

newList=list1[1::2]
print(newList)

for i in newList:
    numList.append(int(i))
print("Extract numbers from the said string:",numList)

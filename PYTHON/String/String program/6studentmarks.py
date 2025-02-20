# Write a program to accept marks of 6 students and display them in a sorted manner.

a=(input("enter first student marks: "))
b=(input("enter second student marks: "))
c=(input("enter third student marks: "))
d=(input("enter fourth student marks: "))
e=(input("enter fifth student marks: "))
f=(input("enter sixth student marks: "))


sortedmarks=[a,b,c,d,e,f]
sortedmarks.sort()
print(sortedmarks)
print("first student marks: ",sortedmarks[0])
print("second student marks: ",sortedmarks[1])
print("third student marks: ",sortedmarks[2])
print("fourth student marks: ",sortedmarks[3])
print("fifth student marks: ",sortedmarks[4])
print("sixth student marks: ",sortedmarks[5])

d = [a,b,c,d,e,f]
print(d.sort())
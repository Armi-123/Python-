# list2 = []
list = [[[1,2,3,4],[5,6,7],[[8,9,10],[20,21,21]]],[["Shakti","harsh"],["Prem","Smit","Kishan"]]]

# a1=[list[0][0][0]]
# print(a1)

# a2=[list[0][0][1]]
# print(a2)

# a3=[list[0][0][2]]
# print(a3)

# a4=[list[0][0][3]]
# print(a4)

# a=a1+a2+a3+a4
# print(a)
# print([sum(a)])

# b1=[list[0][1][0]]
# print(b1)

# b2=[list[0][1][1]]
# print(b2)

# b3=[list[0][1][2]]
# print(b3)

# b=b1+b2+b3
# print(b)
# print([sum(b)])

# c1=[list[0][2][0][0]]
# print(c1)

# c2=[list[0][2][0][1]]
# print(c2)

# c3=[list[0][2][0][2]]
# print(c3)

# c=c1+c2+c3
# print(c)
# print([sum(c)])

# d1=[list[0][2][1][0]]
# print(d1)

# d2=[list[0][2][1][1]]
# print(d2)

# d3=[list[0][2][1][2]]
# print(d3)

# d=d1+d2+d3
# print(d)
# print([sum(d)])

# list1=[["Shakti","harsh"],["Prem","Smit","Kishan"]]
# list2=["Shakti","harsh"]
# list3=["Prem","Smit","Kishan"]
# list2.extend(list3)
# print(list2)

# newList=['Shakti', 'harsh', 'Prem', 'Smit', 'Kishan']
# newList.insert(1,"Armi")
# newList.insert(5,"Radhika")
# newList.remove("Prem")
# newList.insert(-1,"Raju")
# newList.remove("Kishan")
# print(newList)

x=['Shakti', 'Armi', 'harsh', 'Smit', 'Radhika', 'Raju']
x[5], x[0], x[1], x[3], x[2], x[4]= x[0], x[4], x[3], x[2], x[1], x[5]
print(x)

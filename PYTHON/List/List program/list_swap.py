a = [1,2,3,5,7,8]
b = [4,5,6,5,6]
# Output : A=[ 4, 5, 6, 5, 6, 8]  B=[ 1, 2, 3, 5, 7, 'kishan' ]

# a.append("kishan") != b.append("kishan")
for i in range(len(a)):
    for j in range(len(b)):    
        if a[i]==b[j] and b[j]==a[i]:
            len(a) > len(b) and b.append("kishan")
            len(a) < len(b) and a.append("kishan")
print("A:",b)
print("B:",a)
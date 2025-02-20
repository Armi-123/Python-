a=[1,2,3,4,5,6,7,8,9,10]
b=[11,12,13,14,15,1,3,5]

print("a: ",a)
print("b: ",b)

# unique number
c=a+b
def list(x):
    u=[]
    for i in c:
        if i not in u:
            u.append(i)
    return u
print("unique: ",list(c))

# duplicate number
def z(x):
    d=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                d.append(b[j])
    return d
print("duplicate: ",z(c))
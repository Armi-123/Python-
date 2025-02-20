# 1 list duplicate number

def duplicate(x):
    a=[]
    for i in range(len(x)):
        for j in range(i):
            if (x[i]) == (x[j]):
                a.append(x[j])
    return a

print("duplicate list: ",duplicate([1,2,3,4,5,3,2,7,4]))
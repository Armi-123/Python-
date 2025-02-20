def unique(x):
    a=[]
    for i in x:
        if i not in a:
            a.append(i)
    return a
print("unique list: ",unique([1,2,3,4,5,3,2,7,4]))
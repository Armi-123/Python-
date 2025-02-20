x=str(input("Enter the value: "))
c=x.split(",")
x=0

def abc(c):
    a=[]  
    for i in (c):
        num = str(i)
        reverse = num[ : :-1]
        palindrome = num == reverse
        a.append([i,palindrome])
    return a   
print(abc(c))
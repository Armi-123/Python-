# armstrong number

n = (input("Enter the value: "))

def arm(n):
    sum = 0
    for i in n:
        sum = sum + int(i)**len(n)
    if int(n) == sum:
        print(n, "is an Armstrong number")
    else:
        print(n, "is not an Armstrong number")
    return sum
print(arm(n))
# Display that the given number is 3 digit number or not and also displat the second/middle number

user = int(input("enter the 3 digit value = "))

if 100 <= user and user <= 999 :
    print("your second number is:", user % 100 // 10)
else :
    print("enter courect value")
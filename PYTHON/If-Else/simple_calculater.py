# simple calculater

first=int(input("Enter first value: "))
operater=input("Enter operater (+,-,*,/,%): ")
second=int(input("Enter second value: "))

if operater == "+":
    print(first+second)
elif operater == "-":
    print(first-second)
elif operater == "*":
    print(first*second)
elif operater == "/":
    print(first/second)
elif operater == "%":
    print(first%second)
else:
    print("invalid process")
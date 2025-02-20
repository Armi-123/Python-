#Grade Calculator:

sub1 = int(input("enter the sub1 marks is:"))
sub2 = int(input("enter the sub2 marks is:"))
sub3 = int(input("enter the sub3 marks is:"))
sub4 = int(input("enter the sub4 marks is:"))
sub5 = int(input("enter the sub5 marks is:"))

total = sub1+sub2+sub3+sub4+sub5
avg = total / 5
print("ave: ",avg)

if avg>= 91 and avg<= 100:
    print("grade A+")

elif avg>= 81 and avg<= 90:
    print("grade A")   

elif avg>= 71 and avg<= 80:
    print("grade B") 

elif avg>= 61 and avg<= 70:
    print("grade C") 

elif avg>= 51 and avg<= 60:
    print("grade D")

elif avg>= 41 and avg<= 50:
    print("grade E")

elif avg<= 40:
    print("Fail")
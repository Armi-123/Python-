print("Adidas = a")
print("Skechers = s")
print("Nike = n")

# menu selection
user = input("Enter You  favorite Brand:")

Adidas = "a"
Skechers = "s"
Nike = "n"

if user == Adidas:
    print("T = tshirt ,","Z = Shoes,","P = pent")
elif user == Skechers:
    print("J = jeanspent,","W = watch,","S = snikers")
elif user == Nike:
    print("S = shoes,","B = belt,","N = Shocks")

# items selecion
select = input("Enter your choice : ")

tshirt = "T"
Shoes = "Z"
pent = "P"

jeanspent = "J"
watch = "W"
snikers = "S"

shoes = "S"
belt = "B"
Shocks = "N" 

if select == tshirt:
    print("price = ",5500)
elif select == Shoes:
    print("price = ",500)
elif select == pent:
    print("price = ",2000)

elif select == jeanspent:
    print("price = ",1500)
elif select == watch:
    print("price = ",5000)
elif select == snikers:
    print("price = ",8000)
    
elif select == shoes:
    print("price = ",2500)
elif select == belt:
    print("price = ",800)
elif select == Shocks:
    print("price = ",200)
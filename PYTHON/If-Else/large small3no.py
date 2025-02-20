# Display the largest and smallest value from 3  values.

value1 = int(input("Enter the value 1: "))
value2 = int(input("Enter the value 2: "))
value3 = int(input("Enter the value 3: "))

# smallest value
if value1 <= value2 and value1 <= value3 :
    print("value1 smallest")    

elif value2 <= value1 and value2 <= value3:
    print("value2 smallest")   

else:
    print("value3 smallest")

# largest value
if value1 >= value2 and value1 >= value3 :
    print("value1 largest")    

elif value2 >= value1 and value2 >= value3:
    print("value2 largest")   

else:
    print("value3 largest")    


# if value2 >= value1 <= value3 or value3 <= value1 >= value2 :
#     print("value1 is small")

# if value1 >= value2 <= value3 or value3 <= value2 >= value1:
#     print("value2 is large")

# if value1 >= value3 <= value2 or value1 <= value3 >= value2:
#     print("value3 is small or large")

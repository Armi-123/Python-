#  Write a program to accept a number from 1 to 7 and display the number of the day like 1 for sunday,2 for monday and so on.

day = int(input("Enter a number from 1 to 7: "))

if day == 1:
    print(day, "for Sunday")
elif day == 2:
    print(day, "for Monday")
elif day == 3:
    print(day, "for Tuesday")
elif day == 4:
    print(day, "for Wednesday")
elif day == 5:
    print(day, "for Thursday")
elif day == 6:
    print(day, "for Friday")
elif day == 7:
    print(day, "for Saturday")
else:
    print("Wrong input.. Please enter a number from 1 to 7.")
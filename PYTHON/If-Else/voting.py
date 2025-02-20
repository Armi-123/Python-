# Check for voting...
#   If the user's age is 18 or more ask for voting card and if he/she is not having it ask them for applying 
#   And if the user's age is less than 18 he is not eligible for vote

A = 18
age = int(input("enter your age = "))

if 18 <= age:
    print("you are elegabal pramot for voat")
    voterid = input("election card is avaiabal or not ? = ")

    if voterid == ("yes"):
        print("pls voat")
    else :
        print("apply for a election card pls")    
    
else :
    print("you are a not elegable for voat")
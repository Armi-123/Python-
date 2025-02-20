arr = [['ID', 'Name', 'Email', 'Phone number ', 'State', 'city', 'pincode'],
       [101, 'Smit', 'smit@gmail.com', 98958646, 'Gujarat', 'Ahmedabad', 379850],
       [102, 'Harsh', 'harsh@gmail.com', 76758575, 'Gujarat', 'Himatnagar', 383002],
       [103, 'Harsh', 'harsh@gmail.com', 76756777, 'MP', 'Goregao', 236562],
       [104, 'Kishan', 'kishan@gmail.com', 89767666, 'UP', 'Lakhnow', 767666],
       [105, 'Mukesh', 'mukesh@gmail.com', 87565454, 'Dehli', 'Est goregao', 235355]]

arr2 = [['Insert email '],['harsh@gmail.com'],['smit@gmail.com']]

# # user define
user=input(str("Insert email: "))
for i in (arr,user):
    for j in (arr):    
        if j[2]==user and i==arr:
            print(j)

# # specific
a=[]
c=[i[0] for i in arr2]
for i in arr:
    if i[2] in c:
        a.append(i)
print(a)
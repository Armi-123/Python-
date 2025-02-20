# write a python program to remove duplicate words from a given string.


str1 = "armi patel"
str2 = ""

for i in str1:
    if i not in str2:
        str2.join(i)

print("Original str:", str1)
print("str after removing duplicates:", str2)

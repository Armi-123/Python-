n = [155, 123, 121, 555, 876, 954, 891]
output = []

for i in n:
    num = str(i)
    reverse = num[::-1]
    palindrome = num == reverse
    output.append([i,palindrome])   
print(output)
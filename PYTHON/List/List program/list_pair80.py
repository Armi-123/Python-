# arr=[15,20,12,22,50,25,40,60,30]
# input=80
# Out put:-[ [ 20, 60 ], [ 50, 30 ] ]

arr = [15, 20, 12, 22, 50, 25, 40, 60, 30]
output = []

for i in range(len(arr)):
    for j in range(i):
        if arr[i] + arr[j] == 80:
            output.append([arr[i], arr[j]])
print(output)
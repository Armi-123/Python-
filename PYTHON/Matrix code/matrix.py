# sum of matrix

m = [
    [4,5,6],
    [1,2,3],
    [7,8,9]
]
# sum of row
r1=[m[0][0]+m[0][1]+m[0][2]]
r2=[m[1][0]+m[1][1]+m[1][2]]
r3=[m[2][0]+m[2][1]+m[2][2]]
print(r1+r2+r3)
print([sum(r1+r2+r3)])

# sum of coloms
c1=[m[0][0]+m[1][0]+m[2][0]]
c2=[m[0][1]+m[1][1]+m[2][1]]
c3=[m[0][2]+m[1][2]+m[2][2]]
print(c1+c2+c3)
print([sum(c1+c2+c3)])

# sum of daigonal
d1=[m[0][0]+m[1][1]+m[2][2]]
d2=[m[0][2]+m[1][1]+m[2][0]]
print(d1+d2)
print([sum(d1+d2)])
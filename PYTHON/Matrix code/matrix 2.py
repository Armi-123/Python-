# matrix = [
#    [[4,5,6],
#     [7,8,9],
#     [16,17,18]],
#     [[10,11,12],
#     [1,2,3],
#     [13,14,15]]
# ]
m = [
   [[4,5,6],
    [7,8,9],
    [16,17,18]],
    [[10,11,12],
    [1,2,3],
    [13,14,15]]
]

r1=[m[0][0][0]+m[0][0][1]+m[0][0][2]]
r2=[m[0][1][0]+m[0][1][1]+m[0][1][2]]
r3=[m[0][2][0]+m[0][2][1]+m[0][2][2]]
r4=[m[1][0][0]+m[1][0][1]+m[1][0][2]]
r5=[m[1][1][0]+m[1][1][1]+m[1][1][2]]
r6=[m[1][2][0]+m[1][2][1]+m[1][2][2]]
print(r1+r2+r3+r4+r5+r6)
print([sum(r1+r2+r3+r4+r5+r6)])

c1=[m[0][0][0]+m[0][1][0]+m[0][2][0]]
c2=[m[0][0][1]+m[0][1][1]+m[0][2][1]]
c3=[m[0][0][2]+m[0][1][2]+m[0][2][2]]
c4=[m[1][0][0]+m[1][1][0]+m[1][2][0]]
c5=[m[1][0][1]+m[1][1][1]+m[1][2][1]]
c6=[m[1][0][2]+m[1][1][2]+m[1][2][2]]
print(c1+c2+c3+c4+c5+c6)
print([sum(c1+c2+c3+c4+c5+c6)])
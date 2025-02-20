# arr = [['smit+jay-patel'], ['smit+jay-patel'], ['smit+jay-patel']];
# arr2 = [['smit'], ['jay-patel']];
# [ [ 'smit' ], [ 3 ], [ 'jay-patel' ], [ 3 ] ]

arr = [['smit+jay-patel'], ['smit+jay-patel'], ['smit+jay-patel'],['smit+jay-patel']]

smit=0
jay=0
for i in arr:
    smit+=i[0].count('smit')
    jay += i[0].count('jay-patel')
print([['smit'],[smit],['jay-patel'],[jay]])
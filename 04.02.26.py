#1
'''
def rec(a,b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / rec(a,-b)
    else:
     return a * rec(a,b-1)
print(rec(6,3))
'''

#2
'''
def rec(a):
    a = abs(a)
    if a == 0:
        return 0
    else:
        return a % 10 + rec(a //10 )
print(rec(189795))
'''

#3
'''
def rec(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        rec1 = rec(lst[1:])
        return lst[0] if lst[0] > lst[1] else rec1
print(rec([1,2,3,4,5,5253523]))
'''
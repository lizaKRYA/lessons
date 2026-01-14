#a = [[2,4,6],[8,10,12],[14,16,18]]
#b = False
#for values in a:
#    for i in values:
#        if i % 2!= 0:
#            b = True
#if not b:
#    print("da")
#else:
#    print("net")

#matrix = [[1,2,3],[4,0,6],[7,8,9]]
#b = []
#for i,values in enumerate(matrix):
#    z = i if 0 in values else ""
#    if z!= "":
#        print(z)
#        b.append(True)
#    else:
#        b.ppend(False)
#        print(all(b))
#[выражение for элемент in последовельность if условие]
#b = [i for i in range(5) if i % 2 == 0]
#print(b)

#nums = [1,2,3,4,5,-4, -1,-2,-3]
#a =[i**2 for i in nums if i > 0]
#print(a)
#b = []
#for i in range(10):
#    for j in range(10):
#        b.append(i*j)

#matrix= [[row * col for col in range(1,4)] for row in range(1,4) ]
#print(matrix)
#flateten_matrix = [item for row in matrix for item in row]

#dict_test = { i: i**2 for i in range(1,6)}
#print(dict_test)

#set_unique = [i for i in range(10)]
#print(set_unique)

#tuple_test = tuple(i for i in range(10))
#print(tuple_test)


#множество пар (x,y)где x y числв от 1 до 3
#pairs = {(x,y) for x in range(1,4) for y in range(1,4)}
#print(set(pairs))

#d = [ i**2 for i in range(1,16)]
#print(d)

#a = ["python", "java","c++","javascript","go"]
#c = [i.upper() for i in a ]
#print(c)

#temp = [0,15,20,25,30,-5,-10]
#temp_F = [i*9/5+32 for i in temp if i >= 0]
#print(temp_F)
""""
x = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
y = [i for row in x for i in row if i % 2 == 0 ]
print(y)
"""
""""
a = ["apple", "banana", "cherry","date","elderberry"]
my_dict ={ i: len(i) for i in a if len(i) >= 5}
print(my_dict)
"""
""""
a = ['привет мир!'," программирование","списочные включения"]
my_dict = {i: [len(i) for j in i.split()] for i in a}
print(my_dict)
"""

#a = {i: [j for j in range(1,i + 1) if i % j ==0] for i in range(1,6) }
#print(a)
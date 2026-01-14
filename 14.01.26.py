#1
"""""
a = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
b = True
for values in a:
    for i in values:
        if i % 2 != 0:
            b = False
print(b)
"""""
#2
""""
keys = ['name', 'age', 'city', 'profession']
values = ['Иван', 28, 'Москва', 'Программист']
d = dict(zip(keys, values))
for i, (key, value) in enumerate(d.items(), start=1):
    print(f"{i}. {key}: {value}")
"""

#3

#matrix = [[i + j *4 + 1 for j in range(4)] for i in range(4)]
#print(matrix)

#4

#a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#b = [i for j in a for i in j ]
#print(b)

#5

#names = ['Alice', 'Bob', 'Charlie']
#ages = [25, 30, 35]
#for name, age in zip(names, ages):
#    print(f"{name}: {age}")

#6

#a = [1, 2, 21, 37, 4, 42, 42, 5, 59, 6, 6, 7, 82, 94, 9, 10]
#b = [i for i in a if i % 2 != 0]
#print(set(b))


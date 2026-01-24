#1
'''
def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
        return result


nums = [2,3,4,5,6,7,8,9,10,11,12]
print(list(my_map(lambda x: x+5, nums)))
'''

#2
'''
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
sums1 = [a + b for a, b in zip(list1, list2)]
sums2 = [i for i in sums1 if i > 40]
print(sums2)
'''

#3
'''
nums = list(range(-10, 11))

s1 = [ i for i in nums if abs(i) > 3]
s2 = [i **2 for i in s1]
s3 = [i for i in s2 if i % 10 < 5]
print(s3[:5])
'''

#4
'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def func(num):
    return list(filter(lambda x: x % 2 == 0, num))

s1 = map(func, matrix)
sums = list(map(sum, s1))
print(sums)
'''
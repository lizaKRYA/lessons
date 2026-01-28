#1
'''
def make_stats_tracker():
    numbers = []
    total = 0
    def add(value):
        nonlocal total
        #total += value
        print(f"добавлен новый элемент {value}")
    def avg():
        return sum(numbers) / len(numbers)
    def maxim():
        return max(numbers)
    def minim():
        return min(numbers)
    def get_stats():
        dict_test = {
            "max": maxim(),
            "min": minim(),
            "avg": avg(),
            "sum": numbers,
            "numbers" : numbers,
        }
        return dict_test

    return add, get_stats

add_value, get_stats = make_stats_tracker()
add_value(5)
add_value(1)

'''
from unittest import result

#3
'''
def apply_to_each(numbers, operation):
    result = []
    for num in numbers:
        processed = operation(num)
        result.append(processed)
        
    return result
def square(number):
    return number **2
numbers = [1,2,3]
square_result = apply_to_each(numbers, square)
print(square_result)
'''
'''
#без лога
def add(a,b):
    print(f"выполнилось действие : a = {a} + {b}, a + b = {a+b}")
    return a + b

def mul(a,b):
    return a * b
#с логом
a = add(1,2)

def add_with_logging(a,b):
    result = add(a,b)
    print(f"выполнилось действие : a = {a} + {b}, a + b = {a + b}")
    return result

def mul_with_logging(a,b):
    result = mul(a,b)
    print(f"выполнилось действие mul: a = {a} + {b}, a + b = {a + b}")
    return result
def create_logging_wrapper(func):
    
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"ызвана функция {func.__name__}  с аргументом {arqs}, резудьтат: {result}")
        return result
    return wrapper
@create_logging_wrapper
def add(a,b):
    return a + b
@create_logging_wrapper
def mul(a,b):
    return a * b
print(add(1,2))

add_with_logging = create_logging_wrapper(add)
mul_with_logging = create_logging_wrapper(mul)
print(add_with_logging(2,3))
print(mul_with_logging(2,3))
'''
"""
import time
start  = time.time()
print(start)
a = 1 + 1
end = time.time()
print(end)
print(end- start)
"""
'''
from time import time
def timeit_func(func):
    start = time()
    def wrappper(*args, **kwargs):
        start = time()
        result = func(args)
        print(time() - start)
        return result
    return wrappper
@timeit_func
def add(nums:list):
    summ = 0
    for num in nums:
        summ += num
    return summ
@timeit_func
def mul(nums:list):
    mull = 1
    for num in nums:
        mull *= num
    return mull
@timeit_func
def list1(nums: list):
    summ1 = 0
    for num in nums:
        summ1 += num
    return summ1

a = mul([1,2,3,4,5])
'''
'''
from time import time
def parent(func):
    def wrapper(*args, **kwargs):
        start = time()
        a = func(*args)
        print(time() - start)
        return a
    return wrapper
@parent
def test(tfunc, listnums):
    for i, num in enumerate(listnums):
        listnums[i] = tfunc(num)
    return listnums

a = test(lambda x: x**2, [1,2,3,4,5])
print(a)
'''
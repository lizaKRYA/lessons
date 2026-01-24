#4

#matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
#filtered_matrix = list(map(lambda row: list(filter(lambda x: x % 2== 0, row)), matrix))
#print(list(map(sum, filtered_matrix)))

#1
'''
def my_filter(func, iterable):
    a = []
    for item in iterable:
        if func(item):
            a.append(item)
    return a

print(my_filter(lambda x: x%2 == 1,[1,2,3]))
'''
'''
def a(text):
    def b(t):
        print(t + text)
    return b ("hello")

a("hello")
'''
'''
def a(name,func):
    print(name)
a("boris", lambda x: x * 2)
'''
'''
def create_discount(category, discount):
    def bronze(price):
        return price * 2 - (discount / 100)
    def silver(price):
        return price * 0.5
    def gold(price):
        return price * 0.1
        
    if category == ' bronze':
        return bronze
    if category == ' silver':
        return silver
    if category == ' gold':
        return gold
    
bronze_discount = create_discount('bronze')

product_price = 1000
print()
'''
'''
def count_10_times(nums):
    if nums >= 10:
        return nums
    return count_10_times(nums + 1)
print(count_10_times(1))
'''
'''
name = 'hello'
def a():
    global name
    name2 = "world"
    def next():
        nonlocal name2
        name2 = '123'
    next()
    print(name)
a()
'''
'''
def create_adder(number):
    count = 0
    def add_to(x):
        nonlocal count
        count += 1
        return count

    return add_to

add_one = create_adder(5) #замыкание
print(add_one(1))
print(add_one(1))
print(add_one(1))
print(add_one(1))
print(add_one(1))
'''

#задача 1
'''
def make_even_generator(start):

    def next_even():
        nonlocal start
        result = start
        start = start + 2
        return result
    return next_even

even_gen = make_even_generator(6)
print(even_gen())
print(even_gen())
print(even_gen())
print(even_gen())
print(even_gen())
'''
# задача 2
'''
def make_string_builder(text):
    def next_string():
        nonlocal text
        result = text
        text = result + text
        return result
    return next_string

even_gen = make_string_builder('hello')
print(even_gen())
print(even_gen())
print(even_gen())
'''
#задача 3
'''
def make_product_accumulator(number):
    def next_product(nums):
        nonlocal number
        number = number * nums
        return number
    return next_product

even_gen = make_product_accumulator(1)
print(even_gen(5))
print(even_gen(3))
print(even_gen(4))
'''
#задача 4
'''
def make_counter(start, step):
    def next_counter():
        nonlocal start
        start = start + step
        return start
    return next_counter

even_gen = make_counter(1, 2)
print(even_gen())
print(even_gen())
print(even_gen())
'''
#задача 5
'''
def create_length_filter(min_length):
    def next_length(string):
        nonlocal min_length
        result = min_length <= len(string)
        return result
    return next_length

even_gen = create_length_filter(10)
print(even_gen("heiiiiiiiiiiiiiiiiiiii"))
'''
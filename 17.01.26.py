#lambda аргумент: тело фунуции (выражение)
'''
square = lambda x: print(x) #x: x ** 2

print(square(5))
'''

#numbers = [-1, 2 , -3 , 4 , 5]
'''
def duble_pos(num):
    if num > 0:
        return num * 2
    return num
'''

#duble_pos = lambda num: num * 2 if num > 0 else num
#pos_double = [duble_pos(i) for i in numbers]
#print(pos_double)

#pos_doubled = list((lambda num:num * 2 if num > 0 else num)(number)for i in numbers)
'''
dict_students = [
    {"name":"John", "age":25, "grade":"10"},
    {"name":"Boris", "age":10, "grade":"1"},
    {"name":"Arkadiy", "age":30, "grade": "4"},
]
get_name = lambda student: student.get("name")
get_age = lambda student: student.get("age")
get_student= lambda student: student.get(" ") if student.get("grade")  > 3 else None
names = [get_name(student) for student in dict_students]
ages =[get_age(student) for student in dict_students]
grades =[get_student(student) for student in dict_students if get_student(student)]
print(names)
print(ages)
print(grades)
'''

#unsorted_list = [4,3,2,5,1]
#unsorted_str = "ZV-bc-aA"
#print(sorted(unsorted_str))
'''
unsorted_dict = {
    4:"Maria",
    2: "Ivan",
    1:"Pavel",
    3:"Alice"
}
print(sorted(unsorted_dict))
'''

#words = ["daniel","my","name"]
#sorted_list = sorted(words, key = len)
#print(sorted_list)
'''
nums = [14,5,23,42,31]
sorted_nums = sorted(nums, key = lambda x: x % 10)
print(sorted_nums)
'''
'''
students = [
    ("John", 98),
    ("Boris", 0),
    ("Arkadiy", 77),
    ("BOB", 84),
    ("kevin", 85)
]
print(sorted(students, key = lambda x: x[1]))
'''
'''
dict_students = [
    {"name":"John", "age":1000, "score":100},
    {"name":"Boris", "age":77, "score":0},
    {"name":"Arkadiy", "age":30, "score": 60},
    {"name":"BOB", "age":80, "score": 40},
    {"name":"RONALDO", "age":85, "score": 40}
]
#a = sorted(dict_students, key = lambda x: x["score"])
#a = sorted(dict_students, key = lambda x: -x["score"])
print(a[::-1])
'''
'''
students = [
    ("Alice", 4),
    ("ronaldo", 2),
    ("ronaldo", 2),
    ("Alice", 4),
    ("Alice", 4),
    ("Alice", 4),
    ("ronaldo", 2),
    ("ronaldo", 2),
    ("ronaldo", 2),
    ("flins", 5),
    ("elena", 3)
]
students_sorted = sorted(students,key = lambda student: student[1], reverse = True)
for name, grade in students_sorted:
    print(f"{name}: оценка {grade}")
'''

#a = lambda x: len(x) * 8
#print(a("python"))

#is_even = lambda x: x % 2 == 0
#print(is_even(4))

'''
def my_logger(func, num):
    print(f"передано число: {num}.\n"
          f"результат:{func(num)}")
my_logger(lambda x: x **3, 5)
'''

#data = [(1,"b"),(3,"a"),(2,"c")]
#a = sorted(data, key = lambda x: x[1])
#print(a)

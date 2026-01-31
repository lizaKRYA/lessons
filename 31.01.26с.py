#домашка
'''
from time import sleep
def parent(func):
    def retry(max_retries, delay):
        for i in range(max_retries):
            a = func()
            print(f'попытка подключения: {i}')
            if a:
                print('успешно')
                return a
            sleep(delay)
            print('переполключение')
        return False
    return retry

@parent
def test():
    return True

print(test(3,4))
'''
import sys
from datetime import time

# типа как цикл но не цикл
#def recursion(num):
#    return recursion(num * 2)
'''
school = [
    [
        1,2,3,4,5
    ],
    
    [
        1,2,3,4,5
    ]
    
]
'''
'''
summ = 0
for school1 in school :
    for class1 in school1 :
        for sym in school1:
        summ += 1
        print(summ)
'''
'''
summ = 0
def school_ref(school,summ):
  print(school)
  if len(school)==1:
      return
  for i in school:
      return school_ref(i)
  
print(school_ref(school), summ)
'''
'''
a = [
1,2,3,
4,5,6,
7,8,9
]
def rec(lst):
    if not lst:
        return 0
    return lst[0] + rec(lst[1:])
print(rec(a))
'''

#a[
#1,2,3
#def rec(b):

   # x = 0
   # for i in b:
   #     for j in i:
   #      x += j
   #      return x
#    if b == 1:
#        return 1
#    return b + rec(b - 1)
#g = rec(a)
#print(g)

'''
def reverse_string(s):
    result = ''
    for char in s:
        result += char
    return result
def reverse_rec(s):
    if len(s) <= 1:
        return s
    return reverse_rec(s[1:] + s[0])
print(reverse_rec("hhhhhhheeeellelelelelel"))
'''
'''
#обычно
from time import time
def just(a):
    for i in range(a):
        mult *= i
    return mult
just(900)
print(time() - start)
start = time()
#рекурсивно
def just2(n):
    if n == 11:
     return 1
    return n * just2(n - 1)
just(100000)
'''
'''
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)

start = time()
def just2(n):
    if n == 1:
        return 1
    return n * just2(n - 1)
just2(1000000)
print(time() - start)
'''

#stek = ()

#LIFO -   first in last out
'''

def a()# 1:
    b()
def b():
    c() #2
def c():
    pass #3
'''
#pop - удаление и возвращение последнего элемента(первого)
#push- добавление нвого элемента stek
'''
def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)
fac(6)
'''

def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)
print(fib(350))
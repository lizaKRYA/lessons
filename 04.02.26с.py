#def power(a, n):
#    if n == 0:
#        return 1
#    return a * power(a, n - 1)
#print(power(2, 3))

#def sum_digits(n):
#    if n == 0 :
#        return 0
#    return n % 10 + sum_digits(n//10)
#print(sum_digits(100))

#def count_digits(n):
#    if n == 0:
#        return 0
#    return 1 + count_digits(n//10)
#print(count_digits(1000))
"""
from time import time
start = time()
s = {}
def fib(n):
    if n in s:
        return s[n]
    if n < 2:
        return n
    result = (fib(n-1) + fib(n-2))
    s[n] = result
    return result
print(fib(10))
print(time() - start)
"""
'''
from functools import lru_cache
import time 
@lru_cache(maxsize=256) none - неограниченно
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
start = time.perf_counter()
print(fib(100))
end = time.perf_counter()
print(end - start)
info = fib.cache_info()
'''

#stek - LIFO - last in first out - пирамида
#[10,23456789]
#очередь -FIFO - first in first out - 0 1  2 3 4
#[2,10,1,2,3,4,5,6,7,8,9]
#LFU -  least frequensy used - библиотека - > чаще всего сохраняются реже всего удаляются(на сколько часто)
#{
#    "vanya": 10,
#    "katya" : 5,
#    "ilya" : 40
#}
#LRU -  least resently used - наименее недавно использований(

#import sys
#sys.setrecursionlimit(10000)
'''
import sys
sys.setrecursionlimit(10000)
from functools import lru_cache
@lru_cache(maxsize=None)
def f(n):
    if n < 5:
        return n
    return 2 * n * f(n -4)
print(f(13766)- 9*f(13762)/f(13758))
'''
'''
from functools import lru_cache
@lru_cache(maxsize=None)
def trib(n):
    if n < 2:
        return n 
    if n == 2:
        return 1
    return trib(n-1) + trib(n-2) + trib(n-3)
'''
'''
from functools import lru_cache
@lru_cache(maxsize=None)
def ways_rec(n : int):
    if n < 0:
        return 0
    if n ==0:
        return 1
    return ways_rec(n-1) + ways_rec(n-2)
print(ways_rec(10))
print(ways_rec(100))
'''
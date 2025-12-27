#homework
"""""
st = input()
substring = input()
def find(st:str, substring:str):
    flag = 0
    for i in range(len(st)):
     for j in range(len(substring)):
         if substring[j] != st[i+j]:
             flag = True
             break
     if not flag:
         return i 
find(input(), input())
"""""
"""""
def reverse(lst:list):
    b = []
    for i in range(len(lst)-1,-1,-1):
      b.append(lst[i])
    return b
lst = list(map(int, input().split()))
print(reverse(lst))
"""'""'
""""
def index(lst:list, element:int):
   flag = 1
   for i in range(len(lst)):
       if element == lst[i]:
           print(i)
   if element not in lst or flag:
    print("эл не найден")
"""
"""""
def func1(st:str):
    st = st.lower()
    lst_st = st.split()
    set_list = set(lst_st)
    s = {}
    for item in set_list:
        s[item] = lst_st.count(item)
    return s
print(func1(input()))
     """
#d - десятичная
print(f"{27:d}")#десятичная система исчисления
#b - двоичная bin
print(f"{27:b}")
#o - восмеричная oct
print(f"{27:o}")
#x - щеснадцатиричная hex
print(f"{27:x}")

a = 1.243434243
print(f"rsggvsdgsdsd; f{a:1f}")

import string
print(string.printable)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
print(string.whitespace)




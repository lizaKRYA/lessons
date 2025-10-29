#import math#импортирует модуль ( как коробку)
#from math import sqrt #импотирует инструмнт from math
#import math as mth# меняем назание модуля и импортируем
#math - библиотека для мат вычислений
#random - библиотека для генерации псевдослчайеых чисел

#import math
#print(math.sqrt(25))

#from math import pow,sqrt
#from math import * #* - все инструменты из модуля
#print(pow(10,10))

#import math as mth
#print(mth.pow(10,10))

#from random import randint, choice

# index = randint(0,4) #от какого до какого числа сделать
#l = ["a", "b", "c", "d", "e"]
#print(choice(l))

#9
#a = input()
#index = len(a) // 2
#index = int(len(a) / 2)
#j = a[:index]
#b = a[index:]
#print(j + b)

#14

#a = input()
#j = a[::2]
#k = a[1::2]
#k = k[::-1]
#print(j+k)

#15

#j = input()
#for i in range(0,len(j)-2):
#    print(j[i:i:+3])

#12

#a = "шалаш, камыш, заказ, возврат, поиск, довод, спектр, комок, альянс"
#a = a.split(", ")
#for i in a:
#    if i == i[::-1]:
#        print(i)

#16

#s = input()
#alpha = " "
#amount = 0
#set - уникализирует список
#setter = set(s)
#print(setter)
#for i in set(s):
#    count = s.count(i)
#    if count> amount:
#        alpha = i
#        amount = count
#print(alpha,amount)
#print(s[::3])
#maxim = 0
#print(a.rfind("o"))
#for i in setter:
#    if s.count(i) == 1:
#        continue
#    backward = s.rfind(i)
#    forward = s.find(i)
#    if (backward - forward) > maxim;
#        maxim = backward - forward
#    indexes = a[backward:forward]
#        print(indexes)


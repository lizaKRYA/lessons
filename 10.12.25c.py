#1
"""""
with open("902.txt", "r") as f:
    k = 0
    for line in f:
        s = line.split()
        d = []
        for i in s:
            d.append(int(i))
        d = sorted(d)
        flag = True
        k_amount = 0
        for i in range(len(d)):
                k_cash = 0
                for j in range(len(d)):
                    if d[i]==d[j]:
                        k_cash += 1
                if k_cash > 1:
                    k_amount +=1
                    flag = False
                    print(k_amount)
                    print(d)
                if d[-1] > sum(d[:-1]) and k_amount == 1:
                  k += 1
        print(k)
"""
import numbers
from os import set_inheritable

#2
"""
with open("903.txt" , "r") as f:
    count = 0
    for line in f:
        numbers = line.split("\t")
        s = []
        for i in numbers:
            s.append(int(i))
        s = sorted(s)
        print(s[1:-1], s)
        sum_rst = sum(s[1:-1]) >= (s[0] + s[-1])
        if sum_rst :
            count +=1 
        print(count)
"""

"""
with open("900.txt", "r") as file:
    for line in file:
     numbers = line.split("\t")
     g  = []
     for i in numbers:
      g.append(int(i))
      k = 0
      amount_lines = 0
     first = []
     second = []
     for i in g:
         if g.count(i) != 1:
             first.append(i)
             continue
         second.append(i)
            
         if len(set(g)) == 4 and sum(first) **2  > sum(second) **2:
          if k == 1:
              amount_lines += 1
         print(amount_lines)
   """
"""
with open("905.txt", "r") as file:
       g = 0
       for line in file:
           number = line.split("\t")
           h = []
           for i in number:
               h.append(int(i))
           if len(set(h)) == 3  and h.count(max(h)) > 1:
               g += 1
               print(g)
"""







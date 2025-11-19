#46
from time import process_time

#t = (1,2,3,4,4,4,4,5,6,8,4,6,7)
#count = 1
#maxim = 0
#for i in range(len(t)):
#    if t[i] == t[i-1]:
#        count+=1
#    else:
#        if maxim < count:
#            maxim = count
#
#print(maxim)

#47

#cart = [("яблоки", 100),("хлеб",50),("молоко",80),("яблоки",100)]
#cart1 = []
#for i,j in cart:
#    if j > 70:
#      cart1.append((i,j))
#for i,j in cart:
#    cart2.append((i,j*2))
#print(cart2)
#for i,j in set(cart):
#    cart3.append(i,j/2))
#print(cart3)

#48

#books = [("война и мир",1865), ("1984", 1949),("гарри поттер", 1997),("война и мир", 1965)]
#books1 = []
#books2 = []
#books3 = []
#for i, j in books:
#    if j>1900:
#        books1.append((i, j))
#        print(j)
#for i, j in books:
#    books2.append((i, j-100))
#    print(i, j)
#for i, j in set(books):
#    if j<1950:
#        books3.append((i, j))
#    print("классика", i, j)

#59

#math_students = {"Анна", "Борис", "Вера", "Глеб"}
#physics_students = {"Борис", "Вера", "Дмитрий", "Елена"}
#chemistry_students = {"Вера", "Глеб", "Дмитрий", "Жанна"}
#print(math_students.intersection(physics_students).intersection(chemistry_students))
#print(math_students.difference(physics_students, chemistry_students))
#print(math_students.union( physics_students) - chemistry_students)

#62

#a = set()
#for i in range(0,21,2):
#    a.add(i)
#a1 = set()
#    for i in range(0,31,3):
#        a1.add(i)
#a2 = set()
#for i in  range(1,20):
#    if i % 2 ==0 and i%3==0:
#     a2.add(i)
#print(a)
#print(a1)
#print(a.intersection(a1))
#print(a2)

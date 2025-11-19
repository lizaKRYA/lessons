#homework

#1

#from random import randint
#r = randint(1,10)
#for i in range(20):
#    r_unique = set(r)
#    f_count = len(r_unique) - len(r)
#    print(f_count)

#2

#my_set = set()
#for i in range(5):
#    g = int(input())
#    my_set.add(g)
#    print(my_set)
#    print(len(my_set))
#if my_set:
#    e = min(my_set)
#    p = max(my_set)
#    print(e)
#    print(p)
#else:
#    print ("ничо нет")

#3

#numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#for number in numbers:
#    if number % 2 == 0:
#        numbers.discard(number)
#for i in numbers:
#   squared = numbers ** 2
#print(squared)

#4

#fantasy_readers = {"Игорь", "Катя", "Лев", "Марина"}
#detective_readers = {"Катя", "Лев", "Никита", "Ольга"}
#sci_fi_readers = {"Лев", "Марина", "Никита", "Павел"}
#print(fantasy_readers.intersection(detective_readers).intersection(sci_fi_readers))
#print(fantasy_readers.difference(detective_readers,sci_fi_readers))
#print(fantasy_readers.union(detective_readers) - sci_fi_readers)
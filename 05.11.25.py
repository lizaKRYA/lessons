#2 homework
#from random import randint
#a = [
#    randint(1,100),
#    randint(1,100),
#     randint(1,100),
#      randint(1,100),
#       randint(1,100)
#
#]
#maxim = 0
#minim = 100
#for i in a:
 #   if maxim < i:
 #       maxim = i
  #  if minim > i:
  #      minim = i
#print(a,maxim,minim)

#3

#s = input().strip(" ") #удаляет символы
#count = 0
#len_s = len(s)
#for i in range(len_s):
#    print(i)#helloh

#    for j in range(i+1, len_s):
#      if s[i] == s[j]:
#          if j - i > 1:
#              count += 1
#    print(count)

#a = [1,2,3,4]
#iterator = iter(a)
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))

#for i in a:
#    print(i)

#    k = [1,2,3]
#    k = [
#        [1,2,3],
#        [4,5,6],
#        [7,8,9]
#    ]
#k[0] = 0
#for i in range(0,len(k)):
#    k[i] += 1
#    print(k)

#k = [1,2,3]
#l = [4,5,6]
#z = k + l
#k.extend(l)#асширяет олин объект другим
#k = [
# print(z)
#from random import randint
#k =[]
#for i in range(5);
#    #обавлет новый элемент в конец списка
#    k.append(randint(0,100))
#    print(k)

#k = ["раз", "три"]
#j = ["два"]
#k.insert(1,j)# вставляет перед необхрдимых индексов значение
#print(k)

#k = [1,2,3,4,5]
#k.remove(4)#удаляет первый найденый жлемент
#print(k)

#k = [1,2,3,4,5]
#k.clear()#чистит список
#print(k)

#k = [1,2,3,4,2,3,4,5]
#k.pop(4)#даляет лемент по индексу
#print(k)

#k = [5,4,3,2,1,2,3,4,5]
#k = ["a","b","c","d","e","f"]
#k.sort()
#k.sort(reverse=False)
#print(k)

#k = ["шалаш"]
#k.reverse()#переворачивает список
#print(k)

#k = [1,2,3,4,5]
#print(max(k))
#print(min(k))
#print(sum(k))

#1

#k = [1,2,3,4]
#for i in range(lem(k)):
#    k[i] *=2
#    print(k[i])

 #4

# d = [1,2,3,4]
# iterator = iter(k)
# sumarry = 0
# for i in range(len(d)):
#     summary += next(iterator)
# print(summary)

#k = [1,2,3]
#z = [4,5,6]
#for i in range(len(k)):
#    print(k[i] + z[i], end="")

#8

#g = ["kkj","hhh","oujo"]
#for i in g:
#    count = 0
#   for _ in i:
#       count+= 1
#        if count % 2 == 0:
#            print(i)

#11

#from random import randint
#s = randint(1,100000)
#for _ in str(s):
#    print("разряд")
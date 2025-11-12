#2 homework

#a = int(input())
#b = []
#while True:
#    b.append(a%10)
#    a //= 10

#for i in str(a):
#    b.append(int(i))
#b.sort()#сортирует
#print(b)

#a = (1,2,3,4,5)#кортеж tuple()
#b = [1,2,3,4,5]
#print(tuple(b))#перевод типа #неизменяемый

#FHFH ="hrllo"
#s = ("helo", "world")

#v = 1000
#h = 3000
#f = (1000, 3000)

#values = (1,2,3,4,5)
#v = 1
#r = 1
#x,y= y,x
#print(x,y)
#s1 * s2 = values
#print(s1,s2)
#s = (1,2,3)
#s1 = (4,5)
#print(*s)#распаковывает
#s3 = (*s, *s1)
#print(s3)=

#next_tuple = (1,(2,3,4),5)
#s1,(*s2,*s4),s3 = next_tuple
#print(s2)
#print(*next_tuple[1][1:])

#s = ((1,2),(3,4),(5,6))
#for i,j in s:#подчиняется правилвм распаковки
#    print(i,"+",j,"=",i+j)
#for i in s:
#    print(i[0], "+", i[1], "=", i[0]+i[1])

#next = [([1,2],3),["XY",6]]
#for ((i,b),j) in next:
#    print(i,b,j)

#set

#a = {1,2,3,4,5,6,1,2,3,4,6,7}
#b = [1,2,3,5]
#print(set(b))
#print(a)

#s = {(1,2),(3,4)}
#s = {[1,2],[3,4]) error
#print(s)
#подайье кашолку

#s.add((5,6))#добавление элемента во множество
#print(s)

#s.remove((1,2))#даление жлмеента мноества
#print(s)

#s.clear()
#print(s)


#34

#h = (1,2,3)
#s1, s2, s3 = h
#print(s1)
#print(s2)
#print(s3)

#40

#a = input().split(" ")
#for i in range(len(a):
#    a[i] = float(a[i])
#a = tuple(a)
#*s,s1 = a
#print(s[::-1],s1)

#42

#a = (1,2,3,4,5)
#b = (6,7,8,9,0)
#res = ()
#for i in range(len(a)):
#    res = (*res,a[i]+b[i])
#    print(res)

#set_1 = {1,2,3,4,5,6}
#set_2 = {4,5,6,7,8,9}
#set_3 = set_1.union(set_2)#обединение
#set_4 = set_1.update(set_2)
#print(set_3)

#set_3 = set_1.intersection(set_2)#пересечение
#set_3 = set_1.symmetric_difference(set_2)#имметричная разность
#set_1.intersection_update(set_2)
#print(set_3)

#set_3 = set_1.difference(set_2)#разность
#print(set_3)

#set_1 = {1,2,3}
#set_2 = {3,4,4,5,7,6,7}
#print(set_2.issubset(set_1))
#print(set_1.issubset(set_2))

#print(set_2.issubset(set_1))
#print(set_1.issubset(set_2))

#задача
#a = input()
#b = set()
#print(b,len(b))
#if len(b)>len(a):
#    print("yes")
#else:
#    print("no")





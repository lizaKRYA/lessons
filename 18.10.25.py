#2

#a = input()
#z = 0
#for i in a:
#    z += int(i)
#print(z)

#3

#a = input().split (" ")#"1 2 3 4 5 6 7 8 9 " split
#z = True
#for i in a:
#    if int(i) > 100:
#        print(i)
#        z = True
#        break
#if z == False or z != True or not(z):
#    print("таких чисел нет")

#4

#a = int(input())
#j = False
#for i in range(2,a):
#    if a % i == 0:
#        j = True
#        print(a)
#        break
#
#    if not(j):
#        print("простое")

#5



#for i in range(1,5):
#    for j in range((4-i),-1,-1):
#        print("*" * i + " " * j)
#        break

#15

#a = int(input())
#j = False
#for i in range(2,10):
#    if a % i ==0:
#        j = True
#        print("простое")
#        break
#if not(j):
#        j = False
#        print("составное")

#18

#a = int(input())
#j = False
#for i in range(0,a):
#    if i < a and i % 3 ==0:
#        j = True
#        print("большое число")
#if not(j):
#    j = False
#    print("таких чисел нет")

#20

#a = input()
#a_input = str()
#for i in a:
#    if i != "a":
#        if i != "e":
#            if i != "i":
#                if i != "o":
#                    if i != "u":
#                        if i != "y":
#                            print(i)
#in - в условиях проверяет принадлежность
#a = input()
#b = "aiuyeoIEOUY"
#for i in a:
#    if i not in b:
#print(i, end="")

#end - устанавливает свой символ в конце по умолчанию \n

#24
#for i in range(3,-1,-1):
#    print("*" * (4 - i)+ " "* i)
#for i in range(3,0,-1):
#    print("*" * i + " "*(4 - i))

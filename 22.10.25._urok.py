#1


#a = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
#for i in a:
#    for j in a:
#        for k in a:
#            print(i+j+k)

#3

#while True:
#    a = int(float(input()))
#    b = int(float(input()))
#    event = input()
#    if event == "stop":
#        break
#    if event == "*":
#        print(a*b)
#    if event == "+":
#        print(a+b)
#    if event == "-":
#        print(a-b)
#    if event == "/":
#        print(a/b)

#4

#a = input()
#b = ""
#for i in a:
#    b = i + b
#print("palidrom", if b == a else "no")

#1.1

#a = [
#    [1,2],
#    [3,4]
#]
#print(a[0])
#print(a[1])
#print("-"*10)
#for i in range(0,len(a)):
#    print()
#range - генерирует список элементов в промежутке от и до
#len - длина объекта
#b = [
#    [0,0],
#    [0,0]
#]
#for i in range(len(a)):
#    for j in range(len(a[0])):
#        b [j][i] = a[i][j]
#    for i in b:
#        print(i)

#3.1

#z = "hello"
#print("o" in z)#проверяет принаддежность вне for
#b = "1234567890"
#counter = 0
#while True:
#    a = input("введите пароль: ")
#    if counter == 2:
#        print("опопробуй в другой раз")
#    break
#    counter += 1
#    if len(a)<= 8:
#        print("пароль не верный нужно больше 8 символов")
#    else:
#        k = False#сть ли в пароле числы
#        for i in b:
#            if i not in a:
##                break
 #       if k:
 #               print("пароль верный")

#a = [
#    [[1,2], [3,4]],
#    [[5,6], [7,8]]
#]
#a = [1,2,3,4]#[[1,2],[1,2]]
#a = [
#    [1,2],
#    [3,4]
#]#таблица
#a[0][1]

#b = [
#    [0,0]
#    [0,0],
#    [0,0]
#]
#for i in range(0,len(a)):
#    for j in range(0,len(a[i])):
#    print(i,j)


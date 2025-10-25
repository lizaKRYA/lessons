#5
#h = int(input())
#counter = 0
#for i in range(1,h*2,2):
#    counter += 1
#    print(" "*(h - counter), end="")
#    for j in range(1,counter):
#        print (j, end=" ")
#        for j in range(counter,0,-1):
#            print (j, end=" ")
#        print()

#6

#a = "1234567"
#counter = 0
#l = True
#s = " "
#for i in a:
#    if i == ".":
#        l =False
#        elif

#a = " abcdABCD "
#for i in a:
# print(ord(i),i)
#print("q" < "w")

#a = "10A"
#print(int(str(a),16))

#print("\n\t")
#print("\"")
#print("\U0001F600")
#g = "https:\\google.com\hello"
#print(g)

#name = "mishka"
#s[n:m:k]
#n = начало среза
#m - конец среза ( не включительно )
# k - шаг среза
#print(name[0:4:2])
#ms
#print(name[-1])
#print(name[::-1])

str = "    hello world   "
#print(str.find("q"))#поиск первого вхождения подстроки
#print(str.index("d"))#возвращает индекс подстроки если такого нет
#print(str.rfind("w"))
print(str.split(" "))#елит сроку по разделителю " "
print(str.count(" "))#считает колво полстрок
print(str.lower())#дклвкт текст в нижнем регистре
print(str.upper())#поднимвет текст с колен(верхний регситр)
print(str.isdigit())#се символы строки это числа
print(str.isalpha())#True  если ет пробелоы в строке
string = (" hello ")
print(str.isalnum())#два верхних методв в 1
print(str.strip("l"))#удаляет выбранный символ в начале и конце строки
print(str.replace("*", "#"))
#replace(симывол, на что меняем, сколько раз)
l = ["h", "e", "l" , "l"]
print("-".join(l))#соединяет эдементы с разделитеем

#str = "wiguwpgejwejijw"
#print(str[-4:])

a = "djdgjsdlgjlgkj"
print(a[0:-1:2])
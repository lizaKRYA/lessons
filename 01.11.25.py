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
#    indexes = a[forward+1:backward]
#        print(indexes)


#28

#z = input()
#while True:
#    if z.lower() == 0:
#        print("yes")
#        j = j + 1
#        break
#    if z.upper() == 0:
#        print("yes")
#        break
#    if z.title() == 0:
#        print("yes")
#        break
#    else:
#        print("no")

#a = input()
#print(a.islower())
#print(a.upper())
#print(a.title())

#30

#d = input()
#if not(d.isalpha()):
#    print(d.upper())
#elif not(d.isalnum()):
#    print(d.replace(" ", " * "))
#else:
#    print(d)

#32
#f = input()
#j = 0
#for i in f:
#     nex_j = f.rfind(i)
#     if j < nex_j:
#         j = nex_j
#         alpha = i
#print(j)

#31

#x = "abcd defg ghij"
#x = x.replace("", "")
#for i in x:
#    if x.count(i) > 1:
#        x = x.replace(i, " ")
#print(x)


#20

#choice - случайнвй элемент последатеьности
#from random import choice
#s = " hello"
#while s:
#    a = choice(s)
#    s = s.replace(a, " ")
#    print("удалили букву",a,":", s)

#19
a = input()
k = "АВЕКМНОРСТУХ"
if len(a) == 6:

  numbers = a[1:4]
  aplha = a[:1] + a[4:]
  print(numbers.isdigit() and alpha[0] in k and alpha[1] in k and alpha[2] in k)
else:
      print(False)



#1

#d = input()
#a,b,c = d.split()
#print(f"Значение переменной а: {a}")
#print(f"Значение переменной b: {b}")
#print(f"Значение переменной c: {c}")

#2

#f = input()
#a,b,c,d = map(int, input().split())
#sum_numbers = a+c
#pr_numbers = b* d
#print(sum_numbers,pr_numbers)

#3

#n = input()
#n.isdigit()
#b = 1
#for digit in n:
#    b += int(digit)
#    print(f"{n}: {b}")
#else:
#    print("error")

#4

#g = input()
#a, b = map(int, input().split())
#sum1 = a + (b * 3)
#sum2 = a - (a % 2)
#print(f"Первое число: {sum1}")
#print(f"Второе число: {sum2}")

#f = input()
#if f % 3 == 0:
#    print(f"Удвоенное число: {f * 2}")
#    if f % 2 ==0:
#        print(f"Число без изменений: {f}")

#6

#s = input()
#for i in range(100,999):
#    s_str = str(s)
#    digit1 = int(s_str[0])
#    digit2 = int(s_str[1])
#    if digit2 % 2 != 0 or digit1 % 2 == 0:
#     s += 1
#     if digit1 in [3,7,9]:
#         s -=1
#         print()

#7

#x = float(input())
#if x > 0:
#    y = 3 * x + 1
#elif x == 0:
#    y = x
#else:
#    y = x **2 + 2
#    print(f"{x} равна {y}")

#8

#h = input()
#h_1 = int(h, 16)
#h_2  = bin(h_1)[2:]
#h_3 = h_2.count('1')
#print(f"Введенное число в двоичной СС: {h_2}")
#print(f"ккКОличество единиц: {h_3}")

#9
#b = input()
#if len(b) != 5 or not b.isdigit():
#    print("error")
#else:
#    sum1 = sum(int(digit) for digit in b)
#    print(f"Введенное число: {b}")
#    print(f"Сумма всех разрядов: {sum1}")

#10

#-

#11

#f = input().split()
#h = "".join(f)
#print(h[::-1])

#12
#f = input()
#print(f)
#s = (s.strip() for s in input().split(","))
#for i,s in enumerate(s, 1 ):
#    print(s)
#ond = "".join(char for char in f if char.isdigit())
#print(ond)


#g = input().split()
#g = list(map(int, g))
#print( f"Список: {g}")
#k = 0
#f = False
#for i in g:
#    if i % 13 ==0 and i % 2==0:
#        sum1 = sum(g)
#        f = True
#        break
#    k+= 1
#    if  f:
#     print(f"Сумма элементов до числа {g}: {sum1}")
#    else:
#     print(f"Подходящих чисел не найдено")

#14

#q = int(input())
#z = list(map(int, q.split()))
#print(f"Список:{z}")
#z_1 = [num for num in z if num % 2 == 0]
#print(z_1)
#sum1 = sum(z_1)
#print(sum1)
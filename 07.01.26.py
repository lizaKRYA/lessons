#1

#a = input().split(" ")
#for i in a:
#    print(i[::-1], end=" ")

#all() and
#any() or

#print(all([False, True, False])) #эквивалент and
#print(any([False, True, False])) #эквивалент  or

#a = []
#for i in range(1,1000):
#    a.append(i % 10 == 0)
#print(any(a))
#print(all(a))

#a = [10,20,30,40,50]
#b = []
#for i in a:
#    b.append(i >= 0)
#print(all(a))

#a = [" ", " hello"," ", "world"]
#b = []
#for i in a:
#    b.append(i !="")
#print(any(a))

#enumerate - последовательность, начальный индекс =0
#a = ["h","e","l","l"]
#print(list(enumerate(a, start = 0)))
#for i in range(len(a)):
#    print(a[i])

#for i, item in enumerate(a, start = 0):
#    print(i, item)

#my_dict = {
#    "ключ 1": "значение 1",
#    "ключ 2": "значение 2",
#    "ключ 3": "значение 3",
#}

#for key, value in my_dict.items():
#    print(key, value)
#for i,(value,key) in enumerate(my_dict.items(), start = 1):
#    print(i,key, value)

#a =  ((1,2,3,4,5),(6,7,8,9,10),)
#(z,*y),(k,*s) = a #пакуем элементы
#print(k, s)
#print(z,y)

#print(*a[0], sep="")#запаковка

#a = [10,25,30,15,40,5,50]
#for i, value in enumerate(a):
#    if value >= 20:
#        print(i, value)

#a = ["python","java","c","javascript","go", "rust","php"]
#for i in  enumerate(a):
#    if "a" in i[1] and len(i[1])>3:
#        print(i[0], i[1])

#zip()

#a = ["hello", "my name is"]
#b = ["world", 'daniel']
#for i in range(len(a)):
#    print(a[i], b[i])

#for first, second in zip(a, b):
#    print(first, second)

#    print(list(zip(a,b)))

#pairs = [(1,"a"), (2,"b"), (3,"c"),(4,"d")]
#nums, letters = zip(1,"a"), (2,"b"), (3,"c"),(4,"d")
#print(nums)
#print(letters)

#names = ["алексей", "мария", ' иван']
#ages = [25,30,22]
#for name, ages in zip(names, ages):
#    print(f"{name}:{ages} лет")

#students =["anna","boris","victor"]
#subjects = ["math","physics","chemistry"]
#grades = [5,4,5]
#for students, subjects, grades in zip(students, subjects, grades):
#    print(f"студент: {students},предмет: {subjects}, оценка:{grades}")

#prices = [100, 200,150,300]
#discounts = [10, 15, 5, 20]
#for prices, discount in zip(prices, discounts):
#    print(f"цена без скидок: {prices}"
#          f"цена со скидкой: {discount}")
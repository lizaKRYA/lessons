#переменная - именновая ячейка в памяти
user_name = "Алиса" #строковый тип -  string (str)
max_value = 100 #Численный тип - integer (int)
our_float =1,6 #число с плавающей точкой (float)
logical = True #True\false (1 или 0) - boolen (bool)

# id - возвращает адрес в памяти
print(id(user_name) ,id(max_value), id(our_float),id(logical))

#a = 2
#b = 276655
#a = b
#print (id(a),id(b))

#  определяет тип переменной (объект)
#a = 1
#print(type(a))

a = int(1) # переводит в int
print(type(a), a)
a = float(a) #ереводит в float
print(type(a), a)
a = str(a) # переводит в строку
print(type(a), a)
a = bool(a) # переводит в bool  ( логический тип )
print(type(a),a)

name = "Лиза"
print("Лиза")

#age = 16
#name = "Мне 16 лет"
#print("Мне", age, "лет")

a = "Текст"
# a - имя , a [ index: int]
# index - начинается с 0
# index - целое число
print(a[4]) #  синаксис получения элемента по индексу

my_list = [1, 2,"привет", 4, 5] # тип данных (list)
print(my_list[4].__sizeof__()) # показывает размер в битах

#my_list = [1,2,3,4,5,6,7,8,9,10] # always list нет массивов
# * / + - ( базовые операторы )
#print(my_list[1] - 3 / 2)

#{} - dict ( словарь ) в качестве аргментов ключь : значение
#dictonary = { "a": 880980928}
#print(dictonary["a"])

#input - команда ввода данных
a = input ("Веведите текст: ")
print(a * 10)

a = input ("Введите тест: ")
b = input ("Введите текст: ")
a = int(a)
b = int(b)
print(a * b)


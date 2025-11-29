# функции

#for i in range(10):
 #   print(i)

#for i in range(30):
#    print(i)
#значение принимаеые функции
#def name_func(first_arg = 10,*, second_arg = 15 ):#функция
    #тело  функции
 #   for i in range(first_arg, second_arg):
  #      print(i)
        #конец функции
        # название функций уникальны (строятся как и перемнные)
#параметры
#name_func(first_arg = 25) #вызов функции
#name_func(10, 15)
#name_func(first_arg=10,second_arg=25)
#без наименований в параметрах
#def name_func_2(x,y, /):
 #   pass#ничего(заглушка)

#name_func_2(x=6, y = 2)
#name_func_2(6,2)

#def name_func_3(*args):
#    for i in args:
#        print(i)

#name_func_3(1,2,3,4,5,6)


#словарь - kwargs
#def name_func_4(**kwargs):
#    kwargs.pop("name2")
#    print(kwargs)

#name_func_4(name1 = 1, name2 = 2)

#def a():
#    d = [
#        [
#            [1,2,3],
#            [4,5,6],
#            [7,8,9]
#        ]
#    ]
#    def b(x):
#        for i in range(x):
#            for j in range(y):
#                for k in range(z):
 #           print(d[i][j][k])
#        print( x + " world"
#        b (len(d),len(d[0]), len(d[0][0]))
#print("hello world")
#x = 20#глобальная область видимости
#def local_func():

    #global x
#    x = 10 #локальная область видимости
#    print(x)
    #возвращение значения
#    return [x,x,x]
#local_func()
#print(x)
#print(local_func())

#def a():
#    x = 10 #охватывающая область
#    def b():
#        nonlocal x
#        x = 5
#        print(x)
#    b()
#    print(x)
#a()

#def square(x):
#           x = 0
#           z = True
#           def func():
#               global x
#           while True:
#                while True:
#                     if x >= 5:
#                          return
#                     x+=1
#           if not z:
#                 break
#                 print(x)
#
#print(square(10))
#print(square(5))
#sum ()

#x:int = 0
#def func(s:str)-> list:
#    """
#    эта функция делае что то
#    :return:
#    ничего
#    """
#    global x
#    while True:
#        while True:
#            if x >= 5:
#                return[1,2,3]
#            x +=1
#print(func("hello"))
#print(x)

#2

#def func(y = 10,x = 20):
#    if y!= 0 and type(x) == int and type(x) == int:
#     return y/x

#    return



#name_func = func(10,20)
#print(name_func)

#3
#def  is_even(n:int):
 #    if n%2 ==0:
 #     return True
  #return False
#
#print(is_even(5))

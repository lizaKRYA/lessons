#1

#Напишите функцию, которая принимает натуральное число и возвращает его факториал (используя цикл!).



#2

#Напишите функцию number_to_digits(n), которая принимает натуральное число и возвращает список его цифр.

#def number_to_digits(n):
#    if n > 0:
#        return str(n)
#j = []
#for i in range(1,11):
#    j.append(number_to_digits(i))
#print(j)

#3

#Напишите функцию is_prime(n), которая принимает целое число и
# возвращает True для простых чисел или False для чисел, не являющихся простыми.

#def is_prime(n):
#    if n <= 1:
#        return False
#    if n <= 3:
#        return True
#    if n % 2 == 0 or n % 3 == 0:
#        return False

#    i = 5
#    while i * i <= n:
#        if n % i == 0 or n % (i + 2) == 0:
#            return False
#        i += 6

 #   return True
#print(is_prime(2))


#4

#напишите функцию camel_to_snake(s), которая принимает строку в «верблюжьем регистре»
# (ThisIsCamelCased) и преобразует ее в «змеиный регистр» (this_is_camel_cas

#def camel_to_snake(s):
 #   snake_case = []

  #  for char in s:
   #     if char.isupper() and snake_case:
    #        snake_case.append('_')
     #   snake_case.append(char.lower())
   # return ''.join(snake_case)

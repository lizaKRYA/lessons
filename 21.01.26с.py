#2


#sign = lambda x: "positive" if x > 0 else "zero" if x==0 else"negative"
#print(sign(0,...))

#4
'''
with open('2601.txt', 'r') as f:
    N = int(f.readline())
    data = list(map(int, f))
print(N)
print(data)

data = sorted(data, reverse=True)
res =[data[0]]

for i in data[1:]:
    if res[-1] - i >= 9:
        res.append(i)
print(len(res), res[-1])
'''

#map(функция, список(интерируемый объект- все объекты которые можно посчитать или перебирать))
#MAP  это метод который позволяет применить фунуцию к каждому элементу пос-ти
'''
def plus(x):
    return x + 5
a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#print(list(map(plus, a))) 
print(list(map(lambda x: x + 5, a)))
'''

#a = [2,3,4,5]
#print(list(map(lambda x: [[]]* x,a)))
'''
user = [
    {'username': 'liza_kryachko', 'age': 17},
    {'username': 'olya', 'age': 16},
    {'username': 'dasha', 'age': 15},
    {'username': 'roza', 'age': 14}

]

print(list[str](map(lambda x: x['username'], user)))
'''

#nums = list(range(0,10))
#enens = list(filter(lambda x: int(x) % 2 == 0, nums))
#print(enens)
#filter()
'''
def plus(x):
    return '+'
def minus(x):
    return '-'
def nums(plus, minus):
    return plus(), minus()
s= {
    'plus': plus
}
print(nums(plus, minus))
print(s['plus'])
'''

#nums = [1,2,3,4,5]
#num = []
#print(list(map(lambda x: x ** 2, nums)))


#nums = [1,2,3,4,5,6,7,8,9,10]
#num =  []
#print(list(filter(lambda x: x % 2 != 0, nums)))


#words = ['appple', 'banana', 'cherry', 'date']
#print(list(map(len, words)))

#nums = [-5,-2,0,3,7,-1,10]
#num = []
#print(list(filter(lambda x: x > 0, nums)))

#a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#b = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
#c = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
#print(list(map(lambda x, y: x + y ,a,b)))

#list1 = [1,2,3,4]
#list2 = [5,6,7,8]
#list3 = []
#print(list(map(lambda x, y: x * y ,list1, list2)))

'''
def func1(x):
  if 0 <= x <= 2:
      return True
  for i  in range(2,int(x / 2) + 1):
    if x % i == 0:
      return True
  return False
nums = [2,3,4,5,6,7,8,9,10,11,12]
print(list(filter(func1, nums)))
'''

def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
        return result


nums = [2,3,4,5,6,7,8,9,10,11,12]
my_map(lambda x: x+5, nums)

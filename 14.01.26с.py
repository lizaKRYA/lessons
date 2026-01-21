#1
'''
nums = [2,4,6,8,10]
result = any(num>7 and num % 3 == 0 for num in nums)
print(result)
'''

#2
'''
password = "MyPass123"
has_upper = any(i.isupper() for i in password)
has_lower = any(i.islower() for i in password)
has_digit = any(i.isdigit() for i in password)
is_valid = all([has_upper, has_lower, has_digit])
print(is_valid)
print(is_valid)
'''

#3
'''
with open('files/901.txt') as f:
    data = [list(map(int, i.split())) for i in f]
    
def f1(line):
  cnt_3 = [i for i in line if line.count(i) == 3]
  cnt_1 = [i for i in line if line.count(i) ==1]
  return len(cnt_1) == 6 and len(cnt_3) == 1

def f2(line):
   rep = [ i for i in line if line.count(i) != 1]
   norep = [ i for i in line if line.count(i) == 1]
   aver = sum(rep) / len(rep)
   return aver < norep[0]

for pos, val in list(enumerate(data, start = 1))[::-1]:
    if f1(val) and f2(val):
        print(pos)
        break
'''


#4
'''
from statistics import mean  #1 #средн ариф

with open('911.txt') as f:
    data = [list(map(int, i.split())) for i in f]

for pos, val in list(enumerate(data, start = 1))[::-1]:
    cnt_3 = [i for i in val if val.count(i) ==3]
    cnt_1 = [i for i in val if val.count(i) == 1]
    if len(cnt_3) ==3 and len(cnt_1) ==3 and mean(cnt_1) < cnt_3[0]: #2
        print(pos)
        break
'''
#5
'''
with open ('913.txt')as f:
    data = [list(map(int, i.split())) for i in f]

def f1(line):
    return len(line) == len(set(line))

def f2(line):
    line.sort()
    doubled_sum = (line[0] +line[-1])*2
    triple_rest = sum(line[1:-1]) *3
    return doubled_sum == triple_rest

for pos, val in list(enumerate(data, start = 1))[::-1]:
    if f1(val) and f2(val):
        print(pos)
        break
'''
'''
#открываем файл
with open ("название файла") as f:
    data = [list(map(int, i.split())) for i in f]

#условие 1

def f1(line):
    
#условие 2

count = 0
for line in data:
    #если оба условия выполняютсяъ
     # увел на 1 cout
    print(count)
'''
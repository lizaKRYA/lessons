#html css rect/vue/django/fstapi/flask
#1
#with open('transactions.txt'  ) as f:
#      f.write(f.read())


#2

#3

#def solve():
#    with open("triples.txt") as f:
#        nums = [int(line.strip()) for line in f if line.strip()]
#        print()
#6



def log_action(func):
     def wrapper(*arg):
         print(f"выполняется {func.__name__}")
         result = func(*arg)
         print(f'фунция {func.__name__} выполнена')
         return result
     return wrapper
@log_action
def read_sales():
    with open('transactions.txt', "r", encoding = ' utf-8') as f:
        s = []
        for i in f:
            b = i.split(',')
            s.append(( b[0], b[1], b[2].strip('\n')))
        return s

def get_total_sales(sales, category):
    with open('transactions.txt', "r", encoding=' utf-8') as f:
        s = 0
        for i in f:
            b = i.split(',')
            if b[1] == category:
             s += float(b[0].strip('\n'))
        return s

def get_average_sales(category):
    with open("transactions.txt", 'r', encoding ='utf-8' ) as f:
        s = 0
        summ = 0
        for i in f:
            b = i.split(',')
            if b[1] == category:
             summ += 1
             s += float(b[0].strip('\n'))
    return s / summ
print(read_sales())
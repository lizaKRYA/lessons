#1
'''
def hanoi(n,c, b, a):
    if n == 1:
        print(f"Переместить диск 1 со стержня {c} на стержень {b}")
    else:
        hanoi(n - 1, c, a, b)
        print(f"Переместить диск {n} со стержня {c} на стержень {b}")
        hanoi(n - 1, a, b, c)

n = 3
hanoi(n, 1, 3, 2)
'''
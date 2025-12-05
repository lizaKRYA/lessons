#homework
#1

#with open ("test.txt", "w", encoding="utf-8") as file:
 #   file.write("привет\n как дела\n")
#with open("test.txt", "a", encoding="utf-8") as file:
#    file.write("как погода\n")
#with open('example.txt', 'r') as file:
#    lines = file.readlines()

#2
#from random import randint
#d = {"A": 10, "B": 20, "C": 30}
#randint(100,999)
#for value in d.values():
#    with open ("test.txt", "w") as file:
#        for key, value in d.items():
#         file.write(f"{key: value}")
#    with open("test.txt", "r") as file:
#        lines = file.readlines()
#for line in lines:
#    print(line.strip())

#3

#import random

#with open("test.txt", "w") as file:
#    for _ in  range(50):
#        n = random.randint(1,100)
#        file.write(f'{n}\n')
#with open("test.txt", "a") as file:
#    for _ in range(20):
#        n = random.randint(1,100)
#        file.write(f'{n}\n')
#with open("test.txt", "r") as file:
#    lines = file.readlines()

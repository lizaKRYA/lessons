#from random import randint
#d = {"A": 10, "B": 20, "C": 30}
#c = {}
#c.update({
#    randint(100,999): d["A"],
#    randint(100,999): d["B"],
#    randint(100,999): d["C"]
#})
#with open("test.txt", "w") as file:
#    for key,value in c.items():
#        file.write(f"{key}:{value}\n")
#with open("test.txt", "r") as file:
#    for item in file.readlines():
#        file.readlines(f"{key}:{value}\n")
import string

#3

#from random import randint
#with open("test.txt", "w") as file:
#    for i in range(50):
#        file.write(str(randint(1, 100)) + "\n")
#with open("test.txt", "a") as file:
#    for i in range(20):
#        file.write(str(randint(1, 100)) + "\n")
#with open("test.txt", "r") as file:
#    a = file.readlines()
#    print(int(a[0]))

#s = "qwertyuiopasdfghjklzxcvbnm"
#import string

#print(string.punctuation)
#print(string.digits)
#print(string.ascii_letters)
#print(string.ascii_uppercase)
#print(string.ascii_lowercase)

#print("hello" + ":" + "world")
#sighn = ":"
#print(f"hello{sighn}world")

#from random import randint,choice
#import string
#list_pairs = []
#for i in range(100):
#    a = choice(string.ascii_uppercase)
#    a += str(randint(0, 9))
#    list_pairs.append(a)
#with open('test.txt', 'w') as f:
#    f.writelines("\n".join(list_pairs))

#with open('test.txt', 'r') as f:
#    for i in f:
#        if int(i[1]) % 2 == 0 and not i[1] != "0":
#            print(i)
#with open('test.txt', 'r') as f:
#    cnt = 0
#    for i in f:
 #       if i[0]== "A":
 #          cnt +=1
 #          print(i)

  #  a = "".join(f.readlines()).count("A")
  #  print(a)

#from random import randint, choice
#import string
#d = []
#for i in range(150):
#    a = choice(string.ascii_letters)
#    b = choice(string.digits)
#    d.append(a)
#    print(f"{a}-{b}")
#with open ("test.txt", "w") a:
#    f.write("\n".join())
#    print(d)
#with open("test.txt", "r") as f:
#    a = "".join(f.readlines()).count("\n")
#    for i in f:
#     if int(i[2] ) > 5:
#      print(a)

with open ("903.xlsx", "w") as f:
    s = []
    for line in f:
        number = line.split("\t ")
        maxim = 0
        minim = 99999999999999
        for i in numbers:
                  s.append(int(i))
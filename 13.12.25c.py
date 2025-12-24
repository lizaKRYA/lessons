#2: homework

    #with open("908.txt","r") as f:
    #k = 0
    #for line in f:
    #   s = line.split()
    #    print(s)
    #    d = []
    #    for i in s:
    #        d.append(int(i))
    #        minim = min(d)
    #        arif = sum(d)/len(d)
    #        if minim - arif:
    #            k +=1
    #            print(k)

#with open("test.txt","w") as f:
#    f.write("QRW124")
#with open("test.txt","r") as f:
#    k = 1
#    l = 1
#    maxim = max(map(str,f.readlines()))
#    print(maxim.join(maxim))
#    a = f.read()
#    for i in range(1, len(f.read()), -1):
#       if  (a[i-1].isdigit()  and not a[i].isdigit() or a[i].isalpha() and not a[i].isnumeric())
#             l +=1
#       else:
#           maxim = max(maxim,a[i-1])
#           print(maxim)

#with open("1700.txt", "r")as f:
#            data = list(map(int, f)
#            minim = min(data)
#            answer = []
#                for i in range(len(data)):
#                z = data[i]
#                y = data[i+1]
#                if z % 16 == minim or y % 16 == minim:
#                       answer.append(z + y)
#                print(len(answer), max(answer))



#with open("1710 (1).txt") as file:
#    d = list(map(int, file.read().split()))
#    maxim = max(d)
#    a = []
#    for i in range(len(d)):
#        x = d[i]
#        y = d[i+1]
#        if x + y == maxim:
#            a.append(x**2 + y**2)
#            print(len(a), max(a))
def func1(x,l):
    return (10 <= x <= 99)^ (10 <= y <= 99)
with open("1700.txt", "r")as f:
          r = list(map(int, f))
          minim = -1
          for  i in r:
              if 10 <= i <= 99:
                  if minim == 0 or minim > i:
                      minim = i
                      a = []
          for i in range(len(r) - 1):
              z = r[i]
              y = r[i + 1]
              if func1(z,y) and ((z + y) % minim) == 0:
                  a.append(z + y)
                  print(len(a), max(a))
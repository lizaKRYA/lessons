#4

#a = [1,2,10,1000,999,5,10,15,5]
#minim = 2020309494885859595595958585858
#count = 0
#for i in a:
#    if i < minim:
#        minim = i
#        count+=1
#print(minim, count-1)

#29
#from random import randint

#h = []
#for i in range(5):
#     h.append(randint(0,9))
#print(h)
#s = h[0]
#h[0]= h[-1]
#h[-1] = s
#или
#h[0],h[-1] = h[-1],h[0]
#print(h)

#25

#nums = [1,2,3,4,5,6]
#b = (sum(nums) / len(nums))
#for i in nums:
#    if  i == b:
#        nums.remove(i)
#print(nums)

#23

#a = [1,2,3,4,5,6,7,8,9,0,3,4,6,1,4,3]
#k = []
#for i in range(len(a)-1):
#    if a[i] > a[i+1] and a[i] > a[i+1]:
#        k = [a[i], i]
#        break
#    print(k[0], k[1], a.index(k[0]))

#21

#d = input().split(" ")
#h = []
#for i in d:
#    if i not in h and d.count(i) < 2:
#        h.append(i)
#print(h)

#31

#d = [2,4,2,9,8,3,4,2,1,9,3,2,8,5,9]
#h = []
#for i in range(len(d)):
#    for j in range(i,len(d)):
#        if d[j] in h:
#            break
#        h.append(d[j])
#        if len(h) > maxim:
#            maxim = len(h)
#            cash = h
#print(maxim, sum(cash), cash)









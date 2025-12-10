#1
#num = []
#k = 0
#for s in open("902.txt"):
#         num.append(sorted(map(int, s.split())))
#         for n in range(len(num)):
#             if len(num) == 4:
#                if num[n][3] < num[n][1] + num[n][0] + num[n][2]:
#                                   k += 1
#                                   print(k)

#2


#with open("903.txt","r") as f:
#    s = []
#    k = 0
 #   for line in f:
 #       numbers = sorted(line.split("\t"))
#        maxim = 0

#        minim = 9999999
 #       for i in numbers:
 #           if int(i) > maxim:
 #               maxim = int(i)
 #           if int(i) < minim:
 #               minim = int(i)
  #              sum_1 = len(numbers)
  #              if sum_1 > maxim + minim:
  #                    k +=1
 #print(numbers,maxim, minim)



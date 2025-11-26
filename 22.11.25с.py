#1

#a = input()
#k=()
#j = {}
#for i in k:
#    j.update(i:a)

#85

#f = input().split()
#b = input().split()
#d1 = {}
#for i in f:
#    d1[int(i)] = d1.get(int(i),0)+1
#    d2 = {}
#    for i in b:
#        d2[int(i)] = d2.get(int(i),0)+1
#    for k,v in d2.items():
#        d1.update({k: d1.get(k,0) + v})
#    print(d1)

#86

#a = sorted(input().split())
#dict_a = dict.fromkeys(a, 0)
#dict_b = {}
#for i in dict_a:
#    dict_a[i] = a.count(i)
#    if dict_a[i] > 1:
#     dict_b.update({i: dict_a[i]})
#print(dict_a)
#print(dict_b)

#88

#students = [
#
 #   {'name': 'Alice', 'group': 'A', 'score': 85},
#
  #  {'name': 'Bob', 'group': 'B', 'score': 92},
#
 #   {'name': 'Charlie', 'group': 'A', 'score': 78},
#
 #   {'name': 'David', 'group': 'C', 'score': 88},
#
 #   {'name': 'Eve', 'group': 'B', 'score': 95}
#
#]
#
#f = {}
#for i in students:
 #   if i["group"] in f:
  #      f[i["group"]].append(i["name"])
   # else:
    # f[i["group"]] = [i["name"]]

     #print(f)

 #87

#v = input().replace(" ", " ")
#j = {}
#for i in set(v):
#    j[i] = v.count(i)
#    s =  [
#        ["",0],
#        ["", 0],
#        ["",0]
#    ]
#    for i in j:
#        for v in range(len(s)):
#            if s[v][1] < j[i]:
#             s[v][0] = i
#             s[v][1] = j[i]
#print(j)
#print(s)

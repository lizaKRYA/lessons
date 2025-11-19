# classwork

#sets = {
#    "key":"value",
#    "key1":[
#        1,2,3,4
#    ]
#}#словарь с элементом { ключ : значение}
#print(sets["key"])
#print(sets["key1"][2])
from tkinter.font import names

#my_dict = [
#    ("ключ1","значение1"),
#    ("ключ2","значение2"),
#    ("ключ3","значение3")
#]
#print(my_dict, dict(my_dict))

#d = {}#dict
#d = {1,2}#set
#b = {1:3,4:5}
#print(b[3])

#d = {"key1":"value1"}
#print("key1" not in d) #есть ли ключ в словаре d?
#b = [1,2,3]
#b["key1"] = 100
#d["key2"] = 200
#print(b)
#d = {"key1" : "value1", "key2" : "value2"}
#for i in d:
#    print(i, d[i])
#print(d.items())
#for i,j in d.items():#получает все жлементы как списо кортежей
#    print(i, j)

#print(list(d.values()))#возвращает списрк значений
#print(list(d.keys()))#список ключей

#print(d.get("key3",10))#get(key, value i not exists)
#print(d.pop("key67",10),d)#озвращает значение и удаляет элемент

#print(d.popitem()
#popitem()#даляет и врзвращает последнй элемент
#d.update({"key3":"value3"})

#d.clear
#a = d.copy()#создает копию элемента  в памяти
#a["key3"] = "value4332"
#print(d)

#keys = ["key1", "key2", "key3", "key4", "key5", "key6"]
#new_dict = dict.fromkeys(keys, 8888)#
#print(new_dict)

#69

#s = {}
#s ["name"] = "lice"
#s.update

#71

#points = {"x":10}
#print(ouints.get("y",10))

#75
#books = {"романы":10,"детектив":5}
#books.update("ФАНТАСТИКА":8)
#print(books)
#79
#
#m = {"IT":5,
#   "russhian":4,
#         "history":5,
#         "physics":4,
#         "math":4}
#print(sum(m.values())/ len(m))


#80

#d = input().split(" ")
#dd = []
#k=[]
#for i in d:
#    key,value = i.split(":")
#    k.append((key,int(value)))
#    dd[key] = int(value)
#print(dd,"\n",dict(k))

#81
f = {}
student = ["anna",5,"boris",4,"vera",5]
for i in range(0,len(student),2):
    f[student[i]] = student[i+1]
    print(f)
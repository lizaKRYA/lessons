#2
#{"ignore_case": True}
#s = "1234567890"
#def words(text, **options):
#  if options.get("ignore_case", False):
#        text = text.lower()
#  if iotions.get("ignore_nums", False):
#      for i in s:
#          text = text.replace(i,"")
#  text_list = text.split()
#  text_set = set(text_list)
#  dict_new = {}
#  for text_list_item in text_set:
#        dict_new[text_set_item] = text_list.count(text_set_item)
#  return dict_new
#print(words("hello23 World Hello", ignore_case = True, ignore_nums = True ))

#открытие файлв маршрут/ тип открытия / кодировка  при чтении / записи
#file = open("test.txt", "r", encoding="utf-8")
#r - чтение
#w - запись
#a - добавить в конец файла
# x - открывает файл для записи если только онине существует
# rb, wb, ab, xb - бинарные действия
# r+/x+- открывает файл для чтения и записи ( файл должен сущ)
# w+/a+ - открывает файл для записи если файла нет он его создаст
#print(file.read())#считывает все строки текстового файла
#print(file.readline())#считывает одну строку из файла
#print(file.readlines())#счивтывает файл как список строк
#print(file.readline())#курсор в начале первой строки
#print(file.readline())# урсор в начале второй строки
#print(file.readline())#курсор в начале третьей строки
#print(file.readline())#курсор в начале четвертой строки

#print(file.read(10))
#print(file.tell())#позици указателя (число)
#file.seek(0)
#print(file.readline(1000000))

#a = [1,2,3,3,4,5,6,7,8,9,10]
#d = a[: 3]
#print(d)

#file.close() #закрытие файлов
#контекстный менеджер
#with open("test.txt", "a", ) as file:
 #   file.write("\nhello world")
 #   file_item = file.readline()
  #  while file_item:
  #      print(len(file_item)-1)
  #      file_item = file.readline()
  #  file.readline()
 # for file_item in file:
  #    print(len(file_item)-1)

 # s = ["hello\n", "world"]
  #with open("test2.txt", "w", encoding = 'utf-8') as f:

#with open("test.txt", "r+", encoding = " utf - 8") as f:
 #   file.write("hello world")
#
#with open("test.txt", "r+", encoding = "utf - 8") as f:
  #  file.write("hello world")

#with open("test.txt", "r+", encoding = " utf - 8") as f:
 #   file.writelines("hello world")
#1
#s =["hello","my", "name"]
#with open("text.txt", "w", encoding="utf-8") as file:
 #   file.writelines(s)
  #  with open("text.txt", "r", encoding="utf-8") as file:
   #     print(file.read())

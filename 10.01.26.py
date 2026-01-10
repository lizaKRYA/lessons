#1

#keys = ['name', 'age', 'city', 'profession']
#values = ['Иван', 28, 'Москва', 'Программист']
#d = dict(zip(keys, values))
#for i, (key, value) in enumerate(d.items(), start=1):
#    print(f"{i}. {key}: {value}")

#2

#correct_answers = ['A', 'B', 'C', 'D', 'A']
#student_answers = ['A', 'B', 'D', 'D', 'A']
#b = 0
#for i, (correct_answer, student_answer) in enumerate(zip(correct_answers, student_answers), start=1):
#    if correct_answer == student_answer:
#        b += 1
#        print("правильно")
#    else:
#        print("неправильно")

#3
#-

#4

#temp = [20, 22, 18, 25, 19, 21]
#new_temp = []

#for i in range(len(temp)):
#    new_temp.append(temp[i] + i)
#    print(new_temp)

#5

#matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
#c = []
#for i,j in enumerate(matrix):
#    if 0 in j:
#        c.append(i)
#    if c:
#        print(f" с нулями : {c}")
#    else:
#        print("error")
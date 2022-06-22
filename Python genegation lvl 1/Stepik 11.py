'''
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)
print(average)
'''
'''
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = (max(evens) + min(evens)) / 2
print(average)
'''
'''
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
for i in range(len(rainbow)):
    if rainbow[i] == 'Green':
        rainbow[i] = 'Зеленый'
    elif rainbow[i] == 'Violet':
        rainbow[i] = 'Фиолетовый'
print(rainbow)
'''
'''
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
#for i in rainbow:
#    i = i.replace('e', 'E')
#print(rainbow)
print([x.replace("Green", "Зеленый").replace("Violet", "Фиолетовый") for x in rainbow])
'''
'''
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[-1::-1])
'''
'''
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]
print(numbers1*2 + numbers2*9 + numbers3)
'''
'''
words1 = ['iq option', 'stepik', 'beegeek']
words2 = ['iq option', 'stepik', 'beegeek']
w3 = words1 + ['pytnon']
words1.append('python')
words2.extend('python')

print(words1)
print(words2)
print(w3)
'''
'''
w = ['iq option', 'stepik', 'beegeek']
w[1:2] = 1, 2
print(w)
'''
'''
import time
a = [i for i in range(1000000)]
start = time.time()
print('start', start)
for i in range(1000):
    a = a.copy()
stop = time.time()
print('stop', stop)
print('a = a.copy() x 1000:', stop - start)

print('\n')
a = [i for i in range(1000000)]
start = time.time()
print('start', start)
for i in range(1000):
    a = a[:]
stop = time.time()
print('stop', stop)
print('a = a[:] x 1000:', stop - start)

print('\n')
a = [i for i in range(1000000)]
start = time.time()
print('start', start)
for i in range(1000):
    a = list(a)
stop = time.time()
print('stop', stop)
print('a = list(a) x 1000:', stop - start)
'''
'''
import timeit

a = [i for i in range(500000, 0, -1)]
start = timeit.default_timer()
for _ in range(len(a)):
    del a[0]
stop = timeit.default_timer()
print('del a[0]:', stop - start)

a = [i for i in range(500000, 0, -1)]
start = timeit.default_timer()
for _ in range(len(a)):
    a.pop(0)
stop = timeit.default_timer()
print('a.pop(0):', stop - start)
'''

'''
Заменил второй элемент списка на 17;
Добавил числа 4, 5 и 6 в конец списка;
Удалил первый элемент списка;
Удвоил список;
Вставил число 25 по индексу 3;
Вывел список, с помощью функции print()
'''
'''
numbers = [8, 9, 10, 11]
#print(numbers)
numbers[1] = 17
#print(numbers)
numbers.append(4)
numbers.append(5)
numbers.append(6)
#print(numbers)
del numbers[0]
#print(numbers)
numbers = numbers * 2
#print(numbers)
numbers.insert(3, 25)
print(numbers)
'''

'''
На вход программе подается строка текста, содержащая различные
натуральные числа. Из данной строки формируется список чисел.
Напишите программу, которая меняет местами минимальный и максимальный
элемент этого списка.
'''
'''
l = [int(i) for i in input().split()]
max_i = l.index(max(l))
min_i = l.index(min(l))
l[max_i], l[min_i] = l[min_i], l[max_i]
print(*l)
'''

'''
На вход программе подается строка, содержащая английский текст.
Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.
'''
'''
#через строки - нормально не стработало
st = input()
count = st.lower().count(' a ')
count += st.lower().count(' an ')
count += st.lower().count(' the ')
print(count)
'''
'''
#через список
st = input().split()
search = ['a', 'an', 'the', 'A', 'An', 'The']
count = 0
for i in search:
    count += st.count(i)
print('Общее количество артиклей:', count)
'''

'''
NB - классная задача (удаляем комментарии из кода)
Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли
– секретный бункер Братства Стали, и любезно соглашается помочь
им в решении их проблем. Одной из такой проблем являлся странный
компьютерный вирус, который проявлялся в виде появления комментариев
к программам на терминалах Братства Стали. Известно, что программисты
Братства никогда не оставляют комментарии к коду, и пишут программы
на Python, поэтому удаление всех этих комментариев никак не навредит им.
Помогите писцу Ибсену удалить все комментарии из программы.

На первой строке вводится символ решётки и сразу же натуральное число
nn — количество строк в программе, не считая первой. Далее следует nn строк кода.

Нужно вывести те же строки, но удалить комментарии и символы пустого пространства
в конце строк. Пустую строку вместо первой строки ввода выводить не надо.
'''
'''
nn = int(input()[1:])
code = [input() for _ in range(nn)]
for line in range(len(code)):
    if ' #' in code[line]:
        com_i = code[line].find(' #')
        while code[line][com_i] == ' ':
            com_i -= 1
        code[line] = code[line][:com_i+1]
print(*code, sep = '\n')
'''

'''
На вход программе подается строка текста, содержащая целые числа.
Из данной строки формируется список чисел. Напишите программу, которая
сортирует и выводит данный список сначала по возрастанию, а затем по убыванию.
'''
'''
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
l.sort()
print(*l)
l.sort(reverse = True)
print(*l)
'''
'''
l = [int(i) for i in input().split()]
l.sort()
print(*l)
l.sort(reverse = True)
print(*l)
'''



'''
ЭКЗАМЕН
'''
'''
На вход программе подаются две строки текста, содержащие
целые числа. Из данных строк формируются списки чисел L и M.
Напишите программу, которая создает третий список,
элементами которого являются суммы соответствующих элементов
списков L и M. Далее программа должна вывести каждый элемент
полученного списка на одной строке через 1 пробел.
'''
'''
a = input().split()
b = input().split()
c = [int(a[i]) + int(b[i]) for i in range(len(a))]
print(*c)
'''

'''
На вход программе подается строка текста, содержащая
натуральные числа. Напишите программу, которая вставляет
между каждым числом знак +, а затем вычисляет сумму полученных чисел.
'''
'''
a = [int(i) for i in input().split()]
sum_a = sum(a)
a = [str(i) for i in a]
str_a = '+'.join(a)
print(str_a, sum_a, sep = '=')
'''
'''
Проверка номера телефона на корректность
На вход программе подается строка текста. Напишите программу,
которая определяет является ли введенная строка корректным
телефонным номером. Строка текста является корректным телефонным
номером если она имеет формат:
abc-def-hijk или
7-abc-def-hijk
где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
'''
'''
st = input()
st = st.split('-')
numbers = '0123456789'
flag = False
if len(st) == 3:
    if len(st[0]) == 3 and len(st[1]) == 3 and len(st[2]) == 4:
        flag = True
        for i in range(len(st)):
            for j in st[i]:
                if j not in numbers:
                    flag = False
                    break
            if not flag:
                break
elif len(st) == 4:
    if st[0] == '7' and len(st[1]) == 3 and len(st[2]) == 3 and len(st[3]) == 4:
        flag = True
        for i in range(len(st)):
            for j in st[i]:
                if j not in numbers:
                    flag = False
                    break
            if not flag:
                break
if flag:
    print('YES')
else:
    print('NO')
'''

'''
На вход программе подается строка текста. Напишите программу,
использующую списочное выражение, которая находит длину самого длинного слова.
'''
'''
st = input().split()
st_len = [len(i) for i in st]
print(max(st_len))
'''

'''
На вход программе подается строка текста. Напишите программу,
использующую списочное выражение, которая преобразует каждое
слово введенного текста в "молодежный жаргон" по следующему правилу: 
первая буква каждого слова удаляется и ставится в конец слова; 
затем в конец слова добавляется слог "ки".
'''

st = input().split()
st_out = [st[i][1:]+st[i][0]+'ки' for i in range(len(st))]
print(*st_out)


#%%
# random.shuffle(my_list)
'''
import random
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)
random.shuffle(my_list)
print(my_list)
'''

#%%
# random.choice(my_iterable)
'''
import random
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
my_string = '1 2 3 4 5 6 7 8 9'
my_string2 = '123456789'
[print(random.choice(my_string2)) for _ in range(5)]
'''

#%%
# string module
'''
import string
a1 = string.ascii_letters
print('string.ascii_letters\n', type(a1), a1)
print()
a2 = string.ascii_lowercase
print('string.ascii_lowercase\n', type(a2), a2)
print()
a3 = string.ascii_uppercase
print('string.ascii_uppercase\n', type(a3), a3)
print()
a4 = string.digits
print('string.digits\n', type(a4), a4)
print()
a5 = string.hexdigits
print('string.hexdigits\n', type(a5), a5)
print()
a6 = string.octdigits
print('string.octdigits\n', type(a6), a6)
print()
a7 = string.punctuation
print('string.punctuation\n', type(a7), a7)
print()
a8 = string.printable
print('string.printable\n', type(a8), a8)
print()
'''

#%%
# 12.2.6
'''
IP адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных точкой.

Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.

Примечание 1. Пример правильного (неправильного) IP адреса:

192.168.5.250        # правильный
199.300.521.255      # неправильный
'''
'''
# v1
import random as r
def generate_ip():
    return f'{r.randint(0, 255)}.{r.randint(0, 255)}.{r.randint(0, 255)}.{r.randint(0, 255)}'

for _ in range(10):
    print(generate_ip())
'''
'''
# v2
import random as r

def generate_ip():
    return '.'.join([str(r.randint(0, 255)) for _ in range(4)])

for _ in range(10):
    print(generate_ip())
'''


#%%
# 12.2.7 
'''
Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.

Примечание 1. Пример правильного (неправильного) индекса Латверии:

AB23_56VG          # правильный
V3F_231GT          # неправильный
Примечание 2. Обратите внимание на символ _ в почтовом индексе.

Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.
'''
'''
# v1
import random as r
import string as s
def generate_index():
    answer = list()
    answer.append(r.choice(s.ascii_uppercase))
    answer.append(r.choice(s.ascii_uppercase))
    answer.append(str(r.randint(0, 99)))
    answer.append('_')
    answer.append(str(r.randint(0, 99)))
    answer.append(r.choice(s.ascii_uppercase))
    answer.append(r.choice(s.ascii_uppercase))
    answer = ''.join(answer)
    return answer

print(generate_index())
'''
'''
# v2
import random as r
import string as s
def generate_index():
    num1, num2 = (str(r.randint(0, 99)) for _ in range(2))
    l1, l2, l3, l4 = (r.choice(s.ascii_uppercase) for _ in range(4))
    return '{}{}{}_{}{}{}'.format(l1, l2, num1, num2, l3, l4)

print(generate_index())
'''


#%%
# 12.2.8
'''
Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы (двумерного списка).

Примечание. Выводить содержимое матрицы не нужно.
'''
'''
# v1
import random as r

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]


numbers = list()
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        numbers.append(matrix[i][j])
print(numbers)

r.shuffle(numbers)
print(numbers)
matrix_mixed = [[numbers.pop(0) for i in range(len(matrix))] for j in range(len(matrix[i]))]
matrix = matrix_mixed

for row in matrix_mixed:
    print(row)
'''
'''
# v2
import random as r

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

n = len(matrix)
m = len(matrix[0])

# превращаем матрицу в список двумя спосабами
numbers1 = [elem for row in matrix for elem in row]
numbers2 = sum(matrix, [])

print(numbers1)
print(numbers2)
r.shuffle(numbers1)
r.shuffle(numbers2)
mx1 = [[numbers1[i*m + j] for j in range(m)] for i in range(n)]
mx2 = [[numbers2[i*m + j] for j in range(m)] for i in range(n)]
print()
for row in mx1:
    print(row)
print()
for row in mx2:
    print(row)
'''


#%%
# 12.2.9
'''
Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров лотерейных билетов и выводит их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:

номер не может начинаться с нулей;
номер лотерейного билета должен состоять из 7 цифр;
все 100 лотерейных билетов должны быть различными.

'''
'''
# v1
import random as r
n = 100
tickets = set()
while len(tickets) < n:
    num = [str(r.randint(1, 9))]
    for _ in range(6):
        num += [str(r.randint(0, 9))]
    tickets.add(''.join(num))

# print('total tickets:', len(tickets))
for ticket in tickets:
    print(ticket)
'''
'''
# v2
from random import sample
n = 10
answer = sample(range(1000000, 10000000), n)
print('total tickets:', len(answer))
for ticket in answer:
    print(ticket)
'''

#%%
# 12.2.10
'''
Анаграмма – это слово образованное путём перестановки букв, составляющих другое слово.

Например, слова пила и липа или пост и стоп – анаграммы.

Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму.

Примечание. Обратите внимание на то, что метод shuffle() работает со списком, а не со строкой.
'''
'''
# v1 
from random import shuffle
word = [sym for sym in input()]
shuffle(word)
print(''.join(word))
'''
'''
# v2
from random import sample
word = input()
print(''.join(sample(word, len(word))))
'''

#%%
# 12.2.11 - Бинго
'''
ля игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные) целые числа от 1 до 75 (включительно), при этом центральная клетка является пустой (она заполняется числом 0).

Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.

Примечание 1. Для наглядности рекомендуем отводить на вывод каждого числа ровно 3 символа. Для этого используйте строковый метод ljust().

Примечание 2. Пример возможного ответа:

1  16 31 46 61
10 30 42 47 68
3  18 0  48 63
9  19 34 49 70
5  20 35 50 65
Возможны и другие способы генерации карточки для игры в бинго.
'''
'''
# v1
from random import sample
num_list = sample(range(1,76), 25)
print(num_list)
bingo_ticket = [[num_list[i*5 + j] for j in range(5)] for i in range(5)]
bingo_ticket[2][2]=0
for row in bingo_ticket:
    for elem in row:
        print(str(elem).rjust(3, ' '), end ='')
    print()
'''
'''
# v2
from random import sample
num_list = sample(range(1,76), 25)
ticket = [num_list[i:i+5] for i in range(0, 21, 5)]
ticket[2][2] = 0
for row in ticket:
    for elem in row:
        print(str(elem).rjust(3, ' '), end = '')
    print()
'''


#%%
# 12.2.12 Тайный друг 🌶️
'''
Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе с ним решать задачи по программированию.

Формат входных данных
На вход программе в первой строке подается число n – общее количество учеников. Далее идут n строк, содержащих имена и фамилии учеников.

Формат выходных данных
Программа должна вывести имя и фамилию ученика (в соответствии с исходным порядком) и имя и фамилию его тайного друга, разделённые дефисом.

Примечание 1. Обратите внимание, что нельзя быть тайным другом самому себе и нельзя быть тайным другом для нескольких учеников.

Примечание 2. Приведенные ниже тесты это лишь образцы возможного ответа. Возможны и другие способы выбора тайных друзей.
'''
'''
# v1 через списки и множества
from random import choice
# pupils = [input() for _ in range(int(input()))]
pupils = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p2 = pupils.copy()
for i in range(len(pupils)):
    friend = choice(list(set(p2) - {pupils[i]}))
    p2.remove(friend)
    print(pupils[i], '-', friend)
'''
'''
# v2 через множества
from random import choice
pupils = [input() for _ in range(int(input()))]
# pupils = [1, 2, 3, 4, 5, 6, 7, 8]
# pupils = pupils[:3]
p2 = set(pupils)
for pupil in pupils:
    if len(p2) == 2 and pupils[-1] in p2:
        el1, *_ = p2 - {pupils[-1]}
        el2, *_ = p2 - {el1}
        print(pupils[-2], '-', el2)
        print(pupils[-1], '-', el1)
        break
    else:
        friend = choice(list(p2 - {pupil}))
        p2 -= {friend}
        print(pupil, '-', friend)
'''
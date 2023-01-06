#15.9 base info
#%%
'''
a = []
a1 = ()
a2 = {}
b = [[], []]
b1 = 
print(type(b1))
f = all(b1)
print(f)
'''
#%% all()
'''
def if_all_less(numbers0, num0):
    """проверяем, все ли элементы меньше заданного значения num0"""
    flag = all(map(lambda x: x < num0, numbers0))
    if flag:
        print(f'все элементы меньше {num0}')
    else:
        print(f'хоть один элемент больше {num0}')
    return flag

numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]
if_all_less(numbers, 2000)
'''
#%% enumerate()
'''
numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]

en = enumerate(numbers)
print(type(en))
print(*en)
'''
#%% zip()
'''
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = ['apple', 'banana', 'carrot']
z = zip(a, b, c)
print(type(z))
print(*z)
'''
#%% zip - формируем словарь
'''
name = ['Timur', 'Ruslan', 'Rustam']
age = [28, 21, 19]
my_dict = dict(zip(name, age))

print(my_dict)
for k, v in my_dict.items():
    print(k, v)
'''
#%% zip - параллельный перебор по нескольким коллекциям
'''
name = ['Timur', 'Ruslan', 'Rustam']
age = [28, 21, 19]
color = ('red', 'white', 'yellow', 'black')
for n, a, c in zip(name, age, color):
    print(n, a, c)
'''
#%%
'''
from itertools import zip_longest
name = ['Timur', 'Ruslan', 'Rustam']
age = [28, 21, 19]
color = ('red', 'white', 'yellow', 'black')
for n, a, c in zip_longest(name, age, color, fillvalue=0):
    print(n, a, c)
'''
#%%
'''
name = ['Timur', 'Ruslan', 'Rustam']
age = [28, 21, 19]
f = zip(name, age)
print(*f)
print(*f)
for i in range(2):
    print(f'step {i}')
    for elem in f:
        print(elem)
    print()
'''
#%% 15.9.8
'''
"""Функция ignore_command() принимает на вход один строковый аргумент command – команда, которую нужно проверить,

и возвращает значение True, если в команде содержится подстрока из списка ignore и False – если нет.
def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    for word in ignore:
        if word in command:
            return True
    return False
Перепишите функцию ignore_command(), чтобы она использовала встроенные функции all()/any() сохранив при этом ее функционал."""

test = (
    ('get ip', True),
    ('select all', True),
    ('delete', True),
    ('trancate', False)
)

def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(map(lambda x: x in command, ignore))

for q, a in test:
    print('answer:', a)
    print(ignore_command(q))
'''

#%% 15.9.10 v1
'''
"""Используя параллельную итерацию сразу по трем спискам countries, capitals и population выведите информацию о стране в формате:

<capital> is the capital of <country>, population equal <population> people.


Moscow is the capital of Russia, population equal 145934462 people.
Washington is the capital of USA, population equal 331002651 people.
...
Для каждой страны информацию выводить на отдельной строке. """

countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for country, capital, popul in zip(countries, capitals, population):
    print(f'{capital} is the capital of {country}, population equal {popul} people.')
'''
#%% 15.9.10 v2
'''
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for data in zip(countries, capitals, population):
    print('{1} is the capital of {0}, population equal {2} people.'.format(*data))
'''


#%% 15.9.11 - Внутри шара
'''
"""Внутри шара
На вход программе подаются три строки текста с вещественными числами, значениями абсцисс (x), ординат (y) и аппликат (z) точек трехмерного пространства. Напишите программу для проверки расположения всех точек с введенными координатами внутри либо на поверхности шара с центром в начале координат и радиусом R =2.

Формат входных данных
На вход программе подаются три строки текста с вещественными числами, разделенными символом пробела – абсциссы, ординаты и аппликаты точек в трехмерной системе координат.

Формат выходных данных
Программа должна вывести True если все точки с введенными координатами находятся внутри или на границе шара и False, если вне.

Примечание 1. Гарантируется, что количество чисел во всех трех строках одинаковое.

Примечание 2. Уравнение поверхности шара (сферы) имеет вид 

Примечание 3. Для решения задачи используйте встроенные функции all() и zip().

Примечание 4. Используйте следующие названия abscissas, ordinates, applicates для соответствующих списков."""

test = (
    ('0.0 1.0 2.0', '0.0 0.0 1.1', '0.0 1.0 1.5', False),
    ('0.0 0.0', '1.5 0.0', '1.1 1.1', True),
    ('0.637 -0.411 -0.247 1.658 0.061', '-0.78 -1.374 0.762 0.306 -0.614', '-1.317 -0.444 -0.572 -0.341 0.295', True)
)

'''
def my_map(my_func, my_data):
    answer = []
    for elem in my_data:
        answer.append(my_func(elem))
    return answer

def func1(data0):
    print(type(data0))
    print(data0)
    x0, y0, z0 = data0
    return f'{x0}-{y0}-{z0}'

data_x = [[1, 2, 3], [4, 5, 6]]
print(my_map(func1, [[1, 2, 3], [4, 5, 6]]))
print('v1', *map(lambda data0: f'{data0[0]}-{data0[1]}-{data0[2]}', data_x))
print('v2', *map(lambda x, y, z: f'{x}-{y}-{z}', data_x))
'''

# print(abscissas, ordinates, applicates)
# проверка
# for data in test:
#     abscissas, ordinates, applicates,  = [[float(num) for num in data[i].split()] for i in range(3)]
#     answer = data[-1]
#     print('step')
#     print('data', data[:-1])
    
#     f1 = list(zip(abscissas, ordinates, applicates))
#     print('f1', f1)
#     for i in range(len(f1)):
#         print(f'{i}: {f1[i]}')
#     print()
#     f2 = list(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, f1))
#     print('f2', f2)
#     f3 = all(f2)
#     print('f3', f3)
#     print('answer:', answer)

#     f7 = list(map(lambda data_x: f'{data_x[0]}-{data_x[1]}-{data_x[2]}', f1))
#     print('f7', f7)
    

#     print('answer:', answer)
#     print('final', all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas, ordinates, applicates))))
#     print()

# 15.9.11 v1
abscissas, ordinates, applicates = [[float(num) for num in input().split()] for _ in range(3)]
print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas, ordinates, applicates))))

# 15.9.11 v2
abscissas, ordinates, applicates = [[float(num) for num in input().split()] for _ in range(3)]
print(all(x**2 + y**2 + z**2 <= 4 for x, y, z in zip(abscissas, ordinates, applicates)))
'''

#%% 15.9.12 - Корректный IP-адрес
'''
"""Корректный IP-адрес

IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающей по протоколу TCP/IP.

В 4-й версии IP-адрес представляет собой 32-битное число. Адрес записывается в виде четырёх десятичных чисел (октетов) со значением от 0 до 255 (включительно), разделённых точками, например, 192.168.1.2.

Напишите программу с использованием встроенной функции all() для проверки корректности IP-адреса: все ли октеты в IP-адресе – числа со значением от 0 до 255.

Формат входных данных
На вход программе подается строка в формате x.x.x.x, где x – непустой набор символов 0-9, a-z.

Формат выходных данных
Программа должна вывести True если введенная строка – корректный IP-адрес и False в противном случае."""


# 15.9.12 v1
def ip_check(adress):
    adress_num = []
    for elem in adress:
        try:
            adress_num.append(int(elem))
        except:
            return False
    return all(0 <= num <= 255 for num in adress_num)

# ip = input().split('.')
# print(ip_check(ip))

# проверка
test = (
    ('10.0.1.1', True),
    ('10.1.1.a', False),
    ('10.1.1.260', False),
    ('10.0023.0123.0000015', True)
)

for row in test:
    # print(row)
    print(ip_check(row[0].split('.')))
    print('answer:', row[1])
    print()
'''
#%% 15.9.12 v2
'''
def ip_check(adress):
    try:
        return all(0 <= int(num) <= 255 for num in adress)    
    except:            
        return False

# ip = input().split('.')
# print(ip_check(ip))

# проверка
test = (
    ('10.0.1.1', True),
    ('10.1.1.a', False),
    ('10.1.1.260', False),
    ('10.0023.0123.0000015', True)
)
for row in test:
    print(ip_check(row[0].split('.')))
    print('answer:', row[1])
    print()
'''
#%% 15.9.12 v3
'''
# print(all(num.isdigit() and 0 <= int(num) <= 255 for num in row[0].split('.')))

test = (
    ('10.0.1.1', True),
    ('10.1.1.a', False),
    ('10.1.1.260', False),
    ('10.0023.0123.0000015', True)
)
for row in test:
    print(all(num.isdigit() and 0 <= int(num) <= 255 for num in row[0].split('.')))
    print('answer:', row[1])
    print()
'''

#%% 15.9.13 - Интересные числа
'''
"""Интересные числа

На вход программе подаются два натуральных числа a и b. Напишите программу с использованием встроенной функции all() для обнаружения всех целых чисел в диапазоне [a;b], которые делятся на каждую содержащуюся в них цифру без остатка.

Формат входных данных
На вход программе подаются два натуральных числа a и b на отдельных строках.

Формат выходных данных
Программа должна вывести все числа из диапазона [a;b], удовлетворяющие условию задачи, на одной строке, разделяя их символом пробела.
"""

# 15.9.13 v1
# a, b = [input() for _ in range(2)]
# print(*filter(lambda x: all(x%int(num)==0 if int(num)!=0 else False for num in str(x)), range(int(a), int(b)+1)))

# test
test = (
    ('1', '25', '1 2 3 4 5 6 7 8 9 11 12 15 22 24'),
    ('20', '30', '22 24'),
    ('50', '150', '55 66 77 88 99 111 112 115 122 124 126 128 132 135 144')
)

for row in test:
    print('answer:', row[-1])
    print('result:', *filter(lambda x: all(x%int(num)==0 if int(num)!=0 else False for num in str(x)), range(int(row[0]), int(row[1])+1)))

    # print(*range(int(row[0]), int(row[1])+1))
    # print(*map(lambda x: [x % int(num) == 0 for num in str(x) if int(num) != 0], range(int(row[0]), int(row[1])+1)))
    print()
    # print(row)
'''

#%% 15.9.14 - Хороший пароль
'''
"""Хороший пароль

Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру, заглавную и строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.

Формат входных данных
На вход программе подаётся одна строка текста.

Формат выходных данных
Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае."""

password = input()
print(['NO', 'YES'][all((len(password) >= 7, 
                         any(symbol.isdigit() for symbol in password), 
                         any(symbol.istitle() for symbol in password), 
                         any(symbol.islower() for symbol in password)))])

# test
test = (
    ('abcABC9', 'YES'),
    ('abAB34', 'NO'),
    ('DFSDFSDFSDsdfjsdfnsm', 'NO'),
    ('zxcv123', 'NO')
)

for row in test:
    print('answer:', row[-1])
    print(['NO', 'YES'][all(((len(row[0]) >= 7), (any(symbol.isdigit() for symbol in row[0])), (any(symbol.istitle() for symbol in row[0])), (any(symbol.islower() for symbol in row[0]))))])

    print(((len(row[0]) >= 7), (any(symbol.isdigit() for symbol in row[0])), (any(symbol.istitle() for symbol in row[0])), (any(symbol.islower() for symbol in row[0]))))
    print()
'''


#%% 15.9.15 - Отличники

"""Отличники

Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK и решил убедиться, что в каждом классе есть хотя бы один отличник – ученик с оценкой 5 по контрольной работе. Напишите программу с использованием встроенных функций all(), any() для помощи Тимуру в проверке.

Формат входных данных
На вход программе подается натуральное число n – количество классов. Затем для каждого класса вводится блок информации вида:

натуральное число k – количество учеников в классе;
далее вводится k строк вида: фамилия оценка.
Формат выходных данных
Программа должна вывести YES, если в каждом классе есть хотя бы один отличник, и NO в противном случае."""

data = list()
n = int(input())
for i in range(n):
    data.append([])
    k = int(input())
    for __ in range(k):
        data[i].append(input().split(' ')[1])

print('YES' if all([any(student == '5' for student in clas) for clas in data]) else 'NO')
#print(data)
#print([[student == '5' for student in clas] for clas in data])

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
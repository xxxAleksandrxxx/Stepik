#15.9 base info
#%%
a = []
a1 = ()
a2 = {}
b = [[], []]
b1 = 
print(type(b1))
f = all(b1)
print(f)
#%% all()
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

#%% enumerate()
numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]

en = enumerate(numbers)
print(type(en))
print(*en)

#%% zip()
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = ['apple', 'banana', 'carrot']
z = zip(a, b, c)
print(type(z))
print(*z)
#%% zip - формируем словарь
name = ['Timur', 'Ruslan', 'Rustam']
age = [28, 21, 19]
my_dict = dict(zip(name, age))

print(my_dict)
for k, v in my_dict.items():
    print(k, v)

#%% zip - параллельный перебор по нескольким коллекциям
name = ['Timur', 'Ruslan', 'Rustam']
age = [28, 21, 19]
color = ('red', 'white', 'yellow', 'black')
for n, a, c in zip(name, age, color):
    print(n, a, c)

#%%
from itertools import zip_longest
name = ['Timur', 'Ruslan', 'Rustam']
age = [28, 21, 19]
color = ('red', 'white', 'yellow', 'black')
for n, a, c in zip_longest(name, age, color, fillvalue=0):
    print(n, a, c)

#%%
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

#%% 15.9.8

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
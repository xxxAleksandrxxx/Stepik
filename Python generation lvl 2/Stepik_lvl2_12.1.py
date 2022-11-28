# 12.1.1 
'''
#%%
import random
l = list()
for _ in range(100):
    l.append(random.randint(0, 100))

print(sorted(l))


#%%
import random
a = 0
b = 2.2
c = 1
l = list()
for _ in range(100):
    l.append(random.randrange(a, b))

print(sorted(l))

#%%
import random
l = list()
for _ in range(100):
    l.append(random.random())

print(sorted(l))

#%%
import random
l = list()
a = 0.9
b = 1
for _ in range(100000000):
    l.append(random.uniform(a, b))
    if l[-1] == b:
        print(l[-1])

#print(sorted(l))

# %%
l = list()
for i in range(1, 10):
    l.append(2**i - 1)
print(l)
'''
#%%
# 12.1.11
'''
Напишите программу, которая с помощью модуля random моделирует броски монеты. Программа принимает на вход количество попыток и выводит результаты бросков: Орел или Решка (каждое на отдельной строке).

Примечание. Например, при 
n
=
7
n=7 ваша программа может выводить:

Орел
Решка
Решка
'''
'''
import random

n = int(input())
for _ in range(n):
    print(('Орел', 'Решка')[random.random() > 0.5])
'''
'''
# v2
import random
coin = {1:'Орел', 2:'Решка'}
for _ in range(int(input())):
    print(coin[random.randint(1, 2)])
'''


#%%
# 12.1.12
'''
Напишите программу, которая с помощью модуля random моделирует броски игрального кубика c 
6
6 гранями. Программа принимает на вход количество попыток и выводит результаты бросков — выпавшее число, которое написано на грани кубика (каждое на отдельной строке).

Примечание. Например, при 
n
=
7
n=7 ваша программа может выводить:
5
5
6
6
2
6
2
'''
'''
# v1
import random
n = int(input())
for _ in range(n):
    print(random.randrange(1, 7))
'''
'''
# v2
import random
n = int(input())
for _ in range(n):
    print(random.randint(1, 6))
'''

#%%
# 12.1.13
'''
Напишите программу, которая с помощью модуля random генерирует случайный пароль. Программа принимает на вход длину пароля и выводит случайный пароль, содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).

Примечание 1. Символам A..Z английского языка соответствуют номера с 65 по 90 в таблице символов ASCII.

Примечание 2. Символам a..z английского языка соответствуют номера с 97 по 122 в таблице символов ASCII.

Примечание 3. Используйте функцию chr() для получения символа по его номеру в таблице символов ASCII.

 Примечание 4. Например, при длине пароля, равной 15 символам ваша программа может выводить:

peJFAmhqfaAeKDu
'''
'''
# v1
import random

length = int(input())
for _ in range(length):
    if random.randint(0, 1):
        print(chr(random.randint(65, 90)), end='')
    else:
        print(chr(random.randint(97, 122)), end='')
'''
'''
# v2
import random

length = int(input())
for _ in range(length):
    print((chr(random.randint(65, 90)), chr(random.randint(97, 122)))[random.randint(0, 1)], end = '')
'''

#%%
# 12.1.14
'''
Лотерейный билет содержит 7 чисел из диапазона от 1 до 49 (включительно).

Напишите программу, которая с помощью модуля random генерирует 7 различных случайных чисел для лотерейного билета. Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела.

Примечание. Убедитесь, что сгенерированные числа не содержат дубликатов.
'''
'''
# v1
import random
ticket = set()
while len(ticket) < 7:
    ticket.add(random.randint(1, 49))
print(*sorted(ticket))
'''

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

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
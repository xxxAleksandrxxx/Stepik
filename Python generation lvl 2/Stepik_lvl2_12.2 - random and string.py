
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
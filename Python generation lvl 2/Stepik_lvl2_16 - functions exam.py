#%% 16.1.15

"""Письмо для экзамена

Напишите функцию generate_letter(), которая будет собирать электронное письмо в соответствии с шаблоном:

To: <mail>
Приветствую, <name>!
Вам назначен экзамен, который пройдет <date>, в <time>.
По адресу: <place>. 
Экзамен будет проводить <teacher> в кабинете <number>. 
Желаем удачи на экзамене!
Функция должна получать на вход пять обязательных аргументов mail, name, date, time, place и два необязательных teacher, number и возвращать текст готового письма. При отсутствии аргумента teacher учителем будет Тимур Гуев, а если нет аргумента number, то кабинет будет 17.

Примечание 1. Следующий программный код:

print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 
                      'Часова 23, корпус 2', 'Василь Ярошевич', 23))
должен выводить:

To: lara@yandex.ru
Приветствую, Лариса!
Вам назначен экзамен, который пройдет 10 декабря, в 12:00.
По адресу: Часова 23, корпус 2. 
Экзамен будет проводить Тимур Гуев в кабинете 17. 
Желаем удачи на экзамене!

To: lara@yandex.ru
Приветствую, Лариса!
Вам назначен экзамен, который пройдет 10 декабря, в 12:00.
По адресу: Часова 23, корпус 2. 
Экзамен будет проводить Василь Ярошевич в кабинете 23. 
Желаем удачи на экзамене!"""

def generate_letter(mail, 
                    name, 
                    date, 
                    time, 
                    place, 
                    teacher='Тимур Гуев', 
                    number=17):
    return f'''To: {mail}
Приветствую, {name}!
Вам назначен экзамен, который пройдет {date}, в {time}.
По адресу: {place}. 
Экзамен будет проводить {teacher} в кабинете {number}. 
Желаем удачи на экзамене!'''

print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 
                      'Часова 23, корпус 2', 'Василь Ярошевич', 23))


#%% 16.1.16 - Печать таблицы / таблица

"""Pretty print

Напишите функцию pretty_print(), которая выводит содержимое списка с рамкой. 

Функция должна получать на вход один обязательный аргумент data – список, который следует вывести и два необязательных строковых односимвольных  аргумента side и delimiter и выводить содержимое списка в соответствии с примерами.

В случае если отсутствует аргумент side, то полагаем side='-', а если отсутствует аргумент delimiter, то полагаем delimiter='|'."""

def pretty_print(data, side='-', delimiter='|'):
    horizon_line = ' ' + side*(2 + 4*(len(data)-1)) + side*(sum(map(lambda x: len(str(x)), data)) - (len(data) - 1))
    print(horizon_line)
    for elem in data:
        print(delimiter, elem, end=' ')
    print(delimiter)
    print(horizon_line)

# pretty_print([10000, 100, 100, '12'])
pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


#%% 16.1.16 v2 - Печать таблицы / таблица
def pretty_print(data, side='-', delimiter='|'):
    st = f'{delimiter} ' +\
         f' {delimiter} '.join(map(str, data)) +\
         f' {delimiter}'
    horizon_line = f' {side*(len(st) - 2)}'
    print(horizon_line)
    print(st)
    print(horizon_line)

pretty_print([10, 1])
pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


#%% 16.3.1

"""Напишите функцию concat(), принимающую переменное количество аргументов и объединяющую их в одну строку через разделитель (sep). Если разделитель не задан, им служит пробел.

Примечание 1. Обратите внимание, что функция concat() должна принимать не список, а именно переменное количество аргументов."""

def concat(*arg, sep=' '):
    answer = ''
    for elem in arg:
        answer += str(elem) + sep
    return answer[:-len(sep)]

print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))

#%% 16.3.2

"""Перепишите функцию product_of_odds() в функциональном стиле с использованием встроенных функций filter() и reduce().

def product_of_odds(data):   # data - список целых чисел
    result = 1
    for i in data:
        if i % 2 == 1:
            result *= i
    return result
Примечание 1. Тестирующая система никак не "покарает" вас за неиспользование встроенных функций filter() и reduce(), однако лучше сделать это задание честно 😃."""

from functools import reduce
from operator import mul, mod

def product_of_odds(data):
    return reduce(mul, filter(lambda x: mod(x, 2)==1, data), 1)

d = range(10)

def product_of_odds_orig(data):   # data - список целых чисел
    result = 1
    for i in data:
        if i % 2 == 1:
            result *= i
    return result

print('answer', product_of_odds_orig(d))
print('result', product_of_odds(d))


#%% 16.3.3

"""Дан список слов words. Допишите код после оператора распаковки (*), который оборачивает в двойные кавычки все элементы списка words, а затем печатает результат на одной строке через пробел.

Примечание. Вспомните про встроенную функцию map() и анонимные функции lambda.
words = 'the world is mine take a look what you have started'.split()

print(*...)"""

words = 'the world is mine take a look what you have started'.split()

print(*map(lambda x: f'"{x}"', words))

# long
print(words)
answer = ''
for w in words:
    answer += f'"{w}" '
print(answer[:-1])


#%% 16.3.4

"""Дан список целых чисел numbers. Допишите код после оператора распаковки (*), для удаления из списка всех чисел-палиндромов и печати результата на одной строке через пробел.

Примечание. Вспомните про встроенную функцию filter() и анонимные функции lambda.

numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
print(*...)"""

numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
print(*filter(lambda x: str(x)!=str(x)[::-1], numbers))


#%% 16.3.5 

"""Дан список numbers, состоящий из кортежей. Допишите пропущенную часть программы, чтобы список sorted_numbers был упорядочен по убыванию среднего арифметического элементов кортежей списка numbers.

Примечание. Вспомните про анонимные функции lambda.
numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

sorted_numbers = sorted(numbers, ...)

print(sorted_numbers)"""

numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

sorted_numbers = sorted(numbers, key=lambda x: sum(x)/len(x), reverse=True)

print(sorted_numbers)


#%% 16.3.6

"""Напишите функцию call(), которая принимает произвольную функцию и аргументы для неё и делает вызов переданной функции, возвращая ее значение."""
# the answer:
def call(func, *arg):
    return func(*arg)
#--

def mul7(x):
    return x * 7


def add2(x, y):
    return x + y


def add3(x, y, z):
    return x + y + z


print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))
print('answer:')
print(70, 9, 80, False, sep='\n')


#%% 16.3.7

"""Напишите функцию compose(), которая принимает на вход две других одноаргументных функции f и g и возвращает новую функцию. Эта новая функция также должна принимать один аргумент x и применять к нему исходные функции в нужном порядке: для функций f и g порядок применения должен выглядеть, как f(g(x))."""

# result:
def compose(f, g):
    def inner_f(x):
        return f(g(x))
    return inner_f
#--

def add3(x):
    return x + 3


def mul7(x):
    return x * 7

print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))
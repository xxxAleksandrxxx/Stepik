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


#%% 16.3.8

"""Напишите функцию arithmetic_operation(), которая принимает символ одной из четырех арифметических операций (+, -, *, /) и возвращает функцию двух аргументов для соответствующей операции."""

# result:
from operator import add, sub, mul, truediv
from functools import reduce
def arithmetic_operation(symbol):
    operations = {'+':add, '-':sub, '*':mul, '/':truediv}
    def inner_function(a, b):
        return reduce(operations[symbol], [a, b])
    return inner_function
#--

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))


#%% 16.3.9

"""В одну строку

Дана строка из разделенных пробелами слов в разных регистрах. Напишите программу, которая отсортирует слова независимо от регистра, а затем выведет их. Отсортированные слова должны выводиться на печать в исходном регистре, в каком переданы программе на вход.

Формат входных данных
На вход программе подается строка из разделенных пробелами слов в разных регистрах.

Формат выходных данных
Программа должна вывести строку разделенных пробелом отсортированных слов в прежних регистрах.

Примечание 1. Решите задачу в одну строку кода 😎.

Примечание 2. Встроенная функция sorted() сортирует строки в лексикографическом порядке, но учитывает регистр буквы. Любая буква в верхнем регистре считается идущей раньше, чем буква в нижнем регистре."""

test = {q:'cate Frog cat FROGs bee CATERS mouse cATwalk dolphin mOus Cats CatAlo', a:'bee cat CatAlo cate CATERS Cats cATwalk dolphin Frog FROGs mOus mouse'}
text = test[q]
print('answer:')
print(test[a])
print('result:')

# text = input()
print(*sorted(text.split(), key=lambda x: x.lower()))


#%% 16.3.10

"""Гематрией слова называется сумма числовых значений входящих в него букв.

Для вычисления гематрии слова в этой задаче:

переведём слово в верхний регистр;
числовое значение буквы вычислим как код(буквы) - код(буквы A).
На вход программе подается натуральное число n, а затем n строк английских слов в разных регистрах.

Напишите программу, которая выводит слова в начальном регистре (каждое на отдельной строке) в порядке возрастания их гематрии. Если гематрия слов совпадает, они выводятся в алфавитном (лексикографическом) порядке.

Формат входных данных
На вход программе подается натуральное число n, а затем n строк английских слов в разных регистрах.

Формат выходных данных
Программа должна отсортировать слова в соответствии с условием задачи.

Примечание 1. Для получения кода символа воспользуйтесь встроенной функцией ord().

Примечание 2. Слова во входных данных могут повторяться."""

l = (
    ('basis', 'after', 'chief', 'agenda'),
    ('Basis', 'afTEr', 'CHief', 'agenda')
)
l = l[1]
# l = [input() for _ in range(int(input()))]
g = [sum([ord(letter.upper()) - ord('A') for letter in word]) for word in l]
answer = sorted(zip(g, l))
for elem in answer:
    print(elem[1])



#%% 16.3.11

"""Сортировка IP-адресов

IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающий по протоколу TCP/IP.

В 4-й версии IP-адрес представляет собой 32-битное число. Адрес записывается в виде четырёх десятичных чисел (октетов) со значением от 0 до 255, разделённых точками, например, 192.168.1.2.

Напишите программу, которая считывает IP-адреса и выводит их в порядке возрастания в соответствии с десятичным представлением.

Формат входных данных
На вход программе подается число n (n≥1) – количество IP-адресов. Затем n строк с корректными IP-адресами.

Формат выходных данных
Программа должна вывести IP-адреса в порядке возрастания в соответствии с десятичным представлением.

Чтобы перевести IP-адрес 192.168.1.2 в десятичную форму:
192*256**3 + 168*256**2 + 1**256**1 + 2*256**0 = 3232235778"""

# st = ['128.199.44.24', '128.199.201.245']
# adresses = ((int(a)*256**3 + int(b)*256**2 + int(c)*256 + int(d), ip) for ip in st for a, b, c, d in ip.split('.'))
# print(*adresses)
#%% 16.3.11 v1
# result:
st = [input() for _ in range(int(input()))]
dec_num = []
for adress in st:
    a, b, c, d = map(int, adress.split('.'))
    dec_num.append(a*256**3 + b*256**2 + c*256 + d)

answer = sorted(zip(dec_num, st))
for elem in answer:
    print(elem[1])
#--

#%% 16.3.11 v2

test = {
    q : ('128.199.44.24', '128.199.201.245', '143.198.168.95', '172.67.181.62', '172.67.222.111', '172.67.10.90', '45.8.106.59', '203.13.32.156', '172.67.181.194'),
    a : ('45.8.106.59', '128.199.44.24', '128.199.201.245', '143.198.168.95', '172.67.10.90', '172.67.181.62', '172.67.181.194', '172.67.222.111', '203.13.32.156')
}
st = test[q]


# st = [input() for _ in range(int(input()))]
answer = sorted(st, key=lambda ip: int(ip.split('.')[0])*256**3 + int(ip.split('.')[1])*256**2 + int(ip.split('.')[2])*256 + int(ip.split('.')[3]))
print(*answer, sep = '\n')


# # проверка
# print('answer - result')
# [print(f'{a} - {b}', sep = '\n') for a, b in zip(test[a], answer)]

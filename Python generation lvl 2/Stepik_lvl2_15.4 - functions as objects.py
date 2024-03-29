# 15.4
#%%
'''
def hello():
    """выводит привет"""
    print('hello!')

h = hello
h()
'''
#%%
'''
# Функция как аргумент для другой функции
def modul(x):
    """возвращает модуль числа"""
    return abs(x)

def sq(x):
    """возвращает квадрат числа"""
    return x**2

numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]
print(max(numbers))
print(max(numbers, key=modul))
print(max(numbers, key=sq))
'''

#%%
'''
def second(tuple0):
    """возвращает второй символ кортежа"""
    return tuple0[1]

points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]

print(sorted(points))  # отсортировали по первому элементу
print(sorted(points, key=second))  # отсортировали по второму эелементу
'''

#%%
'''
def generator0():
    """возвращает функцию print0"""
    def print0():
        """выводит текст Hello from function"""
        print('Hello from function')
    return print0

a = generator0()  # здесь нужны скобки т.к. нам нужен результат, а именно вызов еще одной фукнции
a()
'''
'''
#%%

def gen_sq_poynom(a, b, c):
    """возвращает polynom_x(x)"""
    def polynom_x(x):
        """возвращает polynom_x(x)"""
        return a*x**2 + b*x + c
    return polynom_x

gen_sq_poynom(a=1, b=2, c=3)(4)  # 4 передается как аргумент ф-ции polynom_x, a 1, 2, 3 как аргументы ф-ции gen_sq_poynom
'''

#%%
# 15.4.10 v1
'''
"""
Дан список numbers, содержащий кортежи чисел. Напишите программу, которая с помощью встроенных функций min() и max() выводит те кортежи (каждый на отдельной строке), которые имеют минимальное и максимальное среднее арифметическое значение элементов.
Примечание. Используйте необязательный аргумент key.
"""
def comparator(tuple0):
    """возвращает среднне арифм. из кортежа"""
    return sum(tuple0)/len(tuple0)


numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

print(min(numbers, key=comparator))
print(max(numbers, key=comparator))
'''
#%%
# 15.4.10 v2
'''
def comparator(tuple0):
    """возвращает ср.арифм из кортежа"""
    return sum(tuple0)/len(tuple0)

numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

print(*(func(numbers, key=comparator) for func in (min, max)), sep='\n')
'''

#%%
# 15.4.11 v1
'''
"""
Напишите программу, которая сортирует список points координат точек плоскости в соответствии с расстоянием от начала координат (точки (0;0)). Программа должна вывести отсортированный список.
"""
def comparator(tup):
    """возвращает рсстояние от 0,0 до коодинат из кортежа"""
    return (tup[0]**2 + tup[1]**2)**0.5

points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

points.sort(key = comparator)
print(points)
'''

#%%
# 15.4.12 v1
'''
"""
Дан список numbers, содержащий кортежи чисел. Напишите программу, которая сортирует и выводит список numbers в соответствии с суммой минимального и максимального элемента кортежа.
"""
def comparator(tup):
    """возвращает сумму мин и макс значения из преданного кортежа"""
    return min(tup) + max(tup)

numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]

numbers.sort(key=comparator)

print(numbers)
'''
# 15.4.12 v2
'''
numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]

numbers.sort(key=lambda x: min(x)+max(x))

print(numbers)
'''

#%%
# 15.4.13 Сортируй как хочешь
"""
Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).

Напишите программу сортировки списка спортсменов по указанному полю:
1: по имени;
2: по возрасту;
3: по росту;
4: по весу.
Формат входных данных
На вход программе подается натуральное число от 1 до 4 – номер поля по которому требуется отсортировать список.
Примечание. Решите задачу без использования условного оператора.
"""
'''
# v1
def comparator(tup):
    """возвращает i-е поле кортежа с данными"""
    return tup[i-1]


athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

i = int(input())
athletes.sort(key=comparator)
for athlet in athletes:
    print(*athlet)
'''
'''
# v2
athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

i = int(input())
athletes.sort(key=lambda x: x[i-1])
for athlet in athletes:
    print(*athlet)
'''
'''
# v3
def comparator(i):
    def s(tup):
        return tup[i-1]
    return s

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

i = int(input())
k = comparator(i)

athletes.sort(key=k)
for ath in athletes:
    print(*ath)
'''


#%%
# 15.4.14 - Математические функции

"""
Напишите программу, которая принимает число и название функции, а выводит результат применения функции к данному числу.

Список возможных функций:

квадрат: функция принимает число и возвращает его квадрат;
куб: функция принимает число и возвращает его куб;
корень: функция принимает число и возвращает корень квадратный из этого числа;
модуль: функция принимает число и возвращает его модуль;
синус: функция принимает число (в радианах) и возвращает синус этого числа.
Формат входных данных
На вход программе подается целое число и название функции, записанные на отдельных строках.

Формат выходных данных
Программа должна выдать результат применения функции к числу.

Примечание. Решите задачу без использования условного оператора.
"""
# 15.4.14 v1
'''
from math import sin

def sq(num0):
    return num0**2

def qube(num0):
    return num0**3

def sqw(num0):
    return num0**0.5

funcs = {'квадрат':sq, 'куб':qube, 'корень':sqw, 'модуль':abs, 'синус':sin}

num = int(input())
f = input()

print(funcs[f](num))
'''

# 15.4.14 v2
'''
def pow(power0):
    def number(num0):
        return num0**power0
    return number

num = int(input())
f = input()
# num = 10
# f = 'корень'
funcs = {'квадрат':pow(2), 'куб':pow(3), 'корень':pow(0.5), 'модуль':abs, 'синус':sin}

print(funcs[f](num))
'''


# 15.4.15 Интересная сортировка-1
"""
На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. При этом, если два числа имеют одинаковую сумму цифр, следует сохранить их взаиморасположение в начальном списке.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
Формат выходных данных
Программа должна вывести отсортированный список чисел в соответствии с условием задачи, разделяя его элементы одним пробелом.
"""
# 15.4.15 v1
'''
test1 = '12 14 79 7 4 123 45 90 111'
answer1 = '12 111 4 14 123 7 45 90 79'
numbers = [num for num in test1.split()]
numbers = [num for num in input().split()]
# print(numbers)
numbers.sort(key=lambda x: sum([int(num) for num in x]), reverse=False)
print(*numbers)
# print(answer1)
'''
# 15.4.15 v2
''''
numbers = [num for num in input().split()]
numbers.sort(key=lambda x: sum(map(int, x)))
print(*numbers)
'''

#%%
# 15.4.16 - Интересная сортировка-2
"""
Интересная сортировка-2

На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.

Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. При этом, если у двух чисел одинаковая сумма цифр, их следует вывести в порядке неубывания.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

Формат выходных данных
Программа должна вывести отсортированный список чисел в соответствии с условием задачи, разделяя его элементы одним пробелом.
"""
# 15.4.16 v1
'''
def my_sort(str_0):
    ls = str_0.split()
    print(type(ls), ls)

def my_comparator(number):
    return sum([int(num) for num in number])

# test1 = '111 14 79 7 4 123 90 45 12 171'
# answer1 = '12 111 4 14 123 7 45 90 171 79'
# test2 = '19 20 21 22 23 10 11 12 13 14 15 16 17 18'
# answer2 = '10 11 20 12 21 13 22 14 23 15 16 17 18 19'
# test3 = '100 10 451 541 514 145'

# print(test1)
# numbers = test1.split()
numbers = input().split()
numbers.sort(key=lambda x: int(x), reverse=False)
numbers.sort(key=(my_comparator))

# print('a0', answer1)
# print('a1', *numbers)

print(*numbers)

# my_sort(test1)
'''
#%%
# 15.4.16 v2 - используем особенность сравнения кортежей - кортежи сравниваются поэлеменно; если совпадут первые элементы (суммы), то будут сравниваться вторые элементы

test1 = '111 14 79 7 4 123 90 45 12 171'
answer1 = '12 111 4 14 123 7 45 90 171 79'
numbers = test1.split()
print(answer1)

def comparator(number):
    """
    Возвращает кортеж из суммы цифр числа и самого числа. Так как кортежи сравниваются поэлементно, то, если совпадут суммы, будут сравниваться сами числа.
    """
    return sum(int(digit) for digit in number), int(number)

# numbers = input().split()
numbers.sort(key= comparator)
print(*numbers)

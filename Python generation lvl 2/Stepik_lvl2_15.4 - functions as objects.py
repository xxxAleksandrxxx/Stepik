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
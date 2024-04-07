# 3.6.10
# Функция calculate_it()
# Реализуйте функцию calculate_it(), которая принимает один или более аргументов в следующем порядке:
# func — произвольная функция
# *args — переменное количество позиционных аргументов, каждый из которых является произвольным объектом
# Функция должна возвращать кортеж, первым элементом которого является возвращаемое значение функции func при вызове с аргументами *args, а вторым — примерное время (в секундах), затраченное на вычисление этого значения.

# import time
# def calculate_it(func, *args):
#     time_start = time.monotonic()
#     result = func(*args)
#     time_stop = time.monotonic()
#     return (result, time_stop - time_start)

# def my_sum(*args):
#     result = 0
#     for arg in list(args):
#         result += arg
#     return result

# def my_mult(*args):
#     result = 1
#     for arg in args:
#         result *= arg
#     return result

# def check_args(*args):
#     print("args")
#     print(args)
#     for arg in args:
#         print(arg)

# def check_kwargs(**kwargs):
#     print("kwargs:")
#     print(kwargs)
#     for kwarg in kwargs:
#         print(kwarg)


# if __name__ == "__main__":
#     print(calculate_it(my_sum, 1, 2, 3, 4, 5))



##########################################
# 3.6.11
# Функция get_the_fastest_func()
# Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:
# funcs — список произвольных функций
# arg — произвольный объект
# Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила на вычисление значения при вызове с аргументом arg наименьшее количество времени.
# Примечание. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_the_fastest_func(), но не код, вызывающий ее.

# import time

# def get_the_fastest_func(funcs, arg):
#     '''
#     calculates execution time of function from funcs list
#     finds the fastest one
#     returns fastest function
#     '''
#     time_fastest = float('inf')
#     for func in funcs:
#         time_start = time.monotonic()
#         func(arg)
#         time_end = time.monotonic()
#         time_execution = time_end - time_start
#         if time_execution < time_fastest:
#             time_fastest = time_execution
#             func_fastest = func
#     return func_fastest



##########################################
# 3.6.12
# find what function works faster

# import time
# from math import factorial

# def factorial_recurrent(n):
#     if n == 0:
#         return 1
#     return n * factorial_recurrent(n - 1)

# def factorial_classic(n):
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f

# def calc_execution_time(n, *funcs):
#     for func in funcs:
#         print(func.__name__)
#         time_start = time.monotonic()
#         for _ in range(100000):
#             func(n)
#         time_end = time.monotonic()
#         print("execution time:", f"{time_end - time_start:.1f}")

# if __name__ == "__main__":
#     calc_execution_time(900, factorial, factorial_recurrent, factorial_classic)



##########################################
# 3.6.13
# Which way is faster to create a list?
# import time

# def for_and_append(n):
#     my_list = list()
#     for i in range(n):
#         my_list.append(i)
#     return my_list

# def list_comprehension(n):
#     return [i for i in range(n)]

# def execution_time(func, n):
#     time_start = time.monotonic()
#     func(n)
#     time_end = time.monotonic()
#     return time_end - time_start

# if __name__ == "__main__":
#     n = 10000000
#     for func in [for_and_append, list_comprehension]:
#         print(execution_time(func, n))



##########################################
# 3.6.14
# Вам доступны три реализации функции, которая принимает в качестве аргумента итерируемый объект и возвращает список, элементами которого являются элементы переданного итерируемого объекта:
# с использованием цикла for и метода append()
# с использованием списочного выражения
# с использованием встроенной функции list()
# Определите, какая функция быстрее создаст и вернет список на основе итерируемого объекта range(100_000).
# import time

# def for_and_append(iter):
#     iter_list = list()
#     for elem in iter:
#         iter_list.append(elem)
#     return iter_list

# def list_compr(iter):
#     return [elem for elem in iter]

# def list_func(iter):
#     return list(iter)

# def execution_time(func, arg):
#     time_start = time.monotonic()
#     func(arg)
#     time_end = time.monotonic()
#     return time_end - time_start

# if __name__ == "__main__":
#     arg = [i for i in range(10000000)]
#     for func in [for_and_append, list_compr, list_func]:
#         print(func.__name__, end=" ")
#         print(f"{execution_time(func, arg):.4f}")


# import time 
# time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)
# time_obj = time.struct_time(time_tuple)
# print(time_obj)
# print(time_obj.tm_year, time_obj[0])
# print(time_obj.tm_mon, time_obj[1])
# print(time_obj.tm_mday, time_obj[2])


##########################################
##########################################
# 3.7
# import calendar, locale
# def print_week_days():
#     for day in calendar.day_name:
#         print(day.title(), end=" ")
#     print()

# locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
# print_week_days()

# locale.setlocale(locale.LC_ALL, "")
# print_week_days()

# import calendar
# d_list = [day.upper() for day in calendar.day_name]
# print(*d_list)
# d_num_list = [getattr(calendar, day) for day in d_list]
# print(*d_num_list)


# import calendar
# print(*calendar.monthcalendar(2024, 4), sep="\n")


# import calendar
# print(calendar.month(2024, 4))


# import calendar
# print(calendar.calendar(2024))


##########################################
# 3.7.7
# Напишите программу, которая определяет, является ли год високосным.
# import calendar

# def check_year(year_range):
#     for year in year_range:
#         print(calendar.isleap(year))

# if __name__ == "__main__":
#     y = [1999, 2000, 2001, 2002]
#     check_year(y)

import calendar

def check_year(year_range):
    for year in year_range:
        print(calendar.isleap(year))

if __name__ == "__main__":
    y = [int(input()) for _ in range(int(input()))]
    check_year(y)
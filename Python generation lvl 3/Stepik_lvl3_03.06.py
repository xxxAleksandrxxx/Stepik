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

import time

def get_the_fastest_func(funcs, arg):
    '''
    calculates execution time of function from funcs list
    finds the fastest one
    returns fastest function
    '''
    time_fastest = float('inf')
    for func in funcs:
        time_start = time.monotonic()
        func(arg)
        time_end = time.monotonic()
        time_execution = time_end - time_start
        if time_execution < time_fastest:
            time_fastest = time_execution
            func_fastest = func
    return func_fastest

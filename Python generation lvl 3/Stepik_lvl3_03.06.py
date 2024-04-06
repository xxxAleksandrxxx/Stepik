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



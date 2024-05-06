# #######################
# 4.6.15
# Одинокая функция
# Дан pickle файл, содержащий единственную сериализованную функцию. Напишите программу, которая вызывает данную функцию с заданными аргументами и выводит возвращаемое значение функции.

# import pickle
# import sys

# def run_pickle_func1(pickle_func, args:list):
#     with open(pickle_func, "rb") as pkf:
#         func = pickle.load(pkf)
#         print(func(*args))


# def run_pickle_func2(pickle_func, args:list):
#     with open(pickle_func, "rb") as pkf:
#         print(pickle.load(pkf)(*args))

# if __name__ == "__main__":
#     pickle_func, *args = [line.strip() for line in sys.stdin]
#     run_pickle_func2(pickle_func, args)


# #######################
# 4.6.16
# Ты не пройдешь
# Реализуйте функцию filter_dump(), которая принимает три аргумента в следующем порядке:
# filename — название pickle файла, например, data.pkl
# objects — список произвольных объектов
# typename — тип данных
# Функция должна создавать pickle файл с названием filename, который содержит сериализованный список только тех объектов из списка objects, тип которых равен typename.

import pickle

def filter_dump(f_name, obj_in, type_name):
    with open(f_name, "wb") as f_pkl:
        obj_pkl = [elem for elem in obj_in if type(elem) == type_name]
        pickle.dump(obj=obj_pkl, file=f_pkl)



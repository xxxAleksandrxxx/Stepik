# #######################
# 4.6.15
# Одинокая функция
# Дан pickle файл, содержащий единственную сериализованную функцию. Напишите программу, которая вызывает данную функцию с заданными аргументами и выводит возвращаемое значение функции.

import pickle
import sys

def run_pickle_func(pickle_func, args:list):
    with open(pickle_func, "rb") as pkf:
        func = pickle.load(pkf)
        print(func(*args))

if __name__ == "__main__":
    pickle_func, *args = [line.strip() for line in sys.stdin]
    run_pickle_func(pickle_func, args)



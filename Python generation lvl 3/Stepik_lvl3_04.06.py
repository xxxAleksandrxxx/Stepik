# #######################
# 4.6.13
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
# 4.6.14
# Ты не пройдешь
# Реализуйте функцию filter_dump(), которая принимает три аргумента в следующем порядке:
# filename — название pickle файла, например, data.pkl
# objects — список произвольных объектов
# typename — тип данных
# Функция должна создавать pickle файл с названием filename, который содержит сериализованный список только тех объектов из списка objects, тип которых равен typename.

# import pickle

# def filter_dump(f_name, obj_in, type_name):
#     with open(f_name, "wb") as f_pkl:
#         obj_pkl = [elem for elem in obj_in if type(elem) == type_name]
#         pickle.dump(obj=obj_pkl, file=f_pkl)



# #######################
# 4.6.15
# Напишите программу, которая вычисляет контрольную сумму для объекта, содержащегося в pickle файле, и сравнивает ее с данным целым числом.
# По каналу связи передается pickle файл, содержащий сериализованный словарь или список, и целое число — контрольная сумма, которая вычисляется по следующему правилу:
# для словаря — сумма всех целочисленных ключей (тип int)
# для списка — произведение минимального и максимального целочисленных элементов (тип int)

import pickle
import sys
from math import inf

def checksum1(file_pkl):
    with open(file_pkl, "rb") as f_pkl:
        pkl_obj = pickle.load(f_pkl)
        if isinstance(pkl_obj, dict):
            sum = 0
            for elem in pkl_obj:
                if isinstance(elem, int):
                    sum += elem
            return str(sum)
        elif isinstance(pkl_obj, list):
            l_min = inf
            l_max = 0
            for elem in pkl_obj:
                if isinstance(elem, int):
                    if  elem > l_max:
                        l_max = elem
                    if elem < l_min:
                        l_min = elem
            if l_min == inf and l_max == 0:
                return("0")
            else:
                return str(l_min*l_max)



def checksum2(file_pkl):
    with open(file_pkl, 'rb') as f:
        obj = pickle.load(f)
        lst = [i for i in obj if type(i) == int] or [0]
        check = sum(lst) if type(obj) == dict else max(lst)*min(lst)
        # print(['Контрольные суммы не совпадают', 'Контрольные суммы совпадают'][sm == check])
    return str(check)


def checksum3(file_pkl):
    filename = file_pkl
    with open(filename, 'rb') as file:
        data = pickle.load(file)
        if isinstance(data, dict):
            tmp = [key for key in data if type(key) is int]
            res = sum(tmp) if tmp else 0
        elif isinstance(data, list):
            tmp = list(filter(lambda x: type(x) is int, data))
            res = min(tmp) * max(tmp) if tmp else 0
    return res


from time import monotonic
def execution_time(func, *args, n=1000):
    t0 = monotonic()
    for _ in range(n):
        func(*args)
    t1 = monotonic()
    print(f"{func.__name__:<20} {t1-t0:.2f}")

if __name__ == "__main__":
    # obj, ch_sum = [elem.strip() for elem in sys.stdin]
    # print("Контрольные суммы совпадают" if ch_sum == checksum1(obj) else "Контрольные суммы не совпадают")

    # check_func = checksum2
    objects = ["etc/data1.pkl", "etc/data2.pkl", "etc/data3.pkl"]
    ch_sums = ["3023", "4", "0"]
    answers = ["Контрольные суммы не совпадают", "Контрольные суммы не совпадают", "Контрольные суммы совпадают"]
    # for obj, ch, answ in zip(objects, ch_sums, answers):
    #     print("ok" if ch == check_func(obj) else "wrong")

    funcs = [checksum1, checksum2, checksum3]
    for func in funcs:
        execution_time(func, objects[0], n=100000)

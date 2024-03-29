# 15.5 функции выслего порядка
#%%
# релизуем функцию map - применяет указанную в аргументах функцию к каждому элементу списка
def my_map(my_func, my_list):
    """применяет функцию my_func к каждому элементу списка my_list"""
    answer = list()
    for elem in my_list:
        answer.append(my_func(elem))
    return answer


a = [1, 2, -3, -4, -5]
print(type(my_map(lambda x: x**2, a)))

#%%
# реализуем функцию filter - отбирает часть списка по определенному критерию. критерий передаем в виде функции (должна возвращать True или False)
def my_filter(my_func, my_list):
    """отбирает часть списка my_list по критерию, передваемому функцияе my_func (возяращает True / False)"""
    answer =list()
    for elem in my_list:
        if my_func(elem) == True:
            answer.append(elem)
    return answer


a = [1, 2, -3, -4, -5]
print(my_filter(lambda x: x>0, a))

#%%
# релизуем функцию reduce - агрегирует элемнты из списка начиная с определенного значения - сумиирует или перемножает числа из преданного списка
def my_reduce(my_func, my_list, initial_value):
    result = initial_value
    for elem in my_list:
        result = my_func(result, elem)
    return result


def my_sum(a, b):
    return a + b

def my_mult(a, b):
    return a * b

a = [0, 1, 2, 3, 4]
print(my_reduce(my_sum, a, 0))
print(my_reduce(my_mult, a, 1))



# 15.5.10
"""
Напишите программу, которая с помощью функции map() округляет все элементы списка numbers до 2 десятичных знаков, а затем выводит их, каждый на отдельной строке.
"""
'''
#%%
# 15.5.10 v1
def my_map(my_func, my_list):
    answer = list()
    for elem in my_list:
        answer.append(my_func(elem))
    return answer

def okrugl_2(my_number):
    return float(f'{my_number:.2f}')

numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]

print(*my_map(okrugl_2, numbers), sep='\n')

#%%
# 15.5.10 v2
def my_map(my_func, my_list):
    answer = list()
    for elem in my_list:
        answer.append(my_func(elem))
    return answer

numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
print(*my_map(lambda x: round(x, 2), numbers), sep='\n')
'''


# 15.5.11
"""
Напишите программу, которая с помощью функций filter() и map() отбирает из заданного списка numbers трёхзначные числа, дающие при делении на 5 остаток 2, и выводит их кубы, каждый в отдельной строке.

Примечание. Остаток 2 при делении на 5 должно давать само число, а не его куб.
"""

#%%
'''
# 15.5.11 v1
# def my_map(my_func, my_list):
#     answer = list()
#     for elem in my_list:
#         answer.append(my_func(elem))
#     return answer

def my_filter(my_predicat, my_list):
    answer = list()
    for elem in my_list:
        if my_predicat(elem):
            answer.append(elem)
    return answer

def predicat(my_elem):
    return my_elem % 5 == 2 if len(str(my_elem)) == 3 else False


numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

for elem in my_filter(predicat, numbers):
    print(elem**3)
'''


# 15.5.12
"""
Напишите программу для вычисления и вывода суммы квадратов элементов списка numbers.
Примечание. Попробуйте решить задачу двумя способами: с помощью функции reduce(), и с помощью функций map() и sum().
"""

#%%
# 15.5.12 v1 - reduce
def my_reduce(my_func, my_list, init_value):
    answer = init_value
    for elem in my_list:
        answer = my_func(answer, elem)
    return answer

def sum_sq(num_a, num_b):
    return num_a + num_b**2

numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

print(my_reduce(sum_sq, numbers, 0))

#%%
 # 15.5.12 v2 - map() and sum()
def my_map(my_func, my_list):
    answer = list()
    for elem in my_list:
        answer.append(my_func(answer))
    return answer

numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

print(sum(map(lambda x: x**2, numbers)))

#%%
# 15.5.13
"""
Напишите программу для вычисления и вывода суммы квадратов двузначных чисел, которые делятся на 7 без остатка.

Примечание 1. При решении задачи используйте функции filter(), map() и sum().
Примечание 2. На 7 должно делиться исходное двузначное число, а не его квадрат.
Примечание 3. Не забывайте про отрицательные двузначные числа.
"""
#%% # 15.5.13 v1
def my_map(my_func, my_list):
    answer = list()
    for elem in my_list:
        answer.append(my_func(elem))
    return answer

def my_filter(my_predicat, my_list):
    answer = list()
    for elem in my_list:
        if my_predicat(elem):
            answer.append(elem)
    return answer

def predicat(my_elem):
    return my_elem % 7 == 0 if len(str(abs(my_elem))) == 2 else False

numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]

print(sum(my_map(lambda x: x**2, my_filter(predicat, numbers))))
# print(my_filter(predicat, numbers))
# print(my_map(lambda x: x**2, my_filter(predicat, numbers)))
# print(sum(my_map(lambda x: x**2, my_filter(predicat, numbers))))



#%%
# 15.5.14
"""
Напишите функцию func_apply(), принимающую на вход функцию и список значений и возвращающую список, в котором каждое значение будет результатом применения переданной функции к переданному списку.
"""

def func_apply(my_func, my_list):
    answer = list()
    for elem in my_list:
        answer.append(my_func(elem))
    return answer


def add3(x):
    return x + 3

def mul7(x):
    return x * 7

print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))
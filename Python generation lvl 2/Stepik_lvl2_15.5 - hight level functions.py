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
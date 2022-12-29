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

#%%
# 12.3.6 Метод Монте-Карло
'''
Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью системы неравенств:
-2 <= x <= 2
-2 <= y <= 2
x^3 + y^4 + 2 >= 0
3x + y^2 <= 2
'''
'''
# v1
from random import uniform
n = 10**6
k = 0
s0 = 16
for _ in range(n):
    x = uniform(-2, 2)
    y = uniform(-2, 2)
    if (x**3 + y**4 + 2 >= 0) and (3*x + y**2 <= 2):
        k += 1
print(s0*k/n)
'''
'''
# v2
import matplotlib.pyplot as plt
from random import uniform
n = 10**4
k = 0
s0 = 16
X, Y = list(), list()
for _ in range(n):
    x = uniform(-2, 2)
    y = uniform(-2, 2)
    if (x**3 + y**4 + 2 >= 0) and (3*x + y**2 <= 2):
        X.append(x)
        Y.append(y)
        k += 1
# plt.scatter(X, Y, s=1)
# print(k)
print(s0*k/n)
'''

# 12.3.8 расчитать число pi
'''
Напишите программу, которая при помощи метода Монте-Карло определяет приближённое значение числа π.
y^2 + x^2 = 1^2
-1 <= x <= 1
-1 <= y <= 1
'''
'''
import matplotlib.pyplot as plt
from random import uniform

n = 10**4
k = 0
s0 = 4
x_in, x_out, y_in, y_out = list(), list(), list(), list()
for _ in range(n):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    if x**2 + y**2 <= 1:
        x_in.append(x)
        y_in.append(y)
        k += 1
    else:
        x_out.append(x)
        y_out.append(y)
plt.figure(figsize = (6, 6), dpi=80)
plt.scatter(x_in, y_in, s=1, c='b')
plt.scatter(x_out, y_out, s=1, c='r')
print('k =',k)
print(f'pi = 4 * {k}/{n} = {4 * k/(n)}')
'''
'''
# богосорт - болотная сортировка
from random import shuffle
from random import randint

def if_sorted(my_list):
    for i in range(len(my_list) - 1):
        if my_list[i+1] < my_list[i]:
            return False
    return True

def bogosort(my_list):
    k = 0
    while not if_sorted(my_list):
        shuffle(my_list)
        k += 1
    return k, my_list

n = 12
list_nonsorted = [randint(1, n) for _ in range(n)]
print('list before:', list_nonsorted)
print('sorted status:', if_sorted(list_nonsorted))
print()
k, list_sorted = bogosort(list_nonsorted)
print('list after:', list_sorted)
print('sorted status:', if_sorted(list_sorted))
print('всего итераций:', k)
'''
'''
list before: [4, 5, 12, 9, 6, 4, 1, 6, 2, 10, 10, 11]
sorted status: False

list after: [1, 2, 4, 4, 5, 6, 6, 9, 10, 10, 11, 12]
sorted status: True
всего итераций: 101324621
'''

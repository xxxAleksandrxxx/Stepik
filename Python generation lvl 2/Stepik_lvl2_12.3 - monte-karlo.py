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
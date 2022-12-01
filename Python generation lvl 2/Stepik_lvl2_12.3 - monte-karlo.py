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


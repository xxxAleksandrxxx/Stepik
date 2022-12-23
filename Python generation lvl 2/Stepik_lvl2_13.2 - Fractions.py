#%%
# 13.2.6
'''
Десятичные числа хранятся в списке numbers в виде строк. Дополните приведенный код, чтобы он для каждого десятичного числа вывел его представление в виде обыкновенной дроби в формате:

десятичное число = обыкновенная дробь

numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
'''

from fractions import Fraction

numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']

for num in numbers:
    print('{} = {}'.format(num, Fraction(num)))


#%%
# 13.2.7
'''
Десятичные числа, разделенные символом пробела, хранятся в строковой переменной s. Дополните приведенный код, чтобы он вывел сумму наибольшего и наименьшего числа в виде обыкновенной дроби.
s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
'''
'''
# v1
from fractions import Fraction
s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
s_list = [Fraction(num) for num in s.split()]
print(min(s_list) + max(s_list))
'''

# v2
from fractions import Fraction
s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
s_list = list(map(Fraction, s.split()))
print(min(s_list) + max(s_list))


#%%
# 13.2.8 Сократите дробь
'''
Даны два натуральных числа m и n. Напишите программу, которая сокращает дробь m/n и выводит ее.

Формат входных данных
На вход программе подается два натуральных числа, числитель и знаменатель дроби, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести ответ на задачу.
'''
from fractions import Fraction
m, n = [input() for _ in range(2)]
print(Fraction(m)/Fraction(n))

#%%
# 13.2.9 Операции над дробями
'''
Даны две дроби в формате a/b. Напишите программу, которая вычисляет и выводит их сумму, разность, произведение и частное.

Формат входных данных
На вход программе подаются две ненулевые дроби, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести сумму, разность, произведение и частное двух дробей.

Примечание. Обратите внимание на третий тест: исходные дроби сокращать не нужно, а результат нужно.
'''
'''
# v1
from fractions import Fraction

def fr(str):
    m, n = str.split('/')
    return Fraction(m)/Fraction(n)

num = [input() for _ in range(2)]
num1, num2 = [fr(elem) for elem in num]

print('{} + {} = {}'.format(num[0], num[1], num1 + num2))
print('{} - {} = {}'.format(num[0], num[1], num1 - num2))
print('{} * {} = {}'.format(num[0], num[1], num1 * num2))
print('{} / {} = {}'.format(num[0], num[1], num1 / num2))
'''
'''
# v2
from fractions import Fraction
num1, num2 = [input() for _ in range(2)]
print('{} + {} = {}'.format(num1, num2, Fraction(num1) + Fraction(num2)))
print('{} - {} = {}'.format(num1, num2, Fraction(num1) - Fraction(num2)))
print('{} * {} = {}'.format(num1, num2, Fraction(num1) * Fraction(num2)))
print('{} / {} = {}'.format(num1, num2, Fraction(num1) / Fraction(num2)))
'''

#%%
# 13.2.10 Сумма дробей 1
'''
На вход программе подается натуральное число n. Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения 
1/1^2 + 1/2^2 + 1/3^2 + ... + 1/n^2
Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание 1. Результирующая дробь должна быть несократимой.
'''
'''
# v1
from fractions import Fraction
s = [Fraction('1/{}'.format(i))**2 for i in range(1, int(input())+1)]
print(sum(s))
'''

# v2
from fractions import Fraction
s = [Fraction(1, i**2) for i in range(1, int(input())+1)]
print(sum(s))


#%%
# 13.2.11 Сумма дробей 2
'''
На вход программе подается натуральное число n. Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения 
1/1! + 1/2! + 1/3! + ... + 1/n!
Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание 1. Результирующая дробь должна быть несократимой.
'''
'''
# v1
from fractions import Fraction
from math import factorial

s = [Fraction(1, factorial(i)) for i in range(1, int(input()) + 1)]
print(sum(s))
'''
'''
# v2
from fractions import Fraction
s = []
f = 1
for i in range(1, int(input()) + 1):
    f *= i
    s.append(Fraction(1, f))
print(sum(s))
'''

# v3
from fractions import Fraction
s = 0
f = 1
for i in range(1, int(input()) + 1):
    f *= i
    s += Fraction(1, f)
print(s)


#%%
# 13.2.12 Юный математик 🌶️
'''
Дима учится в седьмом классе и сейчас они проходят обыкновенные дроби с натуральными числителем и знаменателем. Вчера на уроке математики Дима узнал, что дробь называется правильной, если ее числитель меньше знаменателя, и несократимой, если нет равной ей дроби с меньшими натуральными числителем и знаменателем.

Дима очень любит математику, поэтому дома он долго экспериментировал, придумывая и решая разные задачки с правильными несократимыми дробями. Одну из этих задач Дима предлагает решить вам с помощью компьютера.

На вход программе подается натуральное число n. Напишите программу, которая находит наибольшую правильную несократимую дробь с суммой числителя и знаменателя равной n.

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание. Возможно вам потребуется функция gcd(), которая позволяет находить наибольший общий делитель (НОД) двух чисел. Функция реализована в модуле math.
'''
'''
# v1
from fractions import Fraction

n = int(input())
drobi = set()
for znam in range(n):
    for chisl in range(znam):
        number = Fraction(chisl,znam)
        if number.as_integer_ratio()[0] + number.as_integer_ratio()[1] == n:
            # print(chisl, znam, n)
            drobi.add(number)

print(max(drobi))
'''

# v2
from fractions import Fraction

n = int(input())
i = n//2
while Fraction(i, n - i).numerator != i:
    i -= 1

print(Fraction(i, n - i))


#%%
# 13.2.13 Упорядоченные дроби
'''
На вход программе подается натуральное число n. Напишите программу, которая выводит в порядке возрастания все несократимые дроби, заключённые между 0 и 1, знаменатель которых не превосходит n.

Формат входных данных
На вход программе подается натуральное число n,n>1.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание. Возможно вам потребуется функция gcd(), которая позволяет находить наибольший общий делитель (НОД) двух чисел. Функция реализована в модуле math.
'''

# v1
from fractions import Fraction
n = int(input())
answer = set()
for i in range(2, n+1):
    for j in range(1, i):
        answer.add(Fraction(j, i))

for elem in sorted(answer):
    print(elem)
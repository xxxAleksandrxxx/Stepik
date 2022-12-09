#%%
# 13.3
a = 4j
print(a, type(a))
z = 1 + 2j
print(z.real)
print(z.imag)


#%%
# 13.3.12 Операции над комплексными числами
'''
Даны два комплексных числа. Напишите программу, которая вычисляет и выводит их сумму, разность и произведение.

Формат входных данных
На вход программе подается два комплексных числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести ответ на задачу.
'''
'''
# v1
num = [complex(input()) for _ in range(2)]
print('{} + {} = {}'.format(num[0], num[1], num[0]+num[1]))
print('{} - {} = {}'.format(num[0], num[1], num[0]-num[1]))
print('{} * {} = {}'.format(num[0], num[1], num[0]*num[1]))
'''

# v2
num1, num2 = [complex(input()) for _ in range(2)]
print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')


#%%
# 13.3.13 
'''
Комплексные числа хранятся в списке numbers. Дополните приведенный код так, чтобы он вывел комплексное число с наибольшим модулем и сам модуль числа на отдельных строках.

Примечание. Модуль комплексного числа можно вычислить с помощью встроенной функции abs().
numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
'''
'''
# v1
numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
n_abs = {abs(number):number for number in numbers}
print(n_abs[max(n_abs)], max(n_abs), sep = '\n')
'''

# v2
numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
answer = 0
for number in numbers:
    if abs(number) > abs(answer):
        answer = number

print(answer, abs(answer), sep='\n')
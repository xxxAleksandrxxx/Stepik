#%%
# 9. Сложение матриц
'''
Напишите программу для вычисления суммы двух матриц.
Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрицах, затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.
Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
'''
'''
# v1
n, m = map(int, input().split())
a = [[int(elem) for elem in input().split()] for _ in range(n)]
b = input()
b = [[int(elem) for elem in input().split()] for _ in range(n)]

c = [[0]*m for _ in range(n)]
for i in range(n):
	for j in range(m):
		c[i][j] = a[i][j]+b[i][j]
		
for row in c:
	for el in row:
		print(el, end=' ')
	print()
'''
#%%
# 10. Умножение матриц 🌶️
'''
Напишите программу, которая перемножает две матрицы.
Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице, затем элементы первой матрицы, затем пустая строка. Далее следуют числа m и k — количество строк и столбцов второй матрицы затем элементы второй матрицы.
Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
'''
'''
# v1
n, m = map(int, input().split())
mx1 = [[int(elem) for elem in input().split()] for _ in range(n)]
input()
m, k = map(int, input().split())
mx2 = [[int(elem) for elem in input().split()] for _ in range(m)]
answer = [[0]*k for _ in range(n)]
for i in range(n):
	for j in range(k):
		for l in range(m):
			answer[i][j] += mx1[i][l]*mx2[l][j]
[print(*row) for row in answer]
'''
#%%
# 11. Возведение матрицы в степень 🌶️
'''
Напишите программу, которая возводит квадратную матрицу в m-ую степень.
Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы, затем натуральное число m.
Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
'''
'''
# v1
n = int(input())
mx = [[int(elem) for elem in input().split()] for _ in range(n)]
m = int(input())
mx_powered = mx
for _ in range(m-1):
	sub_mx = [[0]*n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			for l in range(n):
				sub_mx[i][j] += mx_powered[i][l]*mx[l][j]
	mx_powered = sub_mx
[print(*row) for row in mx_powered]
'''
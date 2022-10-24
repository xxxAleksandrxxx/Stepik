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
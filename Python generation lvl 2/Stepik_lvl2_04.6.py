#%%
# Шахматная доска
'''
На вход программе подаются два натуральных числа 
n и m. Напишите программу для создания матрицы 
размером n×m, заполнив её символами . и * в 
шахматном порядке. В левом верхнем углу должна 
стоять точка. Выведите полученную матрицу на экран, 
разделяя элементы пробелами.
Формат входных данных
На вход программе на одной строке подаются два натуральных числа 
n и m — количество строк и столбцов в матрице.
Формат выходных данных
Программа должна вывести матрицу, описанную в условии задачи.
'''
#v1
m, n = [int(num) for num in input().split()]
matrix = [['']*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if  (i + j)%2==0:
            matrix[i][j] = '.'
        else:
            matrix[i][j] = '*'
[print(*row, sep = ' ') for row in matrix]
#%%
#v2
n, m = map(int, input().split())
matrix = [['.' if (i+j)%2==0 else '*' for i in range(m)] for j in range(n)]
[print(*row) for row in matrix]

#%%
#V3
n, m = map(int, input().split())
matrix = [['.*'[(i+j)%2] for i in range(m)] for j in range(n)]
[print(*row) for row in matrix]

# %%
# Побочная диагональ
'''
На вход программе подается натуральное число 
n. Напишите программу, которая создает матрицу размером 
n×n и заполняет её по следующему правилу:
числа на побочной диагонали равны 1;
числа, стоящие выше этой диагонали, равны 0;
числа, стоящие ниже этой диагонали, равны 2.
Полученную матрицу выведите на экран. Числа 
в строке разделяйте одним пробелом.
Формат входных данных
На вход программе подается натуральное число 
n
n — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с 
условием задачи.

Примечание. Побочная диагональ — это диагональ, 
идущая из правого верхнего в левый нижний угол матрицы.
'''
#v1
n = int(input())
matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == n-j-1:
            matrix[i][j] = 1
        if i > n-j-1:
            matrix[i][j] = 2

for row in matrix:
    print(*row)

#%%
# Заполнение 1
'''
На вход программе подаются два натуральных числа n и m. 
Напишите программу, которая создает матрицу размером 
n×m и заполняет её числами от 1 до n⋅m в соответствии 
с образцом.
Формат входных данных
На вход программе на одной строке подаются два 
натуральных числа n и m — количество строк и столбцов в матрице.
Формат выходных данных
Программа должна вывести матрицу в соответствии с образцом.
'''
#v1
m, n = [int(elem) for elem in input().split()]
matrix = [[j+n*i+1 for j in range(n)] for i in range(m)]
for row in matrix:
	print(*row)

#%%
# Заполнение 1
# v2
n, m = map(int, input().split())
matrix = [[str(j+n*i+1) for j in range(n)] for i in range(m)]
for row in matrix:
    for elem in row:
        print(elem.ljust(3), end = '')
    print()

#%%
# Заполнение 2
'''
На вход программе подаются два натуральных числа n и m. 
Напишите программу, которая создает матрицу размером 
n×m заполнив её в соответствии с образцом.
Формат входных данных
На вход программе на одной строке подаются два натуральных 
числа n и m — количество строк и столбцов в матрице.
Формат выходных данных
Программа должна вывести указанную матрицу в соответствии 
с образцом.
1  4  7  10 13 16 19
2  5  8  11 14 17 20
3  6  9  12 15 18 21
Примечание. Для вывода элементов матрицы как в примерах, 
отводите ровно 3 символа на каждый элемент. 
Для этого используйте строковый метод ljust(). 
Можно обойтись и без ljust(), система примет и такое решение
'''
# v1
n, m = map(int, input().split())
matrix = [[1+i+j*n for j in range(m)] for i in range(n)]
for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end = '')
    print()

#%%
# Заполнение 3
'''
На вход программе подается натуральное число n. 
Напишите программу, которая создает матрицу размером 
n×n заполнив её в соответствии с образцом.
1  0  0  1
0  1  1  0
0  1  1  0
1  0  0  1
Формат входных данных
На вход программе подается натуральное число 
n — количество строк и столбцов в матрице.
Формат выходных данных
Программа должна вывести указанную матрицу в соответствии 
с образцом: разместить единицы на главной и побочной 
диагоналях, остальные позиции матрицы заполнить нулями.
'''
# v1
n = int(input())
matrix = [[0]*n for _ in range(n)]
for i in range(n):
    matrix[i][i] = 1
    matrix[i][~i] = 1

for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end = '')
    print()
    
#%%
# Заполнение 3
# v2
n = int(input())
matrix = [[1 if i == n-1-j or i == j else 0 for i in range(n)] for j in range(n)]
for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end='')
    print()

#%%
# Заполнение 4
'''
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив её в соответствии с образцом.
1  1  1
0  1  0
1  1  1
Формат входных данных
На вход программе подается натуральное число n — количество строк и столбцов в матрице.
Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.
Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение
'''
'''
# v1
n = int(input())
matrix = [[0]*n for _ in range(n)]

def print_matrix(matrix, l=3):
	for row in matrix:
		for elem in row:
			print(str(elem).ljust(l), end='')
		print()

for i in range(n):
	for j in range(n):
		if n-1-i >=j>=i or n-1-i<=j<=i:
			matrix[i][j] = 1

print_matrix(matrix)
'''

#%%
# Заполнение 5 🌶️
'''
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m заполнив её в соответствии с образцом.
1 2 3 4 5 6 7
2 3 4 5 6 7 1
3 4 5 6 7 1 2
4 5 6 7 1 2 3
Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно  3 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение
'''
'''
# v1
n, m = map(int, input().split())

def print_matrix(matrix, l=3):
	for row in matrix:
		for elem in row:
			print(str(elem).ljust(l), end='')
		print()

matrix = [[0]*m for _ in range(n)]

for i in range(n):
	for j in range(m):
		matrix[i][j] = 1 + (i+j)%m
		
print_matrix(matrix)
'''
'''
# v2
n, m = map(int, input().split())

def print_matrix(matrix, l=3):
	for row in matrix:
		for elem in row:
			print(str(elem).ljust(l), end='')
		print()

matrix = [[1 +(i+j)%m for j in range(m)] for i in range(n)]

print_matrix(matrix)
'''

#%%
# Заполнение змейкой
'''
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m заполнив её "змейкой" в соответствии с образцом.
1  2  3  4
8  7  6  5
9 10 11 12
Формат входных данных
На вход программе на одной строке подаются два натуральных числа 
n и m — количество строк и столбцов в матрице.
Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.
Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение
'''
'''
# v1
n, m = map(int, input().split())

def print_matrix(matrix, l=3):
	for row in matrix:
		for elem in row:
			print(str(elem).rjust(l), end='')
		print()

matrix = []
for i in range(n):
	row = [k+1 for k in range(i*m, (i+1)*m)]
	matrix.append(row[::(-1)**i])
	
print_matrix(matrix)
'''
'''
# v2 - красиво
n, m = map(int, input().split())

def print_matrix(matrix, l=3):
	for row in matrix:
		for elem in row:
			print(str(elem).ljust(l), end='')
		print()

matrix = [[j+1 for j in range(i*m, (i+1)*m)][::(-1)**i] for i in range(n)]

print_matrix(matrix)
'''
#%%
# заполнение диагоналями
n, m = map(int, input().split())
matrix = [[0]*m for _ in range(n)]
num = 1
for index in range(n+m-1):
	for i in range(n):
		for j in range(m):
			if i+j==index:
				matrix[i][j] = num
				num += 1

def print_matrix(matrix, l=3):
	for row in matrix:
		for elem in row:
			print(str(elem).ljust(l), end='')
		print()

print_matrix(matrix)
#%%
# 10 - заполнение матрицы спиралью
#%%
# Заполнение спиралью 😈😈
'''
На вход программе подаются два натуральных числа n и 
m. Напишите программу, которая создает матрицу размером 
n×m заполнив её "спиралью" в соответствии с образцом.
1  2  3
8  9  4
7  6  5
Формат входных данных
На вход программе на одной строке подаются два натуральных числа 
n и m — количество строк и столбцов в матрице.
Формат выходных данных
Программа должна вывести матрицу в соответствии образцом.
Примечание. Для вывода элементов матрицы как в примерах, 
отводите ровно 3 символа на каждый элемент. Для этого 
используйте строковый метод ljust(). Можно обойтись и без 
ljust(), система примет и такое решение 
'''
'''
# v1 
# n, m = map(int, input().split())
# matrix = [[0]*m for _ in range(n)]

def print_matrix(matrix, l=3):
    for row in matrix:
        for elem in row:
            print(str(elem).ljust(l), end='')
        print()

#numbers = [i for i in range(1, n*m+1)]
'''
'''
идея самого решения.
1) заполняется первая строка матрицы. 
2) далее берется суб-матрица содержащая все кроме первой строки
3) поворачиваем суб-матрицу против часовой стрелки.
повторяем п.1-3 пока длина суб-матрицы не станет равна нулю.
'''
'''
mx1 = [[1, 2], [3, 4], [5, 6]]
mx2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
n, m = 3, 4
matrix = [[0]*m for _ in range(n)]
numbers = [i for i in range(1, n*m+1)]

# поворот матрицы - возвращает копию повернутой матрицы
def rotate_matrix(matrix_2D):
    n = len(matrix_2D)      # строки
    m = len(matrix_2D[0])   # толбцы
    answer = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            answer[i][j] = matrix_2D[j][~i]
    return answer

sub_mx = matrix
while sub_mx != []:
    print('до заполнения')
    print_matrix(sub_mx)
    j = 0
    for j in range(len(sub_mx[0])):
        sub_mx[0][j] = numbers.pop(0)
    print('после заполнения')
    print_matrix(sub_mx)
    sub_mx = sub_mx[1:]
    print('суб-матрица')
    print_matrix(sub_mx)
    sub_mx = rotate_matrix(sub_mx)
    print('повернули суб-матрицу')
    print_matrix(sub_mx)
    print()

print_matrix(matrix)
# данный вариант не сработал - при формировании суб-матрицы
# и ее повороте элементы суб-матрицы перестают ссылаться
# на позиции изначально матрицы.
'''
#%%
#%%
# Заполнение спиралью 😈😈 v2
'''
На вход программе подаются два натуральных числа n и 
m. Напишите программу, которая создает матрицу размером 
n×m заполнив её "спиралью" в соответствии с образцом.
1  2  3
8  9  4
7  6  5
'''
# v2
# n, m = map(int, input().split())
n, m = 7, 8
matrix = [[0]*m for _ in range(n)]
numbers = [i for i in range(1, n*m+1)]

def print_matrix(matrix, l=3):
    for row in matrix:
        for elem in row:
            print(str(elem).ljust(l), end='')
        print()

print('numbers', numbers, sep='\n')
print('пустая матрица')
print_matrix(matrix)

top, right, bottom, left = 0, m-1, n-1, 0
index = 0
while True:
    # заполняем верхнюю часть
    if left > right:
        break
    #print('loop')
    for j in range(left, right+1):
        matrix[top][j] = numbers[index]
        index += 1
        #print(f'top: index={index}, numbers[{index}]={numbers[index]}')
    top += 1
    print()
    # заполняем правуч часть
    if top > bottom:
        break
    for i in range(top, bottom+1):
        matrix[i][right] = numbers[index]
        index += 1
    right -= 1
    # заполняем нижнюю часть
    if left > right:
        break
    for j in range(right, left-1, -1):
        matrix[bottom][j] = numbers[index]
        index += 1
    bottom -= 1
    # заполняем левую часть
    if top > bottom:
        break
    for i in range(bottom, top-1, -1):
        matrix[i][left] = numbers[index]
        index += 1
    left += 1

print('заполненная матрица')
print_matrix(matrix)
# %%
# Заполнение спиралью 😈😈 v3
'''
На вход программе подаются два натуральных числа n и 
m. Напишите программу, которая создает матрицу размером 
n×m заполнив её "спиралью" в соответствии с образцом.
1  2  3
8  9  4
7  6  5
'''
# v3
#n, m = map(int, input().split())
n, m = 1, 1
matrix = [[0]*m for _ in range(n)]
numbers = [i for i in range(1, n*m+1)]

top, right, bottom, left = 0, m-1, n-1, 0
while True:
    # заполняем верх
    if left > right:
        break
    for j in range(left, right+1):
        matrix[top][j] = numbers.pop(0)
    top += 1
    # заполняем право
    if top > bottom:
        break
    for i in range(top, bottom+1):
        matrix[i][right] = numbers.pop(0)
    right -= 1
    # заполняем низ
    if left > right:
        break
    for j in range(right, left-1, -1):
        matrix[bottom][j] = numbers.pop(0)
    bottom -= 1
    # заполняем лево
    if top > bottom:
        break
    for i in range(bottom, top-1, -1):
        matrix[i][left] = numbers.pop(0)
    left += 1

for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end = '')
    print()

#%%
# Заполнение спиралью 😈😈 v4
'''
На вход программе подаются два натуральных числа n и 
m. Напишите программу, которая создает матрицу размером 
n×m заполнив её "спиралью" в соответствии с образцом.
1  2  3
8  9  4
7  6  5
'''
# v4
#n, m = map(int, input().split())
n, m = 1, 1
matrix = [[0]*m for _ in range(n)]
numbers = [i for i in range(1, n*m+1)]

top, right, bottom, left = 0, m-1, n-1, 0
while len(numbers) > 0:
    # заполняем верх
    for j in range(left, right+1):
        matrix[top][j] = numbers.pop(0)
    top += 1
    # заполняем право
    for i in range(top, bottom+1):
        matrix[i][right] = numbers.pop(0)
    right -= 1
    # проверка на случай, если строк не хватает
    if len(numbers) == 0:
        break
    # заполняем низ
    for j in range(right, left-1, -1):
        matrix[bottom][j] = numbers.pop(0)
    bottom -= 1
    # заполняем лево
    for i in range(bottom, top-1, -1):
        matrix[i][left] = numbers.pop(0)
    left += 1

for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end = '')
    print()
#%%
# Заполнение спиралью 😈😈 v 5
# v5
n, m = map(int, input().split())
#n, m = 2, 4
matrix = [[0]*m for _ in range(n)]
numbers = [i for i in range(1, n*m+1)]

top, right, bottom, left = 0, m-1, n-1, 0
while len(numbers) > 0:
    # заполняем верх
    for j in range(left, right+1):
        matrix[top][j] = numbers.pop(0)
    top += 1
    # заполняем право
    for i in range(top, bottom+1):
        matrix[i][right] = numbers.pop(0)
    right -= 1
    # проверка на случай, если строк не хватает
    if len(numbers) == 0:
        break
    # заполняем низ
    for j in range(right, left-1, -1):
        matrix[bottom][j] = numbers.pop(0)
    bottom -= 1
    # заполняем лево
    for i in range(bottom, top-1, -1):
        matrix[i][left] = numbers.pop(0)
    left += 1

for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end = '')
    print()
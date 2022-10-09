
#%%
# Таблица умножения
'''На вход программе подаются два натуральных числа 
n и m — количество строк и столбцов в матрице. 
Создайте матрицу mult размером n × m и заполните 
её таблицей умножения по формуле mult[i][j] = i * j.
'''

n = int(input())
m = int(input())
matrix = [[i*j for j in range(m)] for i in range(n)]
for i in range(n):
 for j in range(m):
  print(str(matrix[i][j]).ljust(3, ' '), end='')
 print()


#%%
# Максимум в таблице
'''
На вход программе подаются два натуральных числа 
n и m — количество строк и столбцов в матрице, 
затем n строк по m целых чисел в каждой, 
отделенных символом пробела.
Напишите программу, которая находит индексы 
(строку и столбец) первого вхождения максимального элемента.
'''

m1 = [[1, 2], [3, 4], [5, 6]]
m2 = [[0, 1, 2], [3, 6, 9], [2, 2, 4],[1, 6, 3]]
matrix = m2
n = len(matrix)
m = len(matrix[0])
'''
'''
n = int(input())
m = int(input())
matrix = [[int(elem) for elem in input().split()] for _ in range(n)]

[print(row) for row in matrix]

max_i = 0
max_j = 0
max = matrix[0][0]
for i in range(n):
 for j in range(m):
  if matrix[i][j] > max:
   max = matrix[i][j]
   max_i = i
   max_j = j
#print(f'matrix[{max_i}][{max_j}] = ', max)
print(max_i, max_j)


#%%
# Обмен столбцов
'''
Напишите программу, которая меняет местами столбцы в матрице.
Формат входных данных
На вход программе на разных строках подаются два натуральных числа n и m — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену.
'''

n = int(input())
m = int(input())
matrix = [[int(elem) for elem in input().split()] for _ in range(n)]
#i = int(input()) # обмен столбца
#j = int(input()) # обмен столбца


print('до замены')
[print(row) for row in matrix]

for row in range(n):
 matrix[row][i], matrix[row][j] = matrix[row][j], matrix[row][i]

print('после замены')
[print(row) for row in matrix]



#%%
# Симметричная матрица
'''
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
'''

n = int(input())
matrix = [[int(elem) for elem in input().split()] for _ in range(n)]
answer = 'YES'
for i in range(1, n):
 for j in range(i):
  if matrix[i][j] != matrix[j][i]:
   answer = 'NO'
   break
 if answer == 'NO':
  break
print(answer)


#%%
# Обмен диагоналей
'''
Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).
'''

n = int(input())
matrix = [[int(elem) for elem in input().split()] for _ in range(n)]

print('before')
[print(row) for row in matrix]

for i in range(n):
 matrix[i][i], matrix[~i][i] = matrix[~i][i], matrix[i][i]

print('after')
[print(row) for row in matrix]


#%%
# Зеркальное отображение
'''
Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.
'''

n = int(input())
mx = [[int(elem) for elem in input().split()] for _ in range(n)]

[print(row) for row in mx]

for j in range(n):
 for i in range(n//2):
  mx[i][j], mx[~i][j] = mx[~i][j], mx[i][j]

[print(row) for row in mx]

#%%
# Поворот матрицы
'''
Напишите программу, которая поворачивает квадратную матрицу чисел на 90 градусов по часовой стрелке.
Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
Формат выходных данных
Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.
'''

#n = int(input())
#mx = [[int(el) for el in input().split()] for _ in range(n)]
mx1 = [[1, 2, 3], 
       [4, 5, 6],
       [7, 8, 9]]

mx = mx1
n=len(mx)
mx_r=[[0]*n for _ in range(n)]

[print(row) for row in mx]
print()

for i in range(n):
	for j in range(n):
		mx_r[i][j]=mx[~j][i]

[print(row) for row in mx_r]


# %%
# Ход коня
'''
На шахматной доске 
8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *, остальные клетки заполните точками.
'''
n = 8
chess_desk = [['.']*n for _ in range(n)]


# красивый вывод поля с обозначением номеров строк и букв столбцов
def print_chess(chess_desk):
 desk = [[elem for elem in row] for row in chess_desk]
 for i in range(1, 9):
  desk[n-i].insert(0, i)
 desk.insert(0, [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
 [print(*row) for row in desk]


# добавдяем коня
pos = input().lower()
ind_i = n - int(pos[1])
ind_j = ord(pos[0]) - 97
chess_desk[ind_i][ind_j] = 'N'
 
# обозначим, куда конь может ходить
steps = [[ind_i - 2, ind_j - 1],
   [ind_i - 2, ind_j + 1],
   [ind_i - 1, ind_j - 2],
   [ind_i - 1, ind_j + 2],
   [ind_i + 1, ind_j - 2],
   [ind_i + 1, ind_j + 2],
   [ind_i + 2, ind_j - 1],
   [ind_i + 2, ind_j + 1]]

# добавим точки возможных ходов на поле
for p in steps:
 if 0 <= p[0] < 8 and 0 <= p[1] < 8:
  chess_desk[p[0]][p[1]] = '*'

[print(*row) for row in chess_desk]

print_chess(chess_desk)
# %%
# v2
# рисуем поле
x,y = input()
desk = [['.']*8 for _ in range(8)]

# добавдяем коня
ind_i = n - int(y)
ind_j = ord(x) - 97
desk[ind_i][ind_j] = 'N'

# расставляем возможные ходы для коня
for i in range(8):
    for j in range(8):
        if abs(ind_i - i)*abs(ind_j - j) == 2:
            desk[i][j] = '*'


[print(*row) for row in desk]

# %%
# Магический квадрат
'''
Магическим квадратом порядка n называется квадратная 
таблица размера n x n составленная из всех чисел 
1, 2, 3... n^2 так, что суммы по каждому столбцу, 
каждой строке и каждой из двух диагоналей равны 
между собой. Напишите программу, которая проверяет, 
является ли заданная квадратная матрица магическим квадратом.
На вход программе подаётся натуральное число 
n — количество строк и столбцов в матрице, затем 
элементы матрицы: n строк, по n чисел в каждой, 
разделённые пробелами.
'''
# v1 
# n = input()
# matrix = [[int(elem) for elem in input().split()] for _ in range(n)]
flag = True


m1 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
m2 = [[8, 2, 6], [3, 5, 7], [4, 9, 1]]
m3 = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
m4 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
matrix = m4
n = len(matrix)

def check_elems(li):
    current_sum = li[0]
    for elem in li[1:]:
        if current_sum != elem:
            return False
        else:
            return True

# проверяем, что квадрат состоит из чисел от 1 до n^2
all_numbers = [i for i in range(1, 1 + n**2)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] in all_numbers:
            all_numbers.remove(matrix[i][j])
if len(all_numbers) > 0:
    flag = False
else:
    flag = True


# проверяем суммы строк
sum_row = []
for i in range(n):
    sum_current = 0
    for j in range(n):
        sum_current += matrix[i][j]
    sum_row.append(sum_current)
sum_current = sum_row[0]

# # выводим список сумм
print('sum_row:', sum_row)
print(check_elems(sum_row))

# обновляем флаг
flag = flag and check_elems(sum_row)


# проверяем суммы столбцов
sum_col = []
for j in range(n):
    current_sum = 0
    for i in range(n):
        current_sum += matrix[i][j]
    sum_col.append(current_sum)

# # выводим список сумм
print('sum_col:', sum_col)
print(check_elems(sum_col))

flag = flag and check_elems(sum_col)


# проверяем сумму главной диагонали
sum_diag = [0, 0]
for i in range(n):
    sum_diag[0] += matrix[i][i]
    sum_diag[1] += matrix[i][~i]

# # выводим сумму главной диагонали
print('main diagonal:', sum_diag[0])
print(check_elems(sum_diag))

# # выводим сумму побочной диагонали
print('second diagonal:', sum_diag[1])

flag = flag and check_elems(sum_diag)

print('final flag:', flag)

print('YES' if flag else 'NO')

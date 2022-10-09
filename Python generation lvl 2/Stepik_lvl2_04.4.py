
#%%
from concurrent.futures.process import _ThreadWakeup
from locale import MON_1


matrix = [[2, 5, 1, 0],
          [9, 4, 6, 3],
          [4, 7, 2, 2]]

rows = 3
cols = 4

#%%
# перебираем элементы матрицы по строкам
for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end = ' ')
    print()


# %%
# перебираем элементы матрицы по столбцам
for c in range(cols):
    for r in range(rows):
        print(matrix[r][c], end = ' ')
    print()


# %%
rows, cols = 3, 4
matrix  = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7]]
for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end = ' ')
    print()


# %%
# сделаем вывод более красивым с помощью .ljust()
ln = len(str(max(max(matrix))))
for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(ln+2), end = '')
    print()


# %%
# сделаем вывод более красивым с помощью .rjust()
ln = len(str(max(max(matrix))))
for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).rjust(ln+2), end = '')
    print()


# %%
# создаем квадратную матрицу размером 8×8

# функция красивого вывода матрицы через .rjust()
def print_matrix(matr):
    rows = len(matr)
    columns = len(matr[0])
    length = 0
# определяем длину самого длинного элемента
    for r in range(rows):
        for c in range(columns):
            if len(str(matr[r][c])) > length:
                length = len(str(matr[r][c]))
# собственно, сам вывод матрицы
    for r in range(rows):
        for c in range(columns):
            print(str(matr[r][c]).rjust(length+2), end ='')
        print()
    print()

n = 8
matrix = [['neo']*n for _ in range(n)]
print_matrix(matrix)

# заполняем главную диагональ единицами, а побочную двойками
# для квадратных матриц
# индексы главной диагонали i = j
# индексы побочной диагонали j = n - i - 1
for i in range(n):
    matrix[i][i] = 1
    matrix[i][n-i-1] = 2
print_matrix(matrix)


# %%
# создание матрицы m x n через генератор
m = 2
n = 3
matrix = [[input() for _ in range(m)] for _ in range(n)]
print()

# %%
# На вход программе подаются два натуральных 
# числа  n и m, каждое на отдельной строке — 
# количество строк и столбцов в матрице. 
# Далее вводятся сами элементы матрицы — слова, 
# каждое на отдельной строке; подряд идут 
# элементы сначала первой строки, затем второй, 
# и т.д.

# Напишите программу, которая сначала считывает 
# элементы матрицы один за другим, затем выводит 
# их в виде матрицы.
# Программа должна вывести считанную матрицу, 
# разделяя ее элементы одним пробелом.

# version 1
m = int(input('m:  '))
n = int(input('n:  '))
matrix = []
for _ in range(m):
    row = []
    for __ in range(n):
        row.append(input('matrix elem:  '))
    matrix.append(row)
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()


# %%
# version 2
m = int(input()) # rows
n = int(input()) # columns
matrix = [[input() for _ in range(n)] for __ in range(m)]

for r in range(m):
    print(*matrix[r], sep=' ')


# %%
# version 3
m = int(input()) # rows
n = int(input()) # columns

matrix = [[input() for _ in range(n)] for __ in range(m)]
[print(*matrix[row], sep=' ') for row in range(m)]


# %%
# На вход программе подаются два натуральных 
# числа n и m, каждое на отдельной строке — 
# количество строк и столбцов в матрице. 
# Далее вводятся сами элементы матрицы — слова, 
# каждое на отдельной строке; подряд идут 
# элементы сначала первой строки, затем второй, 
# и т.д.

# Напишите программу, которая считывает элементы 
# матрицы один за другим, выводит их в виде 
# матрицы, выводит пустую строку, и снова ту же 
# матрицу, но уже поменяв местами строки со 
# столбцами: первая строка выводится как первый 
# столбец, и так далее.

# version 1
m = int(input()) # rows
n = int(input()) # columns

matrix = [[input() for _ in range(n)] for __ in range(m)]
[print(*matrix[row], sep=' ') for row in range(m)]
print()
for column in range(n):
    for row in range(m):
        print(matrix[row][column], end = ' ')
    print()


# %%
# version 2
m = int(input()) # rows
n = int(input()) # columns

matrix = [[input() for _ in range(n)] for __ in range(m)]
[print(*row, sep =' ') for row in matrix]
print()
[print(*[matrix[row][col] for row in range(m)]) for col in range(n)]


# %%
# Следом квадратной матрицы называется сумма 
# элементов главной диагонали. Напишите программу, 
# которая выводит след заданной квадратной 
# матрицы. На вход программе подаётся натуральное 
# число n — количество строк и столбцов в матрице, 
# затем элементы матрицы (целые числа) построчно 
# через пробел. Программа должна вывести одно 
# число — след заданной матрицы.

n = int(input())
matrix = [input().split() for _ in range(n)]
print(sum([int(matrix[i][i]) for i in range(n)]))


# %%
# Напишите программу, которая выводит количество 
# элементов квадратной матрицы в каждой строке, 
# больших среднего арифметического элементов 
# данной строки.
# На вход программе подаётся натуральное число 
# n — количество строк и столбцов в матрице, 
# затем элементы матрицы (целые числа) построчно 
# через пробел.
# Программа должна вывести n чисел — для каждой 
# строки количество элементов матрицы, больших 
# среднего арифметического элементов данной 
# строки.
# .v1
n = int(input())  # размерность матрицы nxn
matrix = [[int(i) for i in input().split()] for _ in range(n)]
#print(*matrix, sep = '\n')
for row in matrix:
    mean = sum(row)/len(row)
    count_list = [elem for elem in row if elem > mean]
    print(len(count_list))


# %%
# .v2
n = int(input())  # размерность матрицы nxn
matrix = [[int(i) for i in input().split()] for _ in range(n)]
for row in matrix:
    mean = sum(row)/n
    count = 0
    for elem in row:
        if elem > mean:
            count += 1
    print(count)


# %%
# Напишите программу, которая выводит 
# максимальный элемент из области под главной 
# диагноалью квадратной матрицы. Элементы главной
# диагнонали тоже учитываются
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
print(*matrix, sep='\n')
max_elem = matrix[0][0]
for i in range(1, n):
    for j in range(i + 1):
        if matrix[i][j] > max_elem:
            max_elem = matrix[i][j]
print(max_elem)


# %%
# Напишите программу, которая выводит 
# максимальный элемент в заштрихованной области 
# квадратной матрицы.
# Заштрихованный элемент: берем квадратную матрицу
# проводим главную и побочную диагонали
# получаем 4 сектора. нам требуеются левый и правый
# сектора. элементы диагонли входят в сектора.
'''
# создаем матрицу
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
# смотрим, что получилось
print(*matrix, sep = '\n')
'''


# %%
# тестовая матрица
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
n = len(matrix)


#%%
# разобъем задачу на предварительные

# элементы главной диагонали и выше
m_elements_above = []
for i in range(n):
    for j in range(i, n):
        m_elements_above.append(matrix[i][j])
print(*m_elements_above)


# %%
# элементы главной диагонали и ниже
m_elements_under = []
for i in range(n):
    for j in range(i+1):
       m_elements_under.append(matrix[i][j])
print(*m_elements_under)


# %%
# элементы вторичной диагонали и выше
s_elements_above = []
for i in range(n):
    for j in range(n-i):
        s_elements_above.append(matrix[i][j])
print(*s_elements_above)


# %%
# элементы вторичной диагонали и ниже
s_elements_under = []
for i in range(n):
    for j in range(n-i-1, n):
        s_elements_under.append(matrix[i][j])
print(*s_elements_under)


# %%
# соберем теперь все вместе
#  .v1 - разбиваем всю матрицу на 4 шт. и далее в
#  получившихся ищем отностилеьно главной диаганали
#  и вторичной

# тестовая матрица
matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_2 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 1, 2, 3],
            [4, 5, 6, 7]]

matrix_3 = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5]]

matrix = matrix_3
n = len(matrix)

# делим матрицу на 4 сегмента и далее ищем
# только ниже / выше главной или побочной 
# диагонали
selected_elements = []
# 1
for i in range(0, n//2+n%2):
    for j in range(0, i+1):  #диагональ входит
        selected_elements.append(matrix[i][j])
print(*selected_elements)
# 2
# для того, чтобы центральный элемент не
# дублировался, чуть изменяем матрицу по которой
# идет поиск - исключаем центральный элемент, если
# к-во столбцов нечетное.
matrix_2_s = [[elem for elem in row[len(row)//2+len(row)%2:]] for row in matrix[:n//2 + n%2]]
count = 0
for row in matrix_2_s:
    for elem in row[-count-1::]:
        selected_elements.append(elem)
        count += 1
print(*selected_elements)
# 3
for i in range(n//2+n%2, n):
    for j in range(0, n-i):  #диагональ не входит
        selected_elements.append(matrix[i][j])
print(*selected_elements)
# 4
for i in range(n//2+n%2, n):
    for j in range(i, n):
        selected_elements.append(matrix[i][j])
print(*selected_elements)

print(max(selected_elements))



# %%
# решение через индексы. наиболее красивое
# тестовая матрица
matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_2 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 1, 2, 3],
            [4, 5, 6, 7]]

matrix_3 = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 1],
            [2, 3, 4, 5, 6],
            [7, 8, 9, 1, 2],
            [3, 4, 5, 6, 7]]

matrix = matrix_3
n = len(matrix)

selected_elements = []

for i in range(n):
    for j in range(n):
        if (i >= j and i < n - j) or (i <= j and i >= n - j - 1):
            selected_elements.append(matrix[i][j])

#print(selected_elements)
print(max(selected_elements))


# %%
# разбираемся, что делает оператор ~ в индексах
a = matrix_2[0]
print('a:', a)
for i in range(len(a)):
    print(f'm[{i}]=', a[i])
    print(f'm[-{i}]', a[-i])
    print(f'm[~{i}]', a[~i])

   answer[-1].append(el)
 return answer

print(chunked(input(), int(input())))


#%%
#version 2
def chunked(my_str, n):
 answer = []
 for i in range(0, len(my_str), n):
  answer.append(my_str[i:i+n])
 return answer

print(chunked(input().split(), int(input())))



#%%
### Подсписки списка 🌶️🌶️
'''Подсписок — часть другого списка. Подсписок может содержать 
один элемент, несколько, и даже ни одного. Например, [1], [2], [3] 
и [4] — подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок 
списка [1, 2, 3, 4], но список [2, 4] не подсписок списка [1, 2, 3, 4], 
так как элементы 2 и 4 во втором списке не смежные. Пустой список — 
подсписок любого списка. Сам список — подсписок самого себя, то есть
список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].

На вход программе подается строка текста, содержащая символы. Из 
данной строки формируется список. Напишите программу, которая 
выводит список, содержащий все возможные подсписки списка, 
включая пустой список.

пример:
a b c-> [[], ['a'], ['b'], ['c'], ['a', 'b'], ['b', 'c'], ['a', 'b', 'c']]
'''

#version 1
my_list = input().split()
answer = [[]]
n = len(my_list)
for st in range(n):
 for i in range(n - st):
  answer.append(my_list[i:i+st+1])
print(answer)
#print(my_list[i:i+st+1])


#%%
# 
'''Квадратная матрица разбивается на четыре четверти, 
ограниченные главной и побочной диагоналями: верхнюю, 
нижнюю, левую и правую.
Напишите программу, которая вычисляет сумму элементов: 
верхней четверти; правой четверти; нижней четверти; левой 
четверти.
Формат входных данных
На вход программе подаётся натуральное число n — 
количество строк и столбцов в матрице, затем 
элементы матрицы (целые числа) построчно через пробел.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Элементы диагоналей не учитываются.
'''

#v1
#n = int(input())
#matrix = [[int(elem) for elem in input().split()] for _ in range(n)]

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6]]
m3 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 1], [2, 3, 4, 5, 6], [7, 8, 9, 1, 2], [1, 2, 3, 4, 5]]
matrix = m3
n = len(matrix)
[print(row, sep='\n') for row in matrix]

q1, q2, q3, q4 = [], [], [], []
Q1, Q2, Q3, Q4 = 0, 0, 0, 0
for i in range(n):
 for j in range(n):
  if n-j-1 > i < j:
   q1.append(matrix[i][j])
   Q1 += matrix[i][j]
  if n-j-1 < i < j:  #q2
   q2.append(matrix[i][j])
   Q2 += matrix[i][j]
  if n-j-1 < i > j:
   q3.append(matrix[i][j])
   Q3 += matrix[i][j]
  if n-j-1 > i > j:  #q4
   q4.append(matrix[i][j])
   Q4 += matrix[i][j]
for i in range(4):
 print(f'q{i+1}:', [q1, q2, q3, q4][i])
print()
print('Верхняя четверть:', Q1)
print('Правая четверть:', Q2)
print('Нижняя четверть:', Q3)
print('Левая четверть:', Q4)

print()
i = 0
for Q in ['Верхняя', 'Правая', 'Нижняя', 'Левая']:
 print(f'{Q} четверть:', [Q1,Q2,Q3,Q4][i])
 i += 1

#%%
#v2
#n = int(input())
#matrix = [[int(elem) for elem in input().split()] for _ in range(n)]

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6]]
m3 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 1], [2, 3, 4, 5, 6], [7, 8, 9, 1, 2], [1, 2, 3, 4, 5]]
matrix = m3
n = len(matrix)
[print(row, sep='\n') for row in matrix]

q1, q2, q3, q4 = [], [], [], []
Q1, Q2, Q3, Q4 = 0, 0, 0, 0

for i in range(n):
 for j in range(n):
  if n + ~j > i < j:
   q1.append(matrix[i][j])
   Q1 += matrix[i][j]
  if n + ~j < i < j:  #q2
   q2.append(matrix[i][j])
   Q2 += matrix[i][j]
  if n + ~j < i > j:
   q3.append(matrix[i][j])
   Q3 += matrix[i][j]
  if n + ~j > i > j:  #q4
   q4.append(matrix[i][j])
   Q4 += matrix[i][j]
for i in range(4):
 print(f'q{i+1}:', [q1, q2, q3, q4][i])
print()
print('Верхняя четверть:', Q1)
print('Правая четверть:', Q2)
print('Нижняя четверть:', Q3)
print('Левая четверть:', Q4)


#%%
#
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
#
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
'''
# Обмен столбцов
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
'''
# Симметричная матрица
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
'''
# Обмен диагоналей
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
'''
# Зеркальное отображение
Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.
'''

n = int(input())
mx = [[int(elem) for elem in input().split()] for _ in range(n)]

[print(row) for row in mx]

for j in range(n):
 for i in range(n//2):
  mx[i][j], mx[~i][j] = mx[~i][j], mx[i][j]

[print(row) for row in mx]

# %%
# Ход коня
# На шахматной доске 
# 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *, остальные клетки заполните точками.

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
# Магическим квадратом порядка n называется квадратная 
# таблица размера n x n составленная из всех чисел 
# 1, 2, 3... n^2 так, что суммы по каждому столбцу, 
# каждой строке и каждой из двух диагоналей равны 
# между собой. Напишите программу, которая проверяет, 
# является ли заданная квадратная матрица магическим квадратом.
# На вход программе подаётся натуральное число 
# n — количество строк и столбцов в матрице, затем 
# элементы матрицы: n строк, по n чисел в каждой, 
# разделённые пробелами.

# v1 
# n = input()
# matrix = [[int(elem) for elem in input().split()] for _ in range(n)]
flag = True

n = 3
m1 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
matrix = m1

def check_elems(li):
    current_sum = li[0]
    for elem in li[1:]:
        if current_sum != elem:
            return False
        else:
            return True

# проверяем суммы строк
sum_row = []
for i in range(n):
    sum_current = 0
    for j in range(n):
        sum_current += matrix[i][j]
    sum_row.append(sum_current)
sum_current = sum_row[0]

# # выводим список сумм
# print('sum_row:', sum_row)
# print(check_elems(sum_row))

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
# print('sum_col:', sum_col)
# print(check_elems(sum_col))

flag = flag and check_elems(sum_col)


# проверяем сумму главной диагонали
sum_diag = [0, 0]
for i in range(n):
    sum_diag[0] += matrix[i][i]
    sum_diag[1] += matrix[i][~i]

# # выводим сумму главной диагонали
# print('main diagonal:', sum_diag[0])
# print(check_elems(sum_diag))
# # выводим сумму побочной диагонали
# print('second diagonal:', sum_diag[1])

flag = flag and check_elems(sum_diag)

print('final flag:', flag)
# %%

# 6.3.6
'''
Программист Тимур написал программу для работы с биографическими данными русских поэтов. Данные содержатся в кортежах вида (фамилия, год рождения, город рождения). В процессе работы программы в некотором кортеже poet_data обнаружилась ошибка: ('Пушкин', 1799, 'Санкт-Петербург'), неверно указано место рождения, ведь Александр Пушкин родился в Москве.

Дополните приведенный код так, чтобы в переменной poet_data находился правильный кортеж (с исправленным значением), а затем выведите его содержимое.
'''
'''
poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
poet_data = list(poet_data)
poet_data[2] = 'Москва'
poet_data = tuple(poet_data)
print(poet_data)
'''

# 6.3.7
'''
Дополните приведенный код так, чтобы он вывел список, содержащий средние арифметические значения чисел каждого вложенного кортежа в заданном кортеже кортежей numbers.
'''
'''
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
#
answer = [sum(sub)/len(sub) for sub in numbers]

print(answer)
'''

# 6.3.8. Вершина параболы
'''
Уравнение параболы имеет вид y=ax^2+bx+c, где a≠0. Напишите программу, которая по введенным значениям a,b,c определяет и выводит вершину параболы.

Формат входных данных
На вход программе подаются три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести координаты вершины параболы.

Примечание. Координаты вершины параболы имеют вид
(-b/2a; (4ac - b^2)/4a)
'''
'''
a, b, c, = [int(input()) for _ in range(3)]
ext = (-b/(2*a), (4*a*c - b**2)/(4*a))
print(ext)
'''

# 6.4.9. Конкурсный отбор
'''
Напишите программу, которая выводит список хорошистов и отличников в классе.

Формат входных данных
На вход программе подается натуральное число n, далее следует n строк с фамилией школьника и его оценкой на каждой из них.

Формат выходных данных
Программа должна вывести сначала все введённые строки с фамилиями и оценками учеников в том же порядке. Затем следует пустая строка, а затем выводятся строки с фамилиями и оценками хорошистов и отличников (в том же порядке).

Примечание 1. Оценка ученика – это натуральное число от 1 до 5.

Примечание 2. Гарантируется, что в классе есть хотя бы один хорошист – обладатель оценки 4, или отличник – получивший 5.
'''
'''
# v1
n = int(input())
students = [tuple(input().split()) for _ in range(n)]

for student in students:
 print(*student)
print()
for student in students:
 if student[1] in '45':
  print(*student)
'''
'''
# v2
n = int(input())
sts = [tuple(input().split()) for _ in range(n)]

[print(*st) for st in sts]
print()
[print(*st) for st in sts if st[1] in '45']
'''
'''
# v3
sts = [tuple(input().split()) for _ in range(int(input()))]
[print(*st) for st in sts]
print()
for n, v in sts:
  if v in '45':
   print(n, v)
'''

#%%
# 6.3.15. Последовательность Трибоначчи
'''
Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Трибоначчи.

Формат входных данных
На вход программе подается одно число
n (n≤100) – количество членов последовательности.

Формат выходных данных
Программа должна вывести члены последовательности Трибоначчи, отделенные символом пробела.

Примечание. Последовательность Трибоначчи – последовательность натуральных чисел, где каждое последующее число является суммой трех предыдущих:
1,1,1,3,5,9,17,31,57,105…
'''
'''
n = int(input())
a, b, c = 1, 1, 1
for _ in range(n):
 print(a, end=' ')
 a, b, c = b, c, a+b+c
'''
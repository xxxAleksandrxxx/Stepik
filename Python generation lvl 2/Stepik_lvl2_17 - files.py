#%% 17.2.11 - Содержимое файла

"""
Содержимое файла

На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его содержимое."""

f_content = open(input(), 'r')
for raw in f_content:
    print(raw.strip())
f_content.close()

#%% 17.2.12 - Предпоследняя строка
"""На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его предпоследнюю строку."""

# v1
f_content = open(input(), 'r')
print(f_content.readlines()[-2].strip())
f_content.close()

# v2
f_content = open(input(), 'r', encoding='utf-8')
print(list(f_content)[-2].rstrip())
f_content.close()

#%% 17.2.13 - лучайная строка
"""Вам доступен текстовый файл lines.txt из нескольких строк. Напишите программу, которая выводит на экран случайную строку из этого файла."""
from random import choice
f_content = open('lines.txt', 'r', encoding='utf-8')
print(choice(list(f_content)).rstrip())
f_content.close()

#%% 17.2.13 - Сумма двух-1
"""Вам доступен текстовый файл numbers.txt из двух строк, на каждой из них записано целое число. Напишите программу, выводящую на экран сумму этих чисел."""
f_content = open('numbers.txt', 'r', encoding='utf-8')
print(sum(map(int, map(str.rstrip, list(f_content)))))
f_content.close()
# поскольку f_content можно итерировать по строкам, list можно не делать
# .strip() тоже можно не делать, т.к. int() сам уберет лишнее

# v2
f_content = open('numbers.txt', 'r', encoding='utf-8')
print(sum(map(int, f_content)))
f_content.close()

#%% 17.2.14 - Сумма двух-2
"""Вам доступен текстовый файл nums.txt. В файле записано два целых числа, они могут быть разделены символами пробела и конца строки. Напишите программу, выводящую на экран сумму этих чисел."""
# f = '/Users/zwar/Downloads/nums.txt'
# f_content = open(f, 'r', encoding='utf-8')

f_content = open('nums.txt', 'r', encoding='utf-8')
print(sum(map(int, filter(str.isdigit, f_content.read().split()))))
f_content.close()
# использовать фильтр конкретно в данном случае излишне - подсчитать сумму можно и без него

#%% 17.2.14 v2 
f = '/Users/zwar/Downloads/nums.txt'
f_content = open(f, 'r', encoding='utf-8')
# f_content = open('nums.txt', 'r', encoding='utf-8')
print(sum(map(int, f_content.read().split())))
f_content.close()

#%% 17.2.15 Общая стоимость

"""Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью символа табуляции (\t) разделена на три колонки:

наименование товара;
количество товара (целое число);
цена (в рублях) товара за 1 шт (целое число).
Напишите программу, выводящую на экран общую стоимость заказа."""
# f = '/Users/zwar/Downloads/prices.txt'
# f_content = open(f, 'r', encoding='utf-8')
f_content = open('prices.txt', 'r', encoding='utf-8')
result = 0
for row in f_content:
    qty, price = row.split()[1:]
    result += int(price) * int(qty)
f_content.close()
print(result)

#%% 17.3.7 - Переворот строки

"""Вам доступен текстовый файл text.txt с одной строкой текста. Напишите программу, которая выводит на экран эту строку в обратном порядке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести строку указанного файла в обратном порядке.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Используйте менеджер контекста 🙂."""

file_name = r'/Users/zwar/Downloads/'
file_name += 'text.txt'
# file_name = 'text.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    f_content = f.readline()
    print(f_content.strip()[::-1])

#%% 17.3.7 v2
file_name = r'/Users/zwar/Downloads/'
file_name += 'text.txt'
# file_name = 'text.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    print(f.readline()[::-1])

#%% 17.3.8 - Обратный порядок

"""Вам доступен текстовый файл data.txt, в котором записаны строки текста. Напишите программу, выводящую все строки данного файла в обратном порядке: сначала последнюю, затем предпоследнюю и т.д.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести строки указанного файла в обратном порядке.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Используйте менеджер контекста 🙂.

Примечание 3. Получить список всех строк файла можно при помощи метода readlines().

Примечание 4. Не забывайте про символ конца строки '\n'."""

file_name = r'/Users/zwar/Downloads/'
file_name += 'data.txt'
# file_name = 'data.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    strings = [st.rstrip() for st in f.readlines()]
for line in strings[::-1]:
    print(line)

#%% 17.3.8 v2
file_name = r'/Users/zwar/Downloads/'
file_name += 'data.txt'
# file_name = 'data.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    print(*f.readlines()[::-1], sep='')


#%% 17.3.9 - Длинные строки

"""Вам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу, которая выводит все строки наибольшей длины из файла, не меняя их порядок.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести строки указанного файла, имеющие наибольшую длину, не меняя их порядка.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Используйте менеджер контекста 🙂."""
# v1
file_name = r'/Users/zwar/Downloads/'
file_name += 'lines.txt'
# file_name = 'lines.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    f_content = f.readlines()
    print(*filter(lambda x: len(x) == max(map(len, f_content)), sorted(f_content, key=len)), sep='')
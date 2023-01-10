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
# делаем много обходов одного и того же объема данных, что не есть хорошо, но выглядит коротко
file_name = r'/Users/zwar/Downloads/'
file_name += 'lines.txt'
# file_name = 'lines.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    f_content = f.readlines()
    print(*filter(lambda x: len(x) == max(map(len, f_content)), sorted(f_content, key=len)), sep='')

#%% 17.3.9 v2
# делаем один обход данных
file_name = r'/Users/zwar/Downloads/'
file_name += 'lines.txt'
# file_name = 'lines.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    longest_list = list()
    longest_len = 0
    st = f.readline().rstrip()
    while st != '':
        st_len = len(st)
        if st_len > longest_len:
            longest_len = st_len
            longest_list = [st]
        elif st_len == longest_len:
            longest_list.append(st)
        st = f.readline().rstrip()
for elem in longest_list:
    print(elem)
        

#%% 17.3.10 - Сумма чисел в строках

"""Вам доступен текстовый файл numbers.txt, каждая строка которого может содержать одно или несколько целых чисел, разделенных одним или несколькими пробелами.

Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит эту сумму на экран (для каждой строки выводится сумма чисел в этой строке).

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму чисел в каждой строке."""
# 17.3.10 v1
file_name = r'/Users/zwar/Downloads/'
file_name += 'numbers.txt'
# file_name = 'numbers.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    line = f.readline().strip()
    while line != '':
        print(sum(map(int, line.split())))
        line = f.readline().strip()

#%% 17.3.10 v2
file_name = r'/Users/zwar/Downloads/'
file_name += 'numbers.txt'
# file_name = 'numbers.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    for line in f:
        print(sum(map(int, line.split())))


#%% 17.3.11 - Сумма чисел в файле

"""Вам доступен текстовый файл nums.txt. В файле могут быть записаны целые неотрицательные числа и все, что угодно. Числом назовем последовательность одной и более цифр, идущих подряд (число всегда неотрицательно).

Напишите программу, которая вычисляет сумму всех чисел, записанных в файле.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести сумму всех чисел, записанных в файле."""
# 17.3.11 v1
file_name = r'/Users/zwar/Downloads/'
file_name += 'nums-2.txt'
# file_name = 'nums.txt'

with open(file_name, 'r', encoding='utf-8') as f:
    answer = 0
    for line in f:
        line = line.strip()
        for i in range(len(line)):
            if line[i].isdigit() == False:
                line = line.replace(line[i], ' ')
        answer += sum(map(int, line.split()))

print(answer)

#%% 17.3.11 v2
file_name = r'/Users/zwar/Downloads/'
file_name += 'nums-2.txt'
# file_name = 'nums.txt'

with open(file_name, 'r', encoding='utf-8') as f:
    answer = 0
    for line in f:
        line = ''.join(list(map(lambda x: x if x.isdigit()==True else ' ', line)))
        answer += sum(map(int, line.split()))

print(answer)
        

#%% 17.3.12 - Статистика по файлу

"""Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести три найденных числа в формате, приведенном в примере.

Input file contains:
108 letters 
20 words 
4 lines
"""

file_name = r'/Users/zwar/Downloads/'
file_name += 'file.txt'
# file_name = 'file.txt'
with open(file_name) as f:
    content = f.read()

print('Input file contains:')
print(len(list(filter(str.isalpha, content))), 'letters')
print(len(list(content.split())), 'words')
print(1 + len(list(filter(lambda x: x == chr(10), content))), 'lines')

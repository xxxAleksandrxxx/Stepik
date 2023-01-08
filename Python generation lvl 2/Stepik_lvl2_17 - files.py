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
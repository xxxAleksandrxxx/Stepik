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
# f = '/Users/xxXXXXxx/Downloads/nums.txt'
# f_content = open(f, 'r', encoding='utf-8')

f_content = open('nums.txt', 'r', encoding='utf-8')
print(sum(map(int, filter(str.isdigit, f_content.read().split()))))
f_content.close()
# использовать фильтр конкретно в данном случае излишне - подсчитать сумму можно и без него

#%% 17.2.14 v2 
f = '/Users/xxXXXXxx/Downloads/nums.txt'
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
# f = '/Users/xxXXXXxx/Downloads/prices.txt'
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

file_name = r'/Users/xxXXXXxx/Downloads/'
file_name += 'text.txt'
# file_name = 'text.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    f_content = f.readline()
    print(f_content.strip()[::-1])

#%% 17.3.7 v2
file_name = r'/Users/xxXXXXxx/Downloads/'
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

file_name = r'/Users/xxXXXXxx/Downloads/'
file_name += 'data.txt'
# file_name = 'data.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    strings = [st.rstrip() for st in f.readlines()]
for line in strings[::-1]:
    print(line)

#%% 17.3.8 v2
file_name = r'/Users/xxXXXXxx/Downloads/'
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
file_name = r'/Users/xxXXXXxx/Downloads/'
file_name += 'lines.txt'
# file_name = 'lines.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    f_content = f.readlines()
    print(*filter(lambda x: len(x) == max(map(len, f_content)), sorted(f_content, key=len)), sep='')

#%% 17.3.9 v2
# делаем один обход данных
file_name = r'/Users/xxXXXXxx/Downloads/'
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
file_name = r'/Users/xxXXXXxx/Downloads/'
file_name += 'numbers.txt'
# file_name = 'numbers.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    line = f.readline().strip()
    while line != '':
        print(sum(map(int, line.split())))
        line = f.readline().strip()

#%% 17.3.10 v2
file_name = r'/Users/xxXXXXxx/Downloads/'
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
file_name = r'/Users/xxXXXXxx/Downloads/'
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
file_name = r'/Users/xxXXXXxx/Downloads/'
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

file_name = r'/Users/xxXXXXxx/Downloads/'
file_name += 'file.txt'
# file_name = 'file.txt'
with open(file_name) as f:
    content = f.read()

print('Input file contains:')
print(len(list(filter(str.isalpha, content))), 'letters')
print(len(list(content.split())), 'words')
print(1 + len(list(filter(lambda x: x == chr(10), content))), 'lines')


#%% 17.3.13 - Random name and surname

"""Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.

Напишите программу, которая c помощью модуля random создает 3 случайные пары имя + фамилия, а затем выводит их, каждую на отдельной строке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести текст в формате, приведенном в примере."""

folder = r'/Users/xxXXXXxx/Downloads/'
file_name_1 = folder + 'first_names.txt'
file_name_2 = folder + 'last_names.txt'
from random import choice
# file_name_1 = 'first_names.txt'
# file_name_2 = 'last_names.txt'
with open(file_name_1, 'r', encoding='utf-8') as f,\
    open(file_name_2, 'r', encoding='utf-8') as l:
    f_names = [elem.strip() for elem in f]
    l_names = [elem.strip() for elem in l]
for _ in range(3):
    print(choice(f_names), choice(l_names))


#%% 17.3.14 - Необычные страны

"""Вам доступен текстовый файл population.txt с названиями стран и численностью их населения, разделенными символом табуляции '\t'.

Напишите программу выводящую все страны, название которых начинается с буквы 'G', численность населения которых больше чем 500000 человек, не меняя их порядок.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести названия стран, удовлетворяющие условиям задачи, каждое на отдельное строке."""

file_name = r'/Users/xxXXXXxx/Downloads/'
file_name += 'population.txt'
# file_name = 'population.txt'
with open(file_name, 'r', encoding='utf-8') as f:
    for raw in f:
        country, qty = raw.split('\t')
        # if country == 'G' and int(qty) > 500000:
        if country.startswith('G') and int(qty) > 500000:
            print(country)


#%% 17.3.15 - CSV-файл

"""Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных из этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна содержать реализованную функцию read_csv.

Примечание 1. Вызывать функцию read_csv не нужно.

Примечание 2. Функция read_csv не должна принимать аргументов."""

# 17.3.15 v1
file_name = r'/Users/xxXXXXxx/Downloads/'
file_name += 'data.csv'
# file_name = 'data.csv'
def read_csv(file_name0=file_name, sym0=','):
    data0 = list()
    with open(file_name0, 'r', encoding='utf-8') as f:
        head = f.readline().strip().split(sym0)
        for row in f:
            data0.append(dict(zip(head, row.strip().split(sym0))))
    return data0

print(read_csv()[0])


#%% 17.3.15 v2
file_name = r'/Users/xxXXXXxx/Downloads/'
file_name += 'data.csv'
# file_name = 'data.csv'
def read_csv(file_name0=file_name, sym0=','):
    with open(file_name0, 'r', encoding='utf-8') as f:
        key = f.readline().strip().split(sym0)
        return [dict(zip(key, row.strip().split(sym0))) for row in f]

a = read_csv()
print(a[0])

#%% решил не ту задачу - выводит словарь из ключей составленных из первой строки и списков значений, соответствующих каждому ключу
file_name = r'/Users/xxXXXXxx/Downloads/'
file_name += 'data.csv'
# file_name = 'data.csv'
def read_csv(file_name0=file_name, sym0=','):
    with open(file_name0, 'r', encoding='utf-8') as f:
        data0 = dict()
        head = f.readline().strip().split(sym0)
        for row in f:
            row = row.strip().split(sym0)
            for i in range(len(head)):
                data0[head[i]] = data0.get(head[i], []) + [row[i]]
    return data0

    

data = read_csv()
for key, value in data.items():
    print(key)
    print(value)
    print()

#%%% 17.4.8 - Входная строка

"""Напишите программу, которая считывает строку текста и записывает её в текстовый файл output.txt.

Формат входных данных
На вход программе подается строка текста."""

file_name = r'/Users/xxXXXXxx/Downloads/'
file_name += 'output.txt'
# file_name = 'output.txt'
with open(file_name, 'w', encoding='utf-8') as f:
    f.write(input())

# with open(file_name, 'r', encoding='utf-8') as f:
#     print(f.readline())

#%% 17.4.8 - Случайные числа

"""Напишите программу, записывающую в текстовый файл random.txt 25 случайных чисел в диапазоне от 111 до 777 (включительно), каждое с новой строки.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем random.txt и записать в него случайные числа в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке."""

file_name = r'/Users/xxXXXXxx/Downloads/'
file_name += 'random.txt'


from random import randint

# file_name = 'random.txt'
with open(file_name, 'w', encoding='utf-8') as f:
    f.writelines([str(randint(111, 777))+'\n' for _ in range(25)])

print('result:')
with open(file_name, 'r') as f:
    [print(f.readline().strip()) for _ in f]


#%% 17.4.9 - Нумерация строк

"""Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите программу для записи содержимого этого файла в файл output.txt в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел. Нумерация строк должна начинаться с 1.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем output.txt и записать в него пронумерованные строки файла input.txt.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Используйте встроенную функцию enumerate()."""
# 17.4.9 v1
folder_in = r'/Users/xxXXXXxx/Downloads/'
folder_out = r'/Users/xxXXXXxx/Documents/Temp/'

f_name_in = folder_in + 'input.txt'
f_name_out = folder_out + 'output.txt'
# f_name_in = 'input.txt'
# f_name_out = 'output.txt'

with open(f_name_in, 'r', encoding='utf-8') as f_in,\
    open(f_name_out, 'w+', encoding='utf-8') as f_out:
    count = 0
    for row in f_in:
        count += 1
        f_out.write(f'{count}) ' + row)

print('result')
with open(f_name_out, 'r', encoding='utf-8') as f:
    print(f.readlines())


#%% 17.4.10 - Подарок на новый год

"""Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка (фамилия и оценка разделены пробелом). Оценка - целое число от 0 до 100 включительно.

Напишите программу для добавления 5 баллов к каждому результату теста и вывода фамилий и новых результатов тестов в файл new_scores.txt.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем new_scores.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке."""
# 17.4.10 v1
folder_in = r'/Users/xxXXXXxx/Downloads/'
folder_out = r'/Users/xxXXXXxx/Documents/Temp/'

f_name_in = folder_in + 'class_scores.txt'
f_name_out = folder_out + 'new_scores.txt'

with open(f_name_in, 'r', encoding='utf-8') as f_in, \
    open(f_name_out, 'w+', encoding='utf-8') as f_out:
    for row in f_in:
        # print(row)
        n, g = row.strip().split()
        g = str(min(int(g)+5, 100))
        f_out .write(' '.join([n, g, '\n']))
        # f_out.write(''.join([row.strip().split()[0], str(min(100, int(row.strip().split()[1])+5)), '\n']))

#%% 17.4.10 v2
folder_in = r'/Users/xxXXXXxx/Downloads/'
folder_out = r'/Users/xxXXXXxx/Documents/Temp/'

f_name_in = folder_in + 'class_scores.txt'
f_name_out = folder_out + 'new_scores.txt'
with open(f_name_in, 'r', encoding='utf-8') as f_in, \
    open(f_name_out, 'w+', encoding='utf-8') as f_out:
    for row in f_in:
        n, g = row.strip().split()
        g = min(int(g)+5, 100)
        print(n, g, file=f_out)


#%% 17.4.11 - Загадка от Жака Фреско 🌶️

"""Однажды Жака Фреско спросили:

- Если ты такой умный, почему не богатый?
Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:
- Были разноцветные козлы. Сколько?
- Сколько чего?
- Сколько из них составляет более 7% от общего количества козлов?

Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только строки из первого списка.

Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию загадки от Жака Фреско.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем answer.txt и вывести в него в алфавитном порядке названия цветов козлов, которые удовлетворяют условию загадки Жака Фреско."""

# 17.4.11 v1
folder_in = r'/Users/xxXXXXxx/Downloads/'
folder_out = r'/Users/xxXXXXxx/Documents/Temp/'

f_name_in = folder_in + 'goats.txt'
f_name_out = folder_out + 'answer.txt'

# читаем файл
with open(f_name_in, 'r', encoding='utf-8') as f_in:
    f_in.readline()
    colors = list()
    goats = list()
    temp_var = colors
    for row in f_in:
        temp_var.append(row.strip())
        if colors[-1] == 'GOATS':
            colors = colors[:-1]
            temp_var = goats

# обрабатываем информацию
goats_dict = dict()
for elem in goats:
    goats_dict[elem] = goats_dict.get(elem, 0) + 1
goats_total = sum(goats_dict.values())
answer = [key for key, value in goats_dict.items() if value*100 > goats_total*7]

# записываем ответ в файл
with open(f_name_out, 'w+', encoding='utf-8') as f_out:
    print(*sorted(answer), file=f_out, sep='\n')
    # for elem in sorted(answer):
    #     print(elem, file=f_out)


#%% 17.4.12 - Конкатенация файлов 🌶️

"""На вход программе подается натуральное число n и n строк с названиями файлов. Напишите программу, которая создает файл output.txt и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка.

Формат входных данных
На вход программе подается натуральное число n и n строк названий существующих файлов.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.

Примечание. Считайте, что исполняемая программа и указанные файлы находятся в одной папке."""
# 17.4.12 v1
names = [input() for _ in range(int(input()))]
with open('output.txt', 'w+', encoding='utf-8') as f_out:
    for f_name in names:
        with open(f_name, 'r', encoding='utf-8') as f:
            f_out.write(f.read())

# 17.4.12 v2
with open('output.txt', 'w+', encoding='utf-8') as f_out:
    for _ in range(int(input())):
        with open(input(), 'r', encoding='utf-8') as f:
            f_out.write(f.read())


#%% 17.4.13 - Лог файл 🌶️

"""Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее. Каждая строка файла содержит три значения, разделенные запятыми и символом пробела: имя пользователя, время входа, время выхода, где время указано в 24-часовом формате.

Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей (не меняя порядка следования), которые были в сети не менее часа.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Считайте, что каждый пользователь был только раз в системе, то есть в файле нет двух строк с одинаковым пользователем."""
# 17.4.13 v1
folder_in = r'/Users/xxXXXXxx/Downloads/'
folder_out = r'/Users/xxXXXXxx/Documents/Temp/'

f_name_in = folder_in + 'logfile.txt'
f_name_out = folder_out + 'output.txt'

def to_min(time0):
    h, m = map(int, time0.strip().split(':'))
    return 60*h + m

with open(f_name_in, 'r', encoding='utf-8') as f_in,\
    open(f_name_out, 'w+', encoding='utf-8') as f_out:
    for line in f_in:
        name, t_in, t_out = line.strip().split(',')
        if to_min(t_out) - to_min(t_in) >= 60:
            print(name, file=f_out)

#%% 17.4.13 v2
# вместо перобразования времени в минуты, можно просто сделать десятичное число, тогда, например 15:23 станеть 1523 и если пройдет час, то это будет 16:23 -> 1623, таким образом, добавится + 100

folder_in = r'/Users/xxXXXXxx/Downloads/'
folder_out = r'/Users/xxXXXXxx/Documents/Temp/'

f_name_in = folder_in + 'logfile.txt'
f_name_out = folder_out + 'output.txt'

with open(f_name_in, 'r', encoding='utf-8') as f_in,\
    open(f_name_out, 'w+', encoding='utf-8') as f_out:
    for line in f_in:
        name, t_in, t_out = line.strip().split(',')
        if int(t_out.replace(':', '')) - int(t_in.replace(':', '')) >= 100:
            print(name, file=f_out)
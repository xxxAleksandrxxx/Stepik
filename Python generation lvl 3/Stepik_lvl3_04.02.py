
#######################
# 4.2.01
# import os
# import heapq


# def get_csv(file):
#     with open(file, 'r') as f:
#         data = []
#         for line in f:
#             data.append(line.split(','))
#     return data

# # file = os.getcwd() + '/etc/products.csv'
# file = '/etc/products.csv'
# file = os.path.dirname(os.path.abspath(__file__)) + file
# print(file)
# # csv = get_csv(file)
# # for line in csv:
# #     print(line)

# # Sort by price and printout 5 cheapest
# def get_n_cheapest(file, column_name, n, sep_data=','):
#     with open(file, 'r') as f:
#         headers = f.readline().split(sep_data)
#         column_i = headers.index(column_name)
#         # print('column_i:', column_i)
#         data_n_cheapest = f.readline().split(sep_data)
#         for line in f:
            
#             new_data = line.strip().split(sep_data)
#             # print(f'new_data[{column_i}]', new_data[column_i])
#             if len(data_n_cheapest) < n:
#                 data_n_cheapest.append(new_data)
#             else:

#                 data_n_cheapest.append(new_data)
#                 # print(new_data[column_i])
#                 # print()
#                 data_n_cheapest.sort(key=lambda x: int(x[0]))
#                 data_n_cheapest = data_n_cheapest[:n]
#                 # print()
#     return data_n_cheapest


# def get_n_cheapest2(file, column_name='price', n=5, sep_data=','):
#     with open(file, encoding='utf-8') as file:
#         data = file.read()
#         table = [r.split(',') for r in data.splitlines()]
#         del table[0]                                        # удаляем заголовок
#         table.sort(key=lambda item: int(item[1]))
#         return table[:5]


# def get_n_cheapest3(file, column_name='price', n=5, sep_data=','):
#     with open(file, 'r') as f:
#         headers = f.readline()
#         data = [line.split(sep_data) for line in f.read().strip().split('\n')]
#         data.sort(key=lambda item: int(item[1]))
#         return data[:5]


# def get_n_cheapest4(file, column_name='price', n=5, sep_data=','):
#     with open(file, 'r') as f:
#         headers = f.readline()
#         data = [line.split(sep_data) for line in f.read().strip().split('\n')]
#         five_lowest_prices = heapq.nsmallest(5, data, key=lambda x: x[1])
#         return five_lowest_prices
    

# def execution_time(func, arg, n):
#     import time
#     t0 = time.monotonic()
#     for _ in range(n):
#         func(arg)
#     t1 = time.monotonic()
#     print(f'{func.__name__:<20} {t1- t0:.2f}')

# # cheapest_5 = get_n_cheapest2(file, 'price', 5)
# # for line in cheapest_5:
# #     print(line)


# funcs = [get_n_cheapest2, get_n_cheapest3, get_n_cheapest4]
# for func in funcs:
#     print(func(file))
#     execution_time(func, file, 500000)
#     print('#'*10)
#     print()



# import csv
# import os
# file = '/etc/products.csv'
# file = os.path.dirname(os.path.abspath(__file__)) + file
# with open(file, encoding='utf-8') as f:
# 	data = list(csv.reader(f))

# print(data)


# import csv
# import os
# file = '/etc/products.csv'
# file = os.path.dirname(os.path.abspath(__file__)) + file
# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
# data = [['Тимур, abc', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Роман', 'Белых', 10, 'В']]

# with open(file, 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f, delimiter=';')#, quoting=csv.QUOTE_NONE)
#     writer.writerow(columns)
#     writer.writerows(data)
#     print("Done: write finish")

# with open(file, 'r', encoding='utf-8') as f:
# 	data = list(csv.reader(f, delimiter=';'))

# for line in data:
#      print(line)



#######################
# 4.2.12
# Скидки

# Наступил ноябрь, и во многих магазинах начались распродажи, но как 
# многим известно, зачастую товары со скидкой оказываются дороже, чем 
# без нее. Вам доступен файл sales.csv, который содержит данные о 
# ценообразовании различной бытовой техники. В первом столбце записано 
# название товара, во втором — старая цена, в третьем — новая цена со 
# скидкой:
# name;old_price;new_price
# Встраиваемая посудомоечная машина De'Longhi DDW 06S;23089;31862
# Вытяжка Falmec Afrodite 60/600;27694;18001
# ...
# Напишите программу, которая выводит названия тех товаров, цена на 
# которые уменьшилась. Товары должны быть расположены в своем исходном 
# порядке, каждый на отдельной строке.
# Примечание 1. Разделителем в файле sales.csv является точка с запятой, 
# при этом кавычки не используются.
# Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу 
# доступен по ссылке.
# Примечание 3. Начальная часть ответа выглядит так:
# Вытяжка Falmec Afrodite 60/600
# Духовой шкаф AEG BS 5836600
# Вытяжка MAUNFELD PLYM 60
# ...
# Примечание 4. При открытии файла используйте явное указание кодировки 
# UTF-8.

# import csv

# def goods_cheaper(file_csv):
# 	with open(file_csv, 'r', encoding='utf-8') as f:
# 		data = list(csv.DictReader(f, delimiter=';'))
# 	list_cheaper = []
# 	for line in data[1:]:
# 		if int(line['old_price']) > int(line['new_price']):
# 			list_cheaper.append(line['name'])
# 	return list_cheaper


# if __name__ == "__main__":
# 	file_csv = 'sales.csv'
# 	goods = goods_cheaper(file_csv)
# 	for g in goods:
# 		print(g)
		


#######################
# 4.2.13
# Средняя зарплата
# Вам доступен файл salary_data.csv, который содержит анонимную 
# информацию о зарплатах сотрудников в различных компаниях. В первом 
# столбце записано название компании, а во втором — зарплата очередного 
# сотрудника:
# company_name;salary
# Atos;135000
# ХайТэк;24400
# Philax;128600
# Инлайн Груп;43900
# IBS;70600
# Oracle;131600
# Atos;91000
# ...
# Напишите программу, которая упорядочивает компании по возрастанию 
# средней зарплаты ее сотрудников и выводит их названия, каждое на 
# отдельной строке. Если две компании имеют одинаковые средние зарплаты, 
# они должны быть расположены в лексикографическом порядке их названий.
# Примечание 1. Средняя зарплата компании определяется как отношение 
# суммы всех зарплат к их количеству.
# Примечание 2. Разделителем в файле salary_data.csv является точка с 
# запятой, при этом кавычки не используются.
# Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу 
# доступен по ссылке.
# Примечание 4. Начальная часть ответа выглядит так:
# Информзащита
# Форс
# OFT group
# # ...




# import csv


# # На удивление, самое быстрое решение.
# def average_salaries(file):
#     with open(file, encoding='utf-8') as f:
#         data = list(csv.reader(f, delimiter=';'))[1:]
#     average_d = dict()
#     for row in data:
#         count, sum, average = average_d.get(row[0], [0, 0, 0])
#         count += 1
#         sum += int(row[1])
#         average = sum / count
#         average_d[row[0]] = [count, sum, average]
#     average_sorted = sorted(average_d.keys(), key = lambda x: (average_d[x][2], x))
#     return average_sorted


# def average_salaries2(file):
#     with open(file, encoding='utf-8') as f:
#         data = list(csv.reader(f, delimiter=';'))
#     average = dict()
#     for name, salary in data[1:]:
#         average[name] = average.get(name, []) + [int(salary)]
#     average_sorted = sorted(average, key=lambda x: (sum(average[x]) / len(average[x]), x))
#     return average_sorted

# def average_salaries3(file):
#     d = {}
#     with open(file, encoding='utf-8') as f:
#         rows = list(csv.reader(f, delimiter=';'))
#         for key, value in rows[1:]:
#             d[key] = d.get(key, []) + [int(value)]
#         d_sort = sorted(d, key=lambda x: (sum(d[x]) / len(d[x]), x))
#         return d_sort


# def execution_time(func, arg, n=10):
#     import time
#     t0 = time.monotonic()
#     for _ in range(n):
#         func(arg)
#     t1 = time.monotonic()
#     print(f'{func.__name__:<20} {t1-t0:.2f}')


# if __name__ == "__main__":
#     file = '/Users/aduz/Documents/_study/Stepik/Python generation lvl 3/etc/salary_data.csv'
#     # answer = average_salaries(file)
#     funcs = (average_salaries, average_salaries2, average_salaries3)
#     for func in funcs:
#         execution_time(func, file, n=1000)


# # if __name__ == "__main__":
# #     import os
# #     import urllib.request
# #     # file = os.getcwd() + '/etc/products.csv'
# #     file = '/Users/aduz/Documents/_study/Stepik/Python generation lvl 3/etc/salary_data.csv'
# #     answer = average_salaries(file)



#######################
# 4.2.14
# Сортировка по столбцу
# Вам доступен файл deniro.csv, каждый столбец которого содержит либо 
# только числа, либо строковые значения:
# Machete,2010,72
# Marvin's Room,1996,80
# Raging Bull,1980,97
# ...
# Напишите программу, которая сортирует содержимое данного файла по 
# указанному столбцу. Причем данные должны быть отсортированы в порядке 
# возрастания чисел, если столбец содержит числа, и в лексикографическом 
# порядке слов, если столбец содержит слова.
# Формат входных данных
# На вход программе подается натуральное число — номер столбца файла 
# deniro.csv.
# Формат выходных данных
# Программа должна отсортировать содержимое файла deniro.csv по введенному 
# столбцу и вывести полученный результат в исходном формате.
# Примечание 1. Нумерация столбцов начинается с единицы.
# Примечание 2. Например, если бы файл deniro.csv имел вид:
# red,4
# blue,3
# green,28
# purple,1
# и его требовалось отсортировать по второму столбцу (в порядке 
# возрастания чисел), то программа должна была бы вывести:
# purple,1
# blue,3
# red,4
# green,28
# Примечание 3. Если две какие-либо строки имеют одинаковые значения в 
# столбцах, то следует сохранить их исходный порядок следования.
# Примечание 4. Разделителем в файле deniro.csv является запятая, при 
# этом кавычки не используются.

import csv

def sheet_sorted(file, column=1):
    column -= 1
    # with open(file, 'r', encoding='utf-8') as f:
    #     data = list(csv.reader(f, delimiter=','))
    # if data[0][column].isnumeric():
    #     data_sorted = sorted(data, key=lambda x: int(x[column]))
    # else:
    #     data_sorted = sorted(data, key=lambda x: x[column])
    # return data_sorted
    with open(file, 'r') as f:
        for row in f:
            print(row)
    


if __name__ == "__main__":
    file = "etc/deniro.csv"
    d = sheet_sorted(file, 3)
    # for row in d: 
    #     print(*row, sep=",")
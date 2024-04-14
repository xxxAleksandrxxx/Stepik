
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

import csv

def goods_cheaper(file_csv):
	with open(file_csv, 'r', encoding='utf-8') as f:
		data = list(csv.DictReader(f, delimiter=';'))
	list_cheaper = []
	for line in data[1:]:
		if int(line['old_price']) > int(line['new_price']):
			list_cheaper.append(line['name'])
	return list_cheaper


if __name__ == "__main__":
	file_csv = 'sales.csv'
	goods = goods_cheaper(file_csv)
	for g in goods:
		print(g)
		




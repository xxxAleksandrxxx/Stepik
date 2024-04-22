
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

# import csv

# def sheet_sorted(file, column=1):
#     column -= 1
#     with open(file, 'r', encoding='utf-8') as f:
#         data = list(csv.reader(f, delimiter=','))
#     if data[0][column].isnumeric():
#         data_sorted = sorted(data, key=lambda x: int(x[column]))
#     else:
#         data_sorted = sorted(data, key=lambda x: x[column])
#     return data_sorted
    

# if __name__ == "__main__":
#     file = "etc/deniro.csv"
#     c = int(input())
#     d = sheet_sorted(file, c)
#     for row in d: 
#         print(*row, sep=",")



#######################
# 4.2.15
# Функция csv_columns()
# Реализуйте функцию csv_columns(), которая принимает один аргумент:
# filename — название csv файла, например, data.csv
# Функция должна возвращать словарь, в котором ключом является название 
# столбца файла filename, а значением — список элементов этого столбца.
# Примечание 1. Гарантируется, что в передаваемом в функцию файле 
# разделителем является запятая, при этом кавычки не используются.
# Примечание 2. Гарантируется, что у передаваемого в функцию файла первая 
# строка содержит названия столбцов.
# Примечание 3. Например, если бы файл exam.csv имел вид:
# name,grade
# Timur,5
# Arthur,4
# Anri,5
# то следующий вызов функции csv_columns():
# csv_columns('exam.csv')
# должен был бы вернуть:
# {'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}
# Примечание 4. Ключи в словаре, а также элементы в списках должны 
# располагаться в своем исходном порядке.
# Примечание 5. В тестирующую систему сдайте программу, содержащую только 
# необходимую функцию csv_columns(), но не код, вызывающий ее.

# import csv

# def csv_columns(filename, dlm=','):
#     with open(filename, 'r', encoding="utf-8") as f:
#         headers = [header.strip() for header in f.readline().split(dlm)]
#         data = list((csv.reader(f, delimiter=dlm)))
#         m = len(data[0])
#         n = len(data)
#         data_columns = [[data[i][j] for i in range(n)] for j in range(m)]
#         csv_columns = {k: v for k, v in zip(headers, data_columns)}
#         return csv_columns

# if __name__ == "__main__":
#     file = "etc/text.csv"
#     d = csv_columns(file)
#     print(d['name'])


# import csv

# def csv_columns1(filename, dlm=','):
#     with open(filename, 'r', encoding="utf-8") as f:
#         headers = [header.strip() for header in f.readline().split(dlm)]
#         data = list((csv.reader(f, delimiter=dlm)))
#         m = len(data[0])
#         n = len(data)
#         data_columns = [[data[i][j] for i in range(n)] for j in range(m)]
#         csv_columns = {k: v for k, v in zip(headers, data_columns)}
#         return csv_columns
    

# def csv_columns2(filename, dlm=','):
#     with open(filename, 'r', encoding='utf-8') as f:
#         data = csv.reader(f, delimiter=dlm)
#         headers = next(data)
#         data_columns = {h: [] for h in headers}
#         for row in data:
#             for j, value in enumerate(row):
#                 data_columns[headers[j]].append(value)
#         return data_columns


# def csv_columns3(filename, dlm=','):
#     with open(filename, 'r', encoding='utf-8') as f:
#         data = csv.DictReader(f, delimiter=dlm)
#         data_columns = {header: [row[header] for row in data] for header in data.fieldnames}
#         return data_columns
    



# def execution_time(func, arg, n=100):
#     import time
#     t0 = time.monotonic()
#     for _ in range(n):
#         func(arg)
#     t1 = time.monotonic()
#     print(f"{func.__name__:<20} {t1-t0:.2f}")





# if __name__ == "__main__":
#     file = "etc/text.csv"
#     funcs = [csv_columns1, csv_columns2, csv_columns3]
#     for func in funcs:
#         execution_time(func, file, 100000)



#######################
# 4.2.16
# Популярные домены
# Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса. В первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:
# first_name,surname,email
# John,Wilson,johnwilson@outlook.com
# Mary,Wilson,marywilson@list.ru
# ...
# Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:
# domain,count
# rambler.ru,24
# iCloud.com,29
# ...
# где в первом столбце записано название почтового домена, а во втором — количество пользователей, использующих данный домен. Домены в файле должны быть расположены в порядке возрастания количества их использований, при совпадении количества использований — в лексикографическом порядке.
# Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.
# Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
# Примечание 3. Начальная часть файла domain_usage.csv выглядит так:
# domain,count
# rambler.ru,24
# iCloud.com,29
# ...
# Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.


# import csv

# def count_domains(data_file, domains_file):
#     """
#     Reads csv database, counts number of domains, writes new csv file with results
#     """
#     with open(data_file, "r", encoding="utf-8") as f:
#         data = list(csv.DictReader(f, delimiter=","))
#     domain_counter = dict()
#     for record in data:
#         domain = record["email"].split("@")[1]
#         domain_counter[domain] = domain_counter.get(domain, 0) + 1
#     with open(domains_file, "w", encoding="utf-8") as f:
#         writer = csv.writer(f, delimiter=',')
#         writer.writerow(["domain", "count"])
#         for k in sorted(domain_counter, key=lambda x: (domain_counter[x], x)):
#             writer.writerow([k, domain_counter[k]])
        

# if __name__ == "__main__":
#     data_file = "etc/data.csv"
#     domains_file = "etc/domain_usage.csv"
#     count_domains(data_file, domains_file)




#######################
# 4.2.17
# Wi-Fi Москвы
# Вам доступен файл wifi.csv, который содержит данные о городском Wi-Fi Москвы. В первом столбце записано название округа, во втором — название района, в третьем — адрес, в четвертом — количество точек доступа по этому адресу:
# adm_area;district;location;number_of_access_points
# Центральный административный округ;район Якиманка;город Москва, улица Серафимовича, дом 5/16;5
# Центральный административный округ;район Якиманка;город Москва, Болотная набережная, дом 11, строение 1;2
# ...
# Напишите программу, которая определяет количество точек доступа в каждом районе Москвы и выводит названия всех районов, для каждого указывая соответствующее количество точек доступа, каждое на отдельной строке, в следующем формате
# <название района>: <количество точек доступа>
# Названия районов должны быть расположены в порядке убывания количества точек доступа, при совпадении количества точек доступа — в лексикографическом порядке.
# Примечание 1. Разделителем в файле wifi.csv является точка с запятой, при этом кавычки не используются.
# Примечание 2. При сортировке названия районов должны быть использованы именно в том виде, в котором они указаны в исходном файле. Выполнять какие-либо дополнительные преобразования не нужно.
# Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
# Примечание 4. Начальная часть ответа выглядит так:
# Тверской район: 480
# район Хамовники: 386
# Пресненский район: 349
# ..
# Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.


# import csv

# def print_wifi_points(file):
#     with open(file, "r", encoding="utf-8") as f:
#         data = list(csv.DictReader(f, delimiter=";"))
#     wifi_points = dict()
#     for record in data:
#         district = record["district"]
#         wifi_points[district] = wifi_points.get(district, 0) + int(record["number_of_access_points"])
#     for district in sorted(wifi_points, key=lambda k: (-wifi_points[k], k)):
#         print(f"{district}: {wifi_points[district]}")


# if __name__ == "__main__":
#     file = "etc/wifi.csv"
#     print_wifi_points(file)



#######################
# 4.2.17
# Последний день на Титанике
# Вам доступен файл titanic.csv, который содержит данные о пассажирах, присутствовавших на борту парохода Титаник. В первом столбце указана единица, если пассажир выжил, и ноль в противном случае, во втором столбце записано полное имя пассажира, в третьем — пол, в четвертом — возраст:
# survived;name;sex;age
# 0;Mr. Owen Harris Braund;male;22
# 1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
# ...
# Напишите программу, которая выводит имена выживших пассажиров, которым было менее
# 18
# 18 лет, каждое на отдельной строке. Причем сначала должны быть расположены имена всех пассажиров мужского пола, а затем — женского, имена же непосредственно в мужском и женском списках должны быть расположены в своем исходном порядке.
# Примечание 1. Разделителем в файле titanic.csv является точка с запятой, при этом кавычки не используются.
# Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
# Примечание 3. Часть ответа выглядит так:
# Master. Gerios Moubarek
# Master. Alden Gates Caldwell
# ...
# Master. Harold Theodor Johnson
# Mrs. Nicholas (Adele Achem) Nasser
# Miss. Marguerite Rut Sandstrom
# ...
# Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.

import csv

def print_teens(file):
    with open(file, "r", encoding="utf-8") as f:
        data = list(csv.DictReader(f, delimiter=";"))
    females = []
    for record in data:
        if float(record["age"]) < 18 and record["survived"] == "1":
            if record["sex"] == "male":
                print(record["name"])
            else:
                females.append(record["name"])
    for female in females:
        print(female)

if __name__ == "__main__":
    file = "etc/titanic.csv"
    print_teens(file)
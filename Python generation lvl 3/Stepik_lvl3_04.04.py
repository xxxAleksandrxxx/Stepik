# #######################
# 4.4.1
# import json

# countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
#              'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
#              'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
#              'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

# j_str = json.dumps(obj=countries, sort_keys=True, indent="   ", separators=(",", " - "))
# print(j_str)


# #######################
# 4.4.2
# преобразовать словарь words в строку в формате JSON, пропуская пары, которые имеют недопустимые ключи, и присвоить полученный результат переменной data_json
# import json

# words = {
#          frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
#          "travel": "trævl",
#          ("hello", "world"): ("həˈləʊ", "wɜːld"),
#          "moonlight": "muːn.laɪt",
#          "sunshine": "ˈsʌn.ʃaɪn",
#          ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
#          "adventure": "ədˈventʃər",
#          "beautiful": "ˈbjuːtɪfl",
#          frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
#          "bicycle": "baisikl",
#          ("pilot", "fly"): ("pailət", "flai")
#         }

# data_json = json.dumps(obj=words, skipkeys=True)
# print(data_json)


# #######################
# 4.4.3
# объединить словари club1, club2 и club3 в список и записать полученную структуру данных в файл data.json, указав в качестве отступов три символа пробела.

# import json

# club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
#          "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

# club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
#          "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

# club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
#          "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}

# def combine_dics(file, dics):
#     data_combined = [d for d in dics]
#     # print(data_combined)
#     with open(file, "w", encoding="utf-8") as f:
#         json.dump(obj=data_combined, fp=f, indent="   ")

# if __name__ == "__main__":
#     file = "etc/data.json"
#     dics = [club1, club2, club3]
#     combine_dics(file, dics)


# #######################
# 4.4.4
# преобразовать словарь specs в строку в формате JSON и вывести ее с отступами в три пробела, не заменяя кириллические символы на их коды
# import json

# specs = {
#          'Модель': 'AMD Ryzen 5 5600G',
#          'Год релиза': 2021,
#          'Сокет': 'AM4',
#          'Техпроцесс': '7 нм',
#          'Ядро': 'Cezanne',
#          'Объем кэша L2': '3 МБ',
#          'Объем кэша L3': '16 МБ',
#          'Базовая частота': '3900 МГц'
#         }

# specs_json = json.dumps(specs, ensure_ascii=False, indent="   ")

# print(specs_json)



# #######################
# 4.4.5
# Реализуйте функцию is_correct_json(), которая принимает один аргумент string 
# Функция должна возвращать True, если строка string удовлетворяет формату JSON, или False в противном случае.

# import json

# def is_correct_json(string):
#     """
#     Check whether the given string satisfies the JSON format
#     """
#     try: 
#         json.loads(s=string)
#         return True
#     except:
#         return False

# if __name__ == "__main__":
#     st = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
#     st = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
#     print(is_correct_json(st))


# #######################
# 4.4.6
# Напишите программу, которая принимает на вход описание одного объекта в формате JSON и выводит все пары ключ-значение этого объекта.

# import json
# import sys

# def print_k_v_pairs(str_json):
#     for k, v in json.loads(s=str_json).items():
#         print(f"{k}: ", end="")
#         print(v) if type(v)!=list else print(*v, sep=", ")

# # better solution
# def print_k_v_pairs2(str_json):
#     for k, v in json.loads(s=str_json).items():
#         print(f"{k}: ", end="")
#         print(v) if not isinstance(v, list) else print(*v, sep=", ")



# if __name__ == "__main__":
#     st = sys.stdin.read()
#     print_k_v_pairs2(st)





# # #######################
# # 4.4.7
# # Разные типы
# # Вам доступен файл data.json, содержащий список различных объектов:
# # [
# #    "nwkWXma",
# #    null,
# #    {
# #       "ISgHT": "dIUbf"
# #    },
# #    "Pzt",
# #    "BXcbGVTE",
# #    ...
# # ]
# # Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося в файле data.json, измененные по следующим правилам:
# # если объект является строкой, в его конец добавляется восклицательный знак
# # если объект является числом, он увеличивается на единицу
# # если объект является логическим значением, он инвертируется
# # если объект является списком, он удваивается
# # если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
# # если объект является пустым значением (null), он не добавляется
# # Полученный список программа должна записать в файл updated_data.json.

# import json

# def create_list(file_from, file_to):
#     with open(file_from, "r", encoding="utf-8") as f:
#         data = json.load(f)
#     crazy_list = list()
#     for elem in data:
#         if isinstance(elem, str):
#             crazy_list.append(elem + "!")
#         if type(elem) == int or type(elem) == float:
#             crazy_list.append(elem+1)
#         if isinstance(elem, bool):
#             crazy_list.append(not elem)
#         if isinstance(elem, list):
#             crazy_list.append(elem*2)
#         if isinstance(elem, dict):
#             elem.update({"newkey": None})
#             crazy_list.append(elem)
#     with open(file_to, "w", encoding="utf-8") as f:
#         json.dump(obj=crazy_list, fp=f)


# def create_list2(file_from, file_to):
#     opers = {'str': lambda x: x + '!', 
#             'int': lambda x: x + 1, 
#             'float': lambda x: x + 1, 
#             'bool': lambda x: not x, 
#             'list': lambda x: x * 2, 
#             'dict': lambda x: x | {'newkey': None}}
#     with open(file_from, encoding='utf8') as fi, open(file_to, 'w', encoding='utf8') as fo:
#         json.dump([opers[type(i).__name__](i) for i in json.load(fi) if type(i).__name__ in opers], fo, indent=3)


# def create_list3(file_from, file_to):
#     with open(file_from, "r", encoding="utf-8") as f:
#         data = json.load(f)
#     crazy_list = list()
#     for elem in data:
#         elem_type = type(elem)
#         if elem_type == str:
#             crazy_list.append(elem + "!")
#         if elem_type == int or elem_type == float:
#             crazy_list.append(elem+1)
#         if elem_type == bool:
#             crazy_list.append(not elem)
#         if elem_type == list:
#             crazy_list.append(elem*2)
#         if elem_type ==  dict:
#             elem.update({"newkey": None})
#             crazy_list.append(elem)
#     with open(file_to, "w", encoding="utf-8") as f:
#         json.dump(obj=crazy_list, fp=f)


# def create_list4(file_from, file_to):
#     transormations={
#         str: lambda x: x + "!",
#         int: lambda x: x + 1,
#         bool: lambda x: not x,
#         list: lambda x: x * 2,
#         dict: lambda x: x | {"newkey": None}
#     }
#     with open(file_from, "r", encoding="utf-8") as f_from, open(file_to, "w", encoding="utf-8") as f_to:
#         data = json.load(f_from)
#         # call transformation function with the original element as an argument
#         data_updated = [transormations[type(elem)](elem) for elem in data if type(elem) in transormations]
#         json.dump(obj=data_updated, fp=f_to)  # adding indent=3 slows down the function


# def execution_time(func, *args, n=10000):
#     from time import monotonic
#     t0 = monotonic()
#     for _ in range(n):
#         func(*args)
#     t1 = monotonic()
#     print(f"{func.__name__:<20} {t1-t0:.2f}")

# if __name__ == "__main__":
#     file_from = "etc/data.json"
#     file_to = "etc/updated_data.json"
#     # create_list4(file_from, file_to)

#     funcs = [create_list, create_list2, create_list3, create_list4]
#     # funcs = [create_list2, create_list]
#     for func in funcs:
#         execution_time(func, file_from, file_to)





# # #######################
# # 4.4.8
# # Объединение объектов
# # Вам доступны два файла data1.json и data2.json, каждый из которых содержит по единственному JSON-объекту:
# # {
# #    "Holly-Anne": [
# #       33,
# #       "failed"
# #    ],
# #    "Caty": [
# #       36,
# #       "failed"
# #    ],
# #    ...
# # }
# # Напишите программу, которая объединяет два данных JSON-объекта в один JSON-объект, причем если пары из первого и второго объектов имеют совпадающие ключи, то значение следует взять из второго объекта. Полученный JSON-объект программа должна записать в файл data_merge.json.

# import json

# def merge_json(file_1, file_2, file_out):
#     with \
#     open(file_1, "r", encoding="utf-8") as f1, \
#     open(file_2, "r", encoding="utf-8") as f2, \
#     open(file_out, "w", encoding="utf-8") as f_out:
#         data_out = json.load(fp=f1) | json.load(fp=f2)
#         json.dump(fp=f_out, obj=data_out, indent=4)

# if __name__ == "__main__":
#     file_1 = "etc/data1.json"
#     file_2 = "etc/data2.json"
#     file_out = "etc/data_merge.json"
#     merge_json(file_1, file_2, file_out)




# # #######################
# # 4.4.9
# # Вам доступен файл people.json, содержащий список JSON-объектов. Причем у различных объектов может быть различное количество ключей:
# # Напишите программу, которая добавляет в каждый JSON-объект из данного списка все недостающие ключи, присваивая этим ключам значение null. Ключ считается недостающим, если он присутствует в каком-либо другом объекте, но отсутствует в данном. Программа должна создать список с обновленными JSON-объектами и записать его в файл updated_people.json

# import json

# def restore_data(file_in, file_out):
#     with \
#     open(file_in, "r", encoding="utf-8") as f_in, \
#     open(file_out, "w", encoding="utf-8") as f_out:
#         data_in = json.load(fp=f_in)
#         keys = set()
#         for elem in data_in:
#             keys.update(elem.keys())
#         data_out = list()
#         for elem in data_in:
#             keys_missed = keys - elem.keys()
#             data_out.append(elem | {k: None for k in keys_missed})
#         json.dump(fp=f_out, obj=data_out, indent=4)


# # better solution
# def restore_data2(file_in, file_out):
#     with \
#     open(file_in, encoding='utf8') as fi, \
#     open(file_out, 'w') as fo:
#         people = json.load(fi)
#         d = {k: None for i in people for k in i.keys()}
#         json.dump(obj=[d | i for i in people], fp=fo, indent=4)



# def exectution_time(func, *args, n=100):
#     from time import monotonic
#     t0 = monotonic()
#     for _ in range(n):
#         func(*args)
#     t1 = monotonic()
#     print(f"{func.__name__:<20} {t1-t0:.2f}")


# if __name__ == "__main__":
#     file_in = "etc/people.json"
#     file_out = "etc/updated_people.json"
#     restore_data2(file_in, file_out)
#     # funcs = [restore_data, restore_data2]
#     # for func in funcs:
#     #     exectution_time(func, file_in, file_out)



# #######################
# 4.4.10
# Вам доступен файл countries.json, содержащий список JSON-объектов c информацией о странах и исповедуемых в них религиях
# Напишите программу, которая создает единственный JSON-объект, имеющий в качестве ключа название религии, а в качестве значения — список стран, в которых исповедуется данная религия. Полученный JSON-объект программа должна записать в файл religion.json

# import json

# def ॐ(file_in, file_out):
#     with \
#     open(file_in, "r", encoding="utf-8") as f_in, \
#     open(file_out, "w", encoding="utf-8") as f_out:
#         data_in = json.load(fp=f_in)
#         data_out = {}
#         for elem in data_in:
#             k = elem["religion"]
#             v = elem["country"]
#             data_out[k] = data_out.get(k, []) + [v]
#         data_out = {k: data_out.get(k, []) + [v]}
#         json.dump(fp=f_out, obj=data_out, indent=4)


# # the best solution
# from collections import defaultdict
# def ॐ2(file_in, file_out):
#     with \
#     open(file_in, "r", encoding="utf-8") as f_in, \
#     open(file_out, "w", encoding="utf-8") as f_out:
#         data_in = json.load(fp=f_in)
#         data_out = defaultdict(list)
#         [data_out[elem["religion"]].append(elem["country"]) for elem in data_in]
#         json.dump(fp=f_out, obj=data_out, indent=4)


# def execution_time(func, *args, n=1000):
#     from time import monotonic
#     t0 = monotonic()
#     for _ in range(n):
#         func(*args)
#     t1 = monotonic()
#     print(f"{func.__name__:<20} {t1-t0:.2f}")

# if __name__ == "__main__":
#     file_in = "etc/countries.json"
#     file_out = "etc/religion.json"
#     # ॐ2(file_in, file_out)
#     funcs = [ॐ, ॐ2]
#     for func in funcs:
#         execution_time(func, file_in, file_out)



# #######################
# 4.4.11
# Спортивные площадки
# Вам доступен файл playgrounds.csv с информацией о спортивных площадках Москвы. В первом столбце записан тип площадки,  во втором — административный округ, в третьем — название района, в четвертом — адрес:
# ObjectName;AdmArea;District;Address
# Парк, озелененная городская территория «Лианозовский парк культуры и отдыха»;Северо-Восточный административный округ;район Лианозово;Угличская улица, дом 13
# Напишите программу, создающую JSON-объект, ключом в котором является административный округ, а значением — JSON-объект, в котором, в свою очередь, ключом является название района, относящийся к этому административному округу, а значением — список адресов всех площадок в этом районе. Полученный JSON-объект программа должна записать в файл addresses.json

# import csv, json

# def districs1(file_in, file_out):
#     with \
#     open(file_in, "r", encoding="utf-8") as f_in, \
#     open(file_out, "w", encoding="utf-8") as f_out:
#         data = csv.reader(f_in, delimiter=";")
#         header = next(data)
#         data_out = dict()
#         for _, adm, dist, addr in data:
#             if adm not in data_out:
#                 data_out[adm] = dict()
#             if dist not in data_out[adm]:
#                 data_out[adm][dist] = list()
#             data_out[adm][dist].append(addr)
#         # json.dump(fp=f_out, obj=data_out, ensure_ascii=False, indent=4)


# def districs2(file_in, file_out):
#     with \
#     open(file_in, "r", encoding="utf-8") as f_in, \
#     open(file_out, "w", encoding="utf-8") as f_out:
#         _, *data = csv.reader(f_in, delimiter=";")
#         data_out = dict()
#         [data_out.setdefault(record[1], {}).setdefault(record[2], []).append(record[3]) for record in data]
#         # json.dump(fp=f_out, obj=data_out, ensure_ascii=False, indent=4)


# def execution_time(func, *args, n=10**5):
#     from time import monotonic
#     t0 = monotonic()
#     for _ in range(n):
#         func(*args)
#     t1 = monotonic()
#     print(f"{func.__name__:<20} {t1-t0:.2f}")

# if __name__ == "__main__":
#     file_in = "etc/playgrounds.csv"
#     file_out = "etc/addresses.json"
#     # districs2(file_in, file_out)
#     funcs = [districs1, districs2]
#     for func in funcs:
#         execution_time(func, file_in, file_out)


# #######################
# 4.4.12
# import csv, json

# def write_data(file_in, file_out):
#     with \
#     open(file_in, "r", encoding="utf-8") as f_in, \
#     open(file_out, "w", encoding="utf-8") as f_out:
#         data_in = json.load(fp=f_in)
#         headers = ["name", "phone"]
#         data_out = [[elem["name"], elem["phone"]] for elem in data_in if elem["age"]>=18 and elem["progress"]>=75]
#         csv_writer = csv.writer(f_out, delimiter=",")
#         csv_writer.writerow(headers)
#         csv_writer.writerows(sorted(data_out))


# def check_result(res_1, res_2):
#     # for f, d in zip([res_1, res_2], [d_1, d_2]):
#     with open(res_1, "r", encoding="utf-8") as f_1:
#         d_1 = [row.strip() for row in f_1]
#     with open(res_2, "r", encoding="utf-8") as f_2:
#         d_2 = [row.strip() for row in f_2]

#     print("results")
#     print(d_2)
#     for a, b in zip(d_1, d_2):
#         print(a)
#         print(b)
#         print(a==b)
#         print()

#     # with open(res):
# if __name__ == "__main__":
#     file_in = "etc/students.json"
#     file_out = "etc/data.csv"
#     write_data(file_in, file_out)
#     res_1 = file_out
#     res_2 = "etc/clue_students.txt"
#     check_result(res_1, res_2)


# #######################
# 4.4.13
# Бассейны
# Тимур планирует пойти в бассейн. Среди всех бассейнов ему подходят те, которые открыты в понедельник в период с 10:00 до 12:00. Также ему нравится плавать по длинным дорожкам, поэтому из всех работающих в это время бассейнов нужно выбрать бассейн с наибольшей длиной дорожки, при равных значениях — c наибольшей шириной.
# Вам доступен файл pools.json, содержащий список JSON-объектов, которые представляют данные о крытых плавательных бассейнах

# import json

# def swiming_choice1(file_in, day="Понедельник", t0="10:00", t1="12:00"):
#     with open(file_in, "r", encoding="utf-8") as f:
#         data = json.load(fp=f)
#     swiming_pools = []
#     for sp in data:
#         if day in sp["WorkingHoursSummer"]:
#             t_open, t_close = sp["WorkingHoursSummer"][day].split("-")
#             if t_open <= t0 and t_close >= t1:
#                 swiming_pools.append([sp["DimensionsSummer"]["Length"], sp["DimensionsSummer"]["Width"], sp["Address"]])
#     for elem in sorted(swiming_pools, reverse=True)[:1]:
#         print(f"{elem[0]}x{elem[1]}\n{elem[2]}")

# if __name__ == "__main__":
#     file_in = "etc/pools.json"
#     swiming_choice1(file_in)


# #######################
# 4.4.14
# Результаты экзамена
# Вам доступен файл exam_results.csv, который содержит информацию о прошедшем экзамене в некотором учебном заведении. В первом столбце записано имя студента, во втором — фамилия, в третьем — оценка за экзамен, в четвертом — дата и время сдачи в формате YYYY-MM-DD HH:MM:SS, в пятом — адрес электронной почты:

# import csv, json

# def best_grade1(file_in, file_out):
#     """
#     find best grade and appropriate date for each student
#     sort by emails
#     """
#     with \
#     open(file_in, "r", encoding="utf-8") as f_in, \
#     open(file_out, "w", encoding="utf-8") as f_out:
#         data = csv.DictReader(f_in, delimiter=",")
#         students = dict()
#         for elem in data:
#             mail = (elem["email"])
#             if mail not in students:
#                 students[mail] = {"name": elem["name"], "surname": elem["surname"], "best_score": int(elem["score"]), "date_and_time": elem["date_and_time"], "email": elem["email"]}
#             if int(elem["score"]) >= students[mail]["best_score"]:
#                 students[mail]["best_score"] = int(elem["score"])
#                 if elem["date_and_time"] > students[mail]["date_and_time"]:
#                     students[mail]["date_and_time"] = elem["date_and_time"]
#         # json.dump(fp=f_out, obj=[students[elem] for elem in sorted(students)], indent=4)


# def best_grade2(file_in, file_out):
#     result = {}
#     with open('etc/exam_results.csv', encoding='utf-8') as ex_r:
#         rows = csv.DictReader(ex_r)  # 1
#         for row in rows:
#             row['best_score'] = int(row.pop('score'))  # 2
#             r = result.get(row['email'], row)  # 3
#             best_row = max(r, row, key=lambda item: (item['best_score'], item['date_and_time']))  # 4
#             result[row['email']] = best_row  # 5 
#     with open('best_scores.json', 'w', encoding='utf-8') as bs:
#         out = sorted(result.values(), key=lambda item: item['email'])  # 6
#         # json.dump(out, bs, indent=3)  # 7


# def check_result(f1, f2):
#     with \
#     open(f1, "r", encoding="utf-8") as f_1, \
#     open(f2, "r", encoding="utf-8") as f_2:
#         d_1 = json.load(fp=f_1)
#         d_2 = json.load(fp=f_2)
#     print("correct" if d_1 == d_2 else "wrong")
#     # for el_1, el_2 in zip(d_1, d_2):
#     #     print(el_1)
#     #     print(el_2)
#     #     print(el_1 == el_2)
#     #     print()


# def execution_time(func, *args, n=10*4):
#     from time import monotonic
#     t0 = monotonic()
#     for _ in range(n):
#         func(*args)
#     t1 = monotonic()
#     print(f"{func.__name__:<15} {t1-t0:.2f}")




# if __name__ == "__main__":
#     file_in = "etc/exam_results.csv"
#     file_out = "etc/best_scores.json"
#     # best_grade2(file_in, file_out)

#     # file_answer = "etc/clue_exam_results.txt"
#     # check_result(file_out, file_answer)

#     funcs = [best_grade1, best_grade2]
#     for func in funcs:
#         execution_time(func, file_in, file_out, n=10**4)
        


# #######################
# 4.4.15
# Общественное питание 😥
# Вам доступен файл food_services.json, содержащий список JSON-объектов, которые представляют данные о заведениях общественного питания:
# Под «заведением» будем подразумевать один JSON-объект из этого списка. У заведения имеются следующие атрибуты:
# Name — название 
# IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
# OperatingCompany — название сети
# TypeObject — вид (кафе, столовая, ресторан и т.д.)
# AdmArea — административная зона
# District — район
# Address — полный адрес
# SeatsCount — количество мест
# Напишите программу, которая:
# определяет район Москвы, в котором находится больше всего заведений, и выводит название этого района и количество заведений в нем
# определяет сеть с самым большим числом заведений и выводит название этой сети и количество заведений этой сети
# Полученные значения программа должна вывести в следующем формате:
# <район>: <количество заведений>
# <название сети>: <количество заведений>

# import json

# def top_fb(file_in):
#     with open(file_in, "r", encoding="utf-8") as f:
#         data = json.load(fp=f)
#     districts = dict()
#     chains = dict()
#     for elem in data:
#         districts[elem["District"]] = districts.get(elem["District"], 0) + 1
#         chains[elem["OperatingCompany"]] = chains.get(elem["OperatingCompany"], 0) + 1
    
#     for elem in sorted(districts, key=lambda x: districts[x])[-1:]:
#         print(f"{elem}: {districts[elem]}")
#     for elem in sorted(chains, key=lambda x: chains[x])[-2:-1]:
#         print(f"{elem}: {chains[elem]}")


# def top_fb2(file_in):
#     with open(file_in, "r", encoding="utf-8") as f:
#         data = json.load(fp=f)
#     districts = dict()
#     chains = dict()

# if __name__ == "__main__":
#     file_in = "etc/food_services.json"
#     top_fb(file_in)



# #######################
# 4.4.16

import json

def max_seats1(file_in):
    with open(file_in, "r", encoding="utf-8") as f:
        data = json.load(fp=f)
    max_seats = {}
    for record in data:
        # print(record["TypeObject"])
        if record["TypeObject"] not in max_seats:
            max_seats[record["TypeObject"]] = ["", 0]
        if record["SeatsCount"] > max_seats[record["TypeObject"]][1]:
            max_seats[record["TypeObject"]] = [record["Name"], record["SeatsCount"]]
    for elem in sorted(max_seats):
        # print(f"{elem}: {max_seats[elem][0]}, {max_seats[elem][1]}")
        pass


def max_seats2(file_in):
    with open(file_in, 'r', encoding='utf-8') as f1:
        data = json.load(f1)
        d = {i['TypeObject']: f"{i['Name']}, {i['SeatsCount']}" for i
            in sorted(data, key=lambda x:(x['TypeObject'], x['SeatsCount']))}
        for item in d.items():
            # print(f'{item[0]}: {item[1]}')
            pass


def execution_time(func, *args, n=1000):
    from time import monotonic
    t0 = monotonic()
    for _ in range(n):
        func(*args)
    t1 = monotonic()
    print(f"{func.__name__:<20} {t1-t0:.2f}")

if __name__ == "__main__":
    file_in = "etc/food_services.json"
    # max_seats2(file_in)

    funcs = [max_seats1, max_seats2]
    for func in funcs:
        execution_time(func, file_in, n=10*4)
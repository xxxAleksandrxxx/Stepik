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

import json
import sys

def print_k_v_pairs(str_json):
    for k, v in json.loads(s=str_json).items():
        print(f"{k}: ", end="")
        print(v) if type(v)!=list else print(*v, sep=", ")

# better solution
def print_k_v_pairs2(str_json):
    for k, v in json.loads(s=str_json).items():
        print(f"{k}: ", end="")
        print(v) if not isinstance(v, list) else print(*v, sep=", ")



if __name__ == "__main__":
    st = sys.stdin.read()
    print_k_v_pairs2(st)
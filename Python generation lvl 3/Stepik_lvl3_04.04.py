# #######################
# 4.4.1
import json

countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

j_str = json.dumps(obj=countries, sort_keys=True, indent="   ", separators=(",", " - "))
print(j_str)


# #######################
# 4.4.2
# преобразовать словарь words в строку в формате JSON, пропуская пары, которые имеют недопустимые ключи, и присвоить полученный результат переменной data_json
import json

words = {
         frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
         "travel": "trævl",
         ("hello", "world"): ("həˈləʊ", "wɜːld"),
         "moonlight": "muːn.laɪt",
         "sunshine": "ˈsʌn.ʃaɪn",
         ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
         "adventure": "ədˈventʃər",
         "beautiful": "ˈbjuːtɪfl",
         frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
         "bicycle": "baisikl",
         ("pilot", "fly"): ("pailət", "flai")
        }

data_json = json.dumps(obj=words, skipkeys=True)
print(data_json)
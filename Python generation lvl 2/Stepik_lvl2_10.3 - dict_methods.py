#%%
#10.3

# 10.3.10 
'''
Дополните приведенный код, чтобы в переменной result хранился словарь, в котором ключи – числа от 1 до 15 (включительно), а значения представляют собой квадраты ключей.
Примечание. Выводить содержимое словаря result не нужно.
result = {}
'''
'''
# v1
result = {}
for i in range(1, 16):
    result[i] = i**2
'''
'''
# v2
result = {i:i**2 for i in range(1,16)}
print(result)
'''


# 10.3.11
'''
Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2 по ключам, складывая значения по одному и тому же ключу, в случае, если ключ присутствует в обоих словарях. Результирующий словарь необходимо присвоить переменной result.
Примечание. Выводить содержимое словаря result не нужно.
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
'''
'''
# v1
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
for el in dict1|dict2:
    if el in dict1 and el in dict2:
        result[el] = dict1[el]+dict2[el]
    elif el in dict1 and el not in dict2:
        result[el] = dict1[el]
    else:
        result[el] = dict2[el]
'''
'''
# v2
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
for el in dict1|dict2:
    result[el] = dict1.get(el, 0) + dict2.get(el, 0)

print(len(result))
print(result)
'''
'''
# v3
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {i : dict1.get(i,0) + dict2.get(i, 0) for i in dict1|dict2}
print(len(result))
print(result)
'''

# 10.3.12
'''
Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки text будет подсчитано количество его вхождений.
Примечание. Выводить содержимое словаря result не нужно.
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
'''
'''
# v1
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for symbol in text:
    result[symbol] = result.get(symbol, 0) + 1
print(len(result))
print(result)
'''
'''
# v2
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {sym : text.count(sym) for sym in set(text)}
print(len(result))
print(result)
'''


# 10.3.13
'''
Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
'''
# v1
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
'''
#s = 'a a a a a b b b b b c c c d d s r r r r r g'
s_list = s.split()
s_count = {word : s_list.count(word) for word in set(s_list)}
# print(s_count)
name = list()
count = list()
for elem in s_count:
    name.append(elem)
    count.append(s_count[elem])
 # сортируем два списка по возрастанию количества
for i in range(len(name)-1):
    for j in range(len(name)-i-1):
        if count[j] > count[j+1]:
            count[j], count[j+1] = count[j+1], count[j]
            name[j], name[j+1] = name[j+1], name[j]
# print(count)
# print(name)
repeat = count.count(count[-1])
# print(repeat)
# сортируем самые большое количество по имени
if count.count(count[-1]) > 1:
    # print('YES')
    for i in range(len(name) - repeat, len(name)-1):
        # print('i', i)
        # print('start', len(name) - repeat)
        # print('end', len(name)-1)
        # print('len(name)', len(name))
        for j in range(len(name) - repeat, len(name)-1):
            # print('j', j)
            if name[j] < name[j+1]:
                # print(f'name[{j}]', name[j])
                # print(f'name[{j+1}]', name[j+1])
                count[j], count[j+1] = count[j+1], count[j]
                name[j], name[j+1] = name[j+1], name[j]
#print(count)
print(name[-1])
'''
'''
# v2
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

s_list = s.split()
s_dict = {elem : s_list.count(elem) for elem in set(s_list)}
max_el_count = 0
max_el_name = 'z'
for elem in s_dict:
    if s_dict[elem] > max_el_count:
        max_el_count = s_dict[elem]
        max_el_name = elem
    elif s_dict[elem] == max_el_count:
        if elem < max_el_name:
            max_el_name = elem
print(max_el_name)    
'''
'''
# v3
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
s_dict = {}
for word in s.split():
    s_dict[word] = s_dict.get(word, 0) + 1
max_el_count = max(s_dict.values())
answer = list()

for key, value in s_dict.items():
    if value == max_el_count:
        answer.append(key)
print(min(answer))
'''


# 10.3.14
'''
Вам доступен список pets, содержащий информацию о собаках и их владельцах.  Каждый элемент списка – это кортеж вида (кличка собаки, имя владельца, фамилия владельца, возраст владельца).
Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого владельца будут перечислены его собаки. Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), а значением – список кличек собак (сохранив исходный порядок следования).

Примечание 1. Не забывайте: кортежи являются неизменяемыми, поэтому могут быть ключами словаря.
Примечание 2. Обратите внимание, что у некоторых владельцев по несколько собак.
Примечание 3. Выводить содержимое словаря result не нужно.
'''
'''
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]
result = {}
'''
'''
# v1
for tup in pets:
    if tup[1:] not in result:
        result[tup[1:]] = []
    result[tup[1:]].append(*tup[:1])

print(result)
'''
'''
# v2
for tup in pets:
    result.setdefault(tup[1:], []).append(tup[0])

print(result)
'''
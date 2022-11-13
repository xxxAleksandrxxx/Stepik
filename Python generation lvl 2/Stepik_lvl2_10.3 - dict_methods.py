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
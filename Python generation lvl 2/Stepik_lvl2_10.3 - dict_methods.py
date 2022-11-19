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

# 10.3.15 Самое редкое слово 🌶️
'''
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
Формат входных данных
На вход программе подается строка текста.
Формат выходных данных
Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.

Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.
Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-, которые нужно игнорировать. Других символов в тексте нет.
'''
'''
s = 'London is the capital of Great Britain. More than six million people live in London. London lies on both banks of the river Thames. It is the largest city in Europe and one of the largest cities in the world. London is not only the capital of the country, it is also a very big port, one of the greatest commercial centres in the world, a university city, and the seat of the government of Great Britain!'
a = 'also'
'''
'''
# v1
s = input()
s_dict = {}
for word in s.split():
    w = word.lower().strip('.,!?:;- ')
    s_dict[w] = s_dict.get(w, 0) + 1
print(s_dict)

min_freq_word = min(s_dict.values())
answer = list()
for key, value in s_dict.items():
    if value == min_freq_word:
        answer.append(key)

answer = min(answer)

print(('wrong', 'right')[a==answer])
print('a      =', a)
print('answer =', answer)
'''
'''
# v2
#s = [word.strip('.,!?:;- ').lower() for word in input().split()]

s = [word.strip('.,!?:;- ').lower() for word in s.split()]

s_dict = {}
for word in s:
    s_dict[word] = s_dict.get(word, 0) + 1

answer = min(s_dict.items(), key = lambda x: (x[1], x[0]))[0]

print(answer)
'''

# 10.3.16 Исправление дубликатов 🌶️
'''
На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так, чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.

Формат входных данных
На вход программе подается строка текста, содержащая строки-идентификаторы, разделенные символом пробела.

Формат выходных данных
Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.
'''
'''
# v1
s = 'a b c a a d c'
a = 'a b c a_1 a_2 d c_1'

s_list = s.split()
s_dict = {}
# for word in s_list:
#     s_dict[word] = s_dict.get(word, 0) + 1
# print(s_dict)

for word in s_list:
    if word not in s_dict:
        s_dict[word] = 1
    else:
        s_dict[word+'_'+str(s_dict[word])] = 1
        s_dict[word] += 1
print(*s_dict.keys())
'''
'''
# v2
s = 'a b c a a d c'
a = 'a b c a_1 a_2 d c_1'

# s = s.split()
s= inptu().split()
s_dict = dict()
answer = list()
for word in s:
    n = s_dict[word] = s_dict.get(word, -1) + 1
    answer.append(f'{word}_{n}' if n>0 else word)

print(*answer)
'''


# 10.4.1 Словарь программиста
'''
Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык. Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. Напишите программу создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из этого словаря.

Формат входных данных
В первой строке задано одно целое число n — количество слов в словаре. В следующих n строках записаны слова и их определения, разделенные двоеточием и символом пробела. В следующей строке записано целое число m — количество поисковых слов, чье определение нужно вывести. В следующих m строках записаны сами слова, по одному на строке.

Формат выходных данных
Для каждого слова, независимо от регистра символов, если оно присутствует в словаре, необходимо вывести его определение. Если слова в словаре нет, программа должна вывести "Не найдено", без кавычек.

Примечание 1. Мини-словарь для начинающих разработчиков можно посмотреть тут.

Примечание 2. Гарантируется, что в определяемом слове или фразе отсутствует двоеточие (:), следом за которым идёт пробел.
'''
'''
# v1
n = int(input())
word_dict = {}
for _ in range(n):
    key, value = input().split(': ')
    word_dict[key.lower()] = value
m = int(input())
for _ in range(m):
    print(word_dict.get(input().lower(), 'Не найдено'))
'''

# NB
'''
for k, v in [input().split(': ', 1)] - в генераторе использовать цикл по сути для распаковки в переменные для последующей обработки
'''


# 10.4.2 Анаграммы 1
'''
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание). Например, английские слова evil и live – это анаграммы.

На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES если слова являются анаграммами и NO в противном случае.
'''
'''
# v1
a = input()
a = sorted({i : a[i] for i in range(len(a))}.values())
b = input()
b = sorted({i : b[i] for i in range(len(b))}.values())
# a_dict = {i : a[i] for i in range(len(a))}
# print(a_dict)
print('a', a)
print('b', b)
print(('NO', 'YES')[a == b])
'''
'''
# v2
a = ({}, {})
for elem in a:
    for sym in input():
        elem[sym] = elem.get(sym, 0) + 1
print(('NO', 'YES')[a[0] == a[1]])
'''

# 10.4.3 Анаграммы 2
'''
На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет. Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.

Формат входных данных
На вход программе подаются два предложения, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES , если предложения – анаграммы и NO в противном случае.

Примечание. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-. Других символов в тексте нет.
'''
'''
# v1
a = ({}, {})
for elem in a:
    for sym in input().lower():
        if sym in ' .,!?:;-':
            continue
        else:
            elem[sym] = elem.get(sym, 0) + 1
print(('NO', 'YES')[a[0] == a[1]])
[print(i) for i in a]
'''



# 10.4.4 Словарь синонимов
'''
Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу, которая для одного данного слова определяет его синоним.

Формат входных данных
На вход программе подается количество пар синонимов n. Далее следует n строк, каждая строка содержит два слова-синонима. После этого следует одно слово, синоним которого надо найти.

Формат выходных данных
Программа должна вывести одно слово, синоним введенного.

Примечание 1. Гарантируется, что синоним введенного слова существует в словаре.
Примечание 2. Все слова в словаре начинаются с заглавной буквы.
'''
'''
# v1
test = ['4', 'Awful Terrible', 'Beautiful Pretty', 'Great Excellent', 'Generous Bountiful', 'Pretty']
n = int(input())
text = [input() for _ in range(n+1)]
text.insert(0, n)
print(text)
test = text

n = test[0]
words_dict_1 = dict()
words_dict_2 = dict()
for word in test[1:-1]:
    key, value = word.split()
    words_dict_1[key] = words_dict_1.setdefault(key, value)
    words_dict_2[value] = words_dict_2.setdefault(value, key)
try:
    print(words_dict_1[test[-1]])
except: 
    print(words_dict_2[test[-1]])
'''
'''
# v2
test = ['4', 'Awful Terrible', 'Beautiful Pretty', 'Great Excellent', 'Generous Bountiful', 'Pretty']
answer = dict()
for words in test[1:-1]:
    key, value = words.split()
    answer[key], answer[value] = value, key

print(answer[test[-1]])
'''


# 10.4.5 Страны и города
'''
На вход программе подается список стран и городов каждой страны. Затем даны названия городов. Напишите программу, которая для каждого города выводит, в какой стране он находится.

Формат входных данных
Программа получает на вход количество стран n. Далее идет n строк, каждая строка начинается с названия страны, затем идут названия городов этой страны. В следующей строке записано число m, далее идут m запросов — названия каких-то m городов, из перечисленных выше.

Формат выходных данных
Программа должна вывести название страны, в которой находится данный город в соответствии с примером.
'''
'''
n = 2
test_city = ['Германия Берлин Мюнхен Гамбург Дортмунд', 'Нидерланды Амстердам Гаага Роттердам Алкмар']
m = 4
test_find = ['Амстердам', 'Алкмар', 'Гамбург', 'Гаага']

n = int(input())
test_city = [input() for _ in range(n)]
m = int(input())
test_find = [input() for _ in range(m)]

country_dict = dict()
for row in test_city:
    elem = row.split()
    for i in range(1, len(elem)):
        country_dict.setdefault(elem[i], elem[0])

#print(country_dict)

for word in test_find:
    print(country_dict.get(word, 'None'))
'''
'''
# v2
answer_dict = dict()

n = int(input())
for _ in range(n):
    country, *city = input().split()
    answer_dict.update(answer_dict.fromkeys(city, country))
m = int(input())
for _ in range(m):
    print(answer_dict[input()])
'''


 # 10.4.6 Телефонная книга
'''
Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера. У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу, которая поможет Тимуру находить все номера определённого друга.

Формат входных данных
В первой строке задано одно целое число n — количество номеров телефонов, информацию о которых Тимур сохранил в телефонной книге. В следующих n строках заданы телефоны и имена их владельцев через пробел. В следующей строке записано целое число m — количество поисковых запросов от Тимура. В следующих m строках записаны сами запросы, по одному на строке. Каждый запрос — это имя друга, чьи телефоны Тимур хочет найти.

Формат выходных данных
Для каждого запроса от Тимура выведите в отдельной строке все телефоны, принадлежащие человеку с этим именем (независимо от регистра имени). Если в телефонной книге нет телефонов человека с таким именем, выведите в соответствующей строке «абонент не найден» (без кавычек).

Примечание 1. Телефоны одного человека выводите в одну строку через пробел в том порядке, в каком они были заданы во входных данных.

Примечание 2. Количество строк в ответе должно быть равно числу m.

Примечание 3. Телефон — это несколько цифр, записанных подряд, а имя может состоять из букв русского или английского алфавита. Записи не повторяются.
'''
'''
n = int(input())
friends_dict = dict()
for _ in range(n):
    *value, key = input().lower().split()
    for elem in value:
        friends_dict.setdefault(key, []).append(elem)  # setdefault обращается с значению, если там пусто, то создается список. в этот список по одному добавляем номера телефонов из value

m = int(input())
for _ in range(m):
    print(*friends_dict.get(input().lower(), ['абонент не найден']))
'''


# 10.4.7 Секретное слово
'''
Напишите программу для расшифровки секретного слова методом частотного анализа.

Формат входных данных
В первой строке задано зашифрованное слово. Во второй строке задано одно целое число n – количество букв в словаре. В следующих n строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.

Формат выходных данных
Программа должна вывести дешифрованное слово.

Примечание. Гарантируется, что частоты букв не повторяются.
'''
'''
t = ['*!*!*?', '3', 'а: 3', 'н: 2', 'с: 1']
a = 'ананас'

# t = [input()]
# t.append(int(input()))
# for _ in range(int(t[1])):
#     t.append(input())
encrypted_w = dict()
for i in range(len(t[0])):
    encrypted_w[t[0][i]] = encrypted_w.get(t[0][i], 0) + 1
print(encrypted_w)

word = dict()
for row in t[2:]:
    letter, number = row.split(': ')
    word[int(number)] = letter
print(word)

for sym in t[0]:
    print(word[encrypted_w[sym]], end='')
'''


# 10.5.6
'''
Дополните приведенный код, используя генератор, так чтобы получить словарь result , в котором ключом будет позиция числа в списке numbers (начиная с 0), а значением – его квадрат.
numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
result = {}
'''
'''
numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]

result = {i: numbers[i]**2 for i in range(len(numbers))}
'''


# 10.5.7
'''
Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря colors, кроме тех, у которых значением является None.
colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}

result = {}
'''
'''
colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}

result = {key: value for key, value in colors.items() if value != None}
'''


# 10.5.8
'''
Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря favorite_numbers , значения которых являются двузначными числами.
favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}

result = {}
'''
'''
favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}

result = {key: value for key, value in favorite_numbers.items() if 9<value<100}
'''


# 10.5.9
'''
Дополните приведенный код, используя генератор, так, чтобы получить словарь result, состоящий из всех элементов словаря months , в которых ключ и значение поменялись местами.
months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

result = {}
'''
'''
months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

result = {value: key for key, value in months.items()}
'''


# 10.5.10
'''
В переменной s хранится строка пар число:слово. Дополните приведенный код, используя генератор, чтобы получить словарь result , в котором числа будут ключами, а слова – значениями.

Примечание 1. Ключи словаря должны быть целыми числами (иметь тип int), значения – строками (иметь тип str).
'''
'''
# v1
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

result = {int(elem.split(':')[0]): elem.split(':')[1] for elem in s.split()}
# print(result)
'''
'''
# v2
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

result = {int(key) : value for key, value in [elem.split(':') for elem in s.split()]}
print(result)
'''
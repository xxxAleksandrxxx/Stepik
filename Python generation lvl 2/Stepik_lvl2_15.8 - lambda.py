#%% 15.8.5
'''
"""
Напишите функцию func, используя синтаксис анонимных функций, которая принимает целочисленный аргумент и возвращает значение True, если он делится без остатка на 19 или на 13 и False в противном случае.
"""
func = lambda int_num: int_num%19 == 0 or int_num%13 == 0

# print(func(19))
# print(func(13))
# print(func(20))
# print(func(15))
# print(func(247))
'''

#%% 15.8.6 v1

"""
Напишите функцию func, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, если переданный аргумент начинается и заканчивается на английскую букву a (регистр буквы неважен) и False в противном случае.
"""
func = lambda letter: letter[0].lower()=='a' and letter[-1].lower()=='a'


print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))
print()
answer = '''False
False
True
False
False
True'''
print(answer)


#%% 15.8.6 v2
func = lambda letter: letter[0] in 'aA' and letter[-1] in 'aA'

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))
print()
answer = '''False
False
True
False
False
True'''
print(answer)

#%% 15.8.7 v1

"""Напишите функцию is_non_negative_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, если переданный аргумент является неотрицательным числом (целым или вещественным) и False в противном случае."""

is_non_negative_num = lambda x: False if not x.replace('.', '').isdigit() or '-' in x or x.count('.') > 1 else True

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))
print()
print('''False
True
False
False
True
False
False
True''')

#%% 15.8.7. v2
# string.replace(old, new, count)
is_non_negative_num = lambda x: x.replace('.', '', 1).isdigit() 

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))
print()
print('''False
True
False
False
True
False
False
True''')

#%% 15.8.8 v1
"""Напишите функцию is_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, если переданный аргумент является числом (целым или вещественным) и False в противном случае.
"""
def isfloat(my_num):
    try: 
        float(my_num)
        return True
    except:
        return False

is_num = lambda num: isfloat(num)

print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
print(is_num('1-1'))
print(is_num('0'))
print()
print('''False
True
True
True
True
False
False
True
False
False
True''')

#%% 15.8.8.v2
is_num = lambda num: num.replace('-', '', num[0]=='-').replace('.', '', 1).isdigit()

print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
print(is_num('1-1'))
print(is_num('0'))
print()
print('''False
True
True
True
True
False
False
True
False
False
True''')

#%% 15.8.9 v1

"""Напишите программу, которая с помощью встроенных функций filter() и sorted() выводит слова из списка words, имеющие длину ровно 6 символов. Слова следует вывести в алфавитном порядке на одной строке, разделив символом пробела."""

words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

print(*sorted(filter(lambda x: len(x)==6, words)))


#%% 15.8.10
'''
"""
Напишите программу, которая с помощью встроенных функций map() и filter() удаляет из списка numbers все нечетные элементы, большие 47, а все четные элементы нацело делит на два (целочисленное деление – //). Полученные числа следует вывести на одной строке, разделив символом пробела и сохранив исходный порядок.

Примечание. Используйте анонимную функцию в качестве критерия фильтрации.
"""

numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

print(*map(lambda x: x//2 if x%2==0 else x, filter(lambda x: not (x%2==1 and x > 47), numbers)))
'''

#%% 15.8.11
'''
"""Список data содержит информацию о численности населения некоторых штатов США. Напишите программу сортировки по убыванию списка data на основании последнего символа в названии штата. Затем распечатайте элементы этого списка, каждый на новой строке в формате:

<название штата>: <численность населения>

Vermont: 626299
Massachusetts: 7029917
...
Примечание 1. Сортировка производится в лексикографическом порядке (по алфавиту) по убыванию на основании последнего символа в названии штата. При этом, если два штата имеют одинаковый последний символ, следует сохранить их взаиморасположение в начальном списке.

Примечание 2. Используйте анонимную функцию в качестве критерия сортировки.
"""

data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

data = sorted(data, key=lambda x: x[1][-1], reverse=True)
for elem in data:
	print(f'{elem[1]}: {elem[0]}')
'''
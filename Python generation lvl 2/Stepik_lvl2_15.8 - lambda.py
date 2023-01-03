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
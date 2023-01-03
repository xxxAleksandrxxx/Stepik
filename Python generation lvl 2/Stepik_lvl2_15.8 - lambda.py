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
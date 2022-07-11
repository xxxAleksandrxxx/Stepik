'''
Угадайка слов
Описание проекта: программа загадывает слово, а пользователь должен его угадать.
Изначально все буквы слова неизвестны. Также рисуется виселица с петлей.
Пользователь предлагает букву, которая может входить в это слово.
Если такая буква есть в слове, то программа ставит букву столько раз,
сколько она встречается в слове. Если такой буквы нет, к виселице
добавляется круг в петле, изображающий голову. Пользователь продолжает
отгадывать буквы до тех пор, пока не отгадает всё слово.
За каждую неудачную попытку добавляется еще одна часть туловища
висельника (обычно их 6: голова, туловище, 2 руки и 2 ноги.

https://stepik.org/lesson/349847/step/1?unit=333702
'''

import random
from os import system  #для очистки экрана. нормально работает через консоль


#берем случайное слово из файла russian_nouns.txt

'''
#ищем слово через модуль linecache
import linecache
f = open('russian_nouns.txt', mode='r', encoding = 'utf-8')
lines = sum(1 for line in f)
f.close()
random_number = random.randrange(lines)
random_word = linecache.getline('russian_nouns.txt', random_number)
linecache.clearcache()
'''

'''
#ищем слово через функцию enumerate()
f = open('russian_nouns_1000.txt', mode='r', encoding = 'utf-8')
lines = sum(1 for line in f)
f.seek(0)
random_number = random.randrange(lines)
for line, word in enumerate(f):
    if line == random_number:
        random_word = word.upper()
f.close()
'''


#ищем слово через функцию enumerate()
def random_word(file):
    with open(file, mode='r', encoding = 'utf-8') as f:
        lines = sum(1 for line in f)
        f.seek(0)
        random_number = random.randrange(lines)
        for line, item in enumerate(f):
            if line == random_number:
                return item.upper()


#графическое отображение статуса игры
def display_hangman(tries):
    stages = ['''\
--------
|      |
|      
|    
|      
|     
----
''',
'''\
--------
|      |
|      O
|    
|      
|     
----
''',
'''\
--------
|      |
|      O
|      |
|      |
|     
----
''',
'''\
--------
|      |
|      O
|     \\|
|      |
|     
----
''',
'''\
--------
|      |
|      O
|     \\|/
|      |
|      
----
''',
'''\
--------
|      |
|      O
|     \\|/
|      |
|     / 
----
''',
'''\
--------
|      |
|      O
|     \\|/
|      |
|     / \\
----
''']
    return stages[tries]


#вводим букву или слово, проверям язык ввода: 'рус.' или 'eng.'
def input_alpha(lang):
    if lang == 'рус.':
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЫЬЪЮЯ'
    elif lang == 'eng.':
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        return print('какой-то не тот язык выбрали, требуется проверить')
    flag = False
    while flag == False:
        word = input(f'\nвведите слово целиком или букву ({lang}): ').upper()
        flag = True
        for i in word:
            if i not in alphabet:
                flag = False
                print('вы ввели что-то не то, попробуйте снова <(v_v)>')
                break
    return word


#вводим букву или слово, проверям язык ввода: 'рус.' или 'eng.'
def input_alpha_one(lang):
    if lang == 'рус.':
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЫЬЪЮЯ'
    elif lang == 'eng.':
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while True:
        letter = input(f'\nвведите одну букву ({lang}): ').upper()
        if len(letter) > 1 and letter[0] not in alphabet:
            print('\nбожечки, мало того, что смовол не тот, так он еще и не один  <(-_-)>')
            print('попробуем снова...')
            continue
        elif len(letter) > 1:
            print('\nнужна всего одна буква  <(-_-)>')
            print('попробуем снова...')
            continue
        elif letter not in alphabet:
            print('\nэто не тот символ  <(-_-)>')
            print('попробуем снова...')
            continue
        return letter


#вводим по одной букве
word_to_guess = random_word('russian_nouns_1000.txt')[:-1]  #последний символ - перенос строки, убираем его
len_word_to_guess = len(word_to_guess)
word = ''
used_alphas = ''
try_number = 0
#
system('cls||clear')  #для очистки экрана. нормально работает через консоль
print('\n' * 3)
#
print('Игра начинается... <(^_-)>')
print('\n' * 5)
print(display_hangman(try_number))
print(f'загаданное слово ({len_word_to_guess} букв):')
print(' ' + '_ '*len_word_to_guess)

while try_number < 6:
    word_to_print = ''
    alpha = input_alpha_one('рус.')
    used_alphas += alpha
    if alpha in word_to_guess:
        word += alpha
    else:
        try_number += 1
    system('cls||clear')  #для очистки экрана. нормально работает через консоль
    print('\n' * 10)
    print(display_hangman(try_number))
    for i in word_to_guess:
        if i in word:
            word_to_print += i + ' '
        else:
            word_to_print += '_ '
    print(f'загаданное слово ({len_word_to_guess} букв):')
    print(' ' + word_to_print)
    print('\nиспользованные буквы:')
    print(used_alphas.replace('', ' '))
    if word_to_print.replace(' ', '') == word_to_guess:
        break
    
if try_number == 6:
    print('\nвы проиграли  <(v_v)>')
    print('ответ:', word_to_guess.replace('', ' ').strip())
else:
    print('поздравляю, вы смогли угодать!  <(^_^)>')



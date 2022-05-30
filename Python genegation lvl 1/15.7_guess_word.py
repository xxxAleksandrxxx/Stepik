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
from itertools import islice



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


#ищем слово через функцию enumerate()
f = open('russian_nouns_1000.txt', mode='r', encoding = 'utf-8')
lines = sum(1 for line in f)
f.seek(0)
random_number = random.randrange(lines)
for line, word in enumerate(f):
    if line == random_number:
        random_word = word.upper()
f.close()

#print('всего строк: ', lines)
#print('номер строки:', random_number)
#print('слово:       ', random_word)


#графическое отображение статуса игры
def display_hangman(tries):
    stages = ['''
\r\r\r\r\r\r\r\r--------
\r\r\r\r\r\r\r\r|      |
\r\r\r\r\r\r\r\r|      O
\r\r\r\r\r\r\r\r|     \\|/
\r\r\r\r\r\r\r\r|      |
\r\r\r\r\r\r\r\r|     / \\
\r\r\r\r\r\r\r\r---
\r\r\r\r\r\r\r\r''',
'''
--------
|      |
|      O
|     \\|/
|      |
|     / 
---
''',
'''
--------
|      |
|      O
|     \\|/
|      |
|      
---
''',
'''
--------
|      |
|      O
|     \\|
|      |
|     
---
''',
'''
--------
|      |
|      O
|      |
|      |
|     
---
''',
'''
--------
|      |
|      O
|    
|      
|     
---
''',
'''
--------
|      |
|      
|    
|      
|     
---
''']
    return stages[tries]

print(display_hangman(0))

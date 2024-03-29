#%% 2.04 - Функция hide_card()

"""Реализуйте функцию hide_card(), которая принимает один аргумент:

card_number — строка, представляющая собой корректный номер банковской карты из 16 цифр, между которыми могут присутствовать символы пробела
Функция должна заменять первые 12 цифр в строке card_number на символ * и возвращать полученный результат. Если между цифрами в номере имелись символы пробела, их следует удалить.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию hide_card(), но не код, вызывающий ее."""
# 2.4 v1
def hide_card(card_number):
    card_number = card_number.replace(' ', '')
    return '*'*12 + card_number[12:]

card = '905 678123 45612 56'
print(hide_card(card))

#%% 2.4 v2
def hide_card(card_number):
    return '*'*12 + card_number.replace(' ', '')[-4:]

card = '905 678123 45612 56'
print(hide_card(card))


#%% 2.5 - Функция same_parity()

"""Реализуйте функцию same_parity(), которая принимает один аргумент:

numbers — список целых чисел
Функция должна возвращать новый список, элементами которого являются числа из списка numbers, имеющие ту же четность, что и первый элемент этого списка.

Примечание 1. Числа в возвращаемом функцией списке должны располагаться в своем исходном порядке. 

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию same_parity(), но не код, вызывающий ее"""
# 2.5 v1
test = (
    [],
    [6, 0, 67, -7, 10, -20],
    [-7, 0, 67, -9, 70, -29, 90]
)

def same_parity(numbers):
    answer = []
    if numbers:
        answer = list(filter(lambda x: numbers[0]%2 == x%2, numbers))
    return answer

for t in test:
    print(same_parity(t))

#%% 2.5 v2
test = (
    [],
    [6, 0, 67, -7, 10, -20],
    [-7, 0, 67, -9, 70, -29, 90]
)

def same_parity(numbers):
    return [i for i in numbers if i%2==numbers[0]%2]

for t in test:
    print(same_parity(t))


#%% 2.6 - Функция is_valid()

"""Будем считать, что PIN-код является корректным, если он удовлетворяет следующим условиям:

состоит из 4, 5 или 6 символов
состоит только из цифр (0−9)
не содержит пробелов
Реализуйте функцию is_valid(), которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать значение True, если строка string представляет собой корректный PIN-код, или False в противном случае.

Примечание 1. Если в функцию передается пустая строка, функция должна возвращать значение False.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_valid(), но не код, вызывающий ее."""
# 2.6 v1
test = (
    '4367',
    '92134',
    '89abc1',
    '49 83'
)
def is_valid(string):
    return all([4 <= len(string) <= 6, ' ' not in string, string.isdigit()])

for t in test:
    print(is_valid(t))


#%% 2.6 v2
test = (
    '4367',
    '92134',
    '89abc1',
    '49 83'
)
def is_valid(string):
    return all([4 <= len(string) <= 6, string.isdigit()])

for t in test:
    print(is_valid(t))


#%% 2.7 - Функция print_given()

"""Реализуйте функцию print_given(), которая принимает произвольное количество позиционных и именованных аргументов и выводит все переданные аргументы, указывая тип каждого. Пары аргумент-тип должны выводиться каждая на отдельной строке, в следующем формате:

для позиционных аргументов:
<значение аргумента> <тип аргумента>
для именованных аргументов:
<имя переменной> <значение аргумента> <тип аргумента>
Примечание 1. При выводе позиционные аргументы должны быть расположены в порядке их передачи, именованные — в лексикографическом порядке имен переменных.

Примечание 2. При выводе сначала должны следовать все позиционные аргументы, затем — все именованные.

Примечание 3. Если в функцию ничего не передается, функция ничего не должна выводить.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_given(), но не код, вызывающий ее."""
# 2.7 v1
def print_given(*arg, **kwarg):
    try:
        [print(a, type(a)) for a in arg]
        [print(k, v, type(v)) for k, v in sorted(kwarg.items())]
    except:
        pass

# print_given(1, [1, 2, 3], 'three', two=2)
print_given(b=2, d=4, c=3, a=1)

#%% 02.7 v2
def print_given(*arg, **kwarg):
        [print(a, type(a)) for a in arg]
        [print(k, v, type(v)) for k, v in sorted(kwarg.items())]

print_given(1, [1, 2, 3], 'three', two=2)
print_given(b=2, d=4, c=3, a=1)
print_given()

#%% 2.8 - Функция convert()

"""Реализуйте функцию convert(), которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать строку string:

полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает
Примечание 1. Символы строки, не являющиеся буквами, следует игнорировать.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию convert(), но не код, вызывающий ее.
"""

def convert(string):
    return string.upper() if len(list(filter(lambda x: x.isupper(), string))) > len(list(filter(lambda x: x.islower(), string))) else string.lower()

print(convert('aad567BBBI'))


#%% 2.9 - Функция filter_anagrams()

"""Анаграммы — это слова, которые состоят из одинаковых букв. Например:

адаптер — петарда
адресочек — середочка
азбука — базука
аистенок — осетинка
Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:

word — слово в нижнем регистре
words — список слов в нижнем регистре
Функция должна возвращать список, элементами которого являются слова из списка words, которые представляют анаграмму слова word. Если список words пуст или не содержит анаграмм, функция должна вернуть пустой список.

Примечание 1. Слова в возвращаемом функцией списке должны располагаться в своем исходном порядке. 

Примечание 2. Считайте, что слово является анаграммой самого себя.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию filter_anagrams(), но не код, вызывающий ее."""

# 2.9 v1

# def filter_anagrams(word, words):
#     answer = []
#     for w in words:
#         w_copy = w[:]
#         for alpha in word:
#             try:
#                 w_copy = w_copy.replace(alpha, '', 1)
#             except:
#                 pass
#         if len(w_copy) == 0 and len(word)==len(w):
#             answer.append(w)
#     return answer

def filter_anagrams(word, words):
    answer = []
    for w in words:
        w_copy = w[:]
        for alpha in word:
            w_copy = w_copy.replace(alpha, '', 1)
        if len(w_copy) == 0 and len(word)==len(w):
            answer.append(w)
    return answer


# word = 'abba'
# anagrams = ['aabb', 'abcd', 'bbaa', 'dada']
# print(filter_anagrams(word, anagrams))
# print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
print(filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']))

#%% 2.9 v2
def filter_anagrams(word, words):
    word = sorted(word)
    return [w for w in words if sorted(w) == word]

print(filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']))
print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))


#%% 2.10 - Функция likes()

"""В различных социальных сетях существуют системы лайков, которые в зависимости от количества людей, оценивших запись, показывают соответствующую информацию.

Реализуйте функцию likes(), которая принимает один аргумент:
names — список имён
Функция должна возвращать строку в соответствии с примерами ниже, содержание которой зависит от количества имён в списке names."""

# 2.10 v1
def likes(names):
    if names:
        if len(names) == 1:
            return f'{names[0]} оценил(а) данную запись'
        elif len(names) == 2:
            return f'{names[0]} и {names[1]} оценили данную запись'
        elif len(names) == 3:
            return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
        else:
            return f'{names[0]}, {names[1]} и {len(names[2:])} других оценили данную запись'
    else:
        return 'Никто не оценил данную запись'

print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))

#%% 2.10 v2
def likes(names):
    answer = {
        0 : "'Никто не оценил'",
        1 : "f'{names[0]} оценил(а)'",
        2 : "f'{names[0]} и {names[1]} оценили'",
        3 : "f'{names[0]}, {names[1]} и {names[2]} оценили'",
        4 : "f'{names[0]}, {names[1]} и {len(names[2:])} других оценили'"
    }
    return eval(answer.get(len(names), answer[4])) + ' данную запись'

print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))

#%% 2.11 - Функция index_of_nearest()

"""Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:

numbers — список целых чисел
number — целое число
Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс. Если список numbers пуст, функция должна вернуть число −1.

Примечание 1. Если в функцию передается список, содержащий несколько чисел, одновременно являющихся ближайшими к искомому числу, функция должна возвращать наименьший из индексов ближайших чисел.

Примечание 2. Рассмотрим третий тест. Ближайшими числами к числу 4 являются 5 и 3, имеющие индексы 1 и 2 соответственно. Наименьший из индексов равен 1.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию index_of_nearest(), но не код, вызывающий ее."""

def index_of_nearest(numbers, number):
    if numbers:
        answer = 0
        for i in range(len(numbers)):
            if abs(number - numbers[i]) < abs(number - numbers[answer]):
                answer = i
        return answer
    else:
        return -1

print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))


#%% 2.11 v2
def index_of_nearest(numbers, number):
    if numbers:
        answer = min(numbers, key=lambda x: abs(x - number))
        return numbers.index(answer)
    else:
        return -1

print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))


#%% 2.12 - Функция spell()

"""Реализуйте функцию spell(), которая принимает произвольное количество позиционных аргументов-слов и возвращает словарь, ключи которого — первые буквы слов, а значения — максимальные длины слов на эту букву.

Примечание 1. Если в функцию не передается ни одного аргумента, функция должна возвращать пустой словарь.

Примечание 2. Функция должна игнорировать регистр слов, при этом в результирующий словарь должны попасть именно буквы в нижнем регистре.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию, но не код, вызывающий ее."""

def spell(*arg):
    return {elem[0].lower() : max(map(len, filter(lambda x: x[0].lower()==elem[0].lower(), arg))) for elem in arg}

words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))
print()

print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
print()

words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))
print()

print(spell())


#%% 2.13 - Функция choose_plural() 🌶️🌶️

"""Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:

amount — натуральное число, количество
declensions — кортеж из трех вариантов склонения существительного
Функция должна возвращать строку, полученную путем объединения подходящего существительного из кортежа declensions и количества amount, в следующем формате:

<количество> <существительное>
Примечание 1. Передаваемый в функцию кортеж легко составить по мнемоническому правилу: один, два, пять. Например:

для слова «арбуз»: арбуз, арбуза, арбузов
для слова «рубль»: рубль, рубля, рублей
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию choose_plural(), но не код, вызывающий ее."""

# 2.13 v1
def choose_plural(amount, declensions):
    answer = f'{amount} '
    a_str = str(amount)
    if (a_str[-1] in '056789') or (len(a_str)>=2 and a_str[-2:] in ['11', '12', '13', '14']):
        answer += declensions[2]
    elif a_str[-1] == '1':
        answer += declensions[0]
    else:
        answer += declensions[1]
    return answer

# print(choose_plural(21, ('пример', 'примера', 'примеров')))
for i in range (40):
    print(choose_plural(i, ('пример', 'примера', 'примеров')))

#%% 2.13 v2
def choose_plural(amount, declensions):
    a = f'0{amount}'
    if a[-1] == '1' and a[-2] != '1':
        return f'{amount} {declensions[0]}'
    elif a[-1] in '234' and a[-2] != '1':
        return f'{amount} {declensions[1]}'
    else:
        return f'{amount} {declensions[2]}'

for i in range (40):
    print(choose_plural(i, ('пример', 'примера', 'примеров')))

#%% 2.13 v3
def choose_plural(amount, declensions):
    a = str(amount)
    if a.endswith(('0', '5', '6', '7', '8', '9', '11', '12', '13', '14')):
        return f'{amount} {declensions[2]}'
    elif a.endswith('1'):
        return f'{amount} {declensions[0]}'
    else:
        return f'{amount} {declensions[1]}'

for i in range (40):
    print(choose_plural(i, ('пример', 'примера', 'примеров')))


#%% 2.14 - Функция get_biggest() 🌶️🌶️

"""Реализуйте функцию get_biggest(), которая принимает один аргумент:

numbers — список целых неотрицательных чисел
Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers. Если список numbers пуст, функция должна вернуть число −1.

Примечание 1. Рассмотрим первый тест со списком чисел [1, 2, 3], из которых можно составить следующие числа: 123,132,213,231,312,321
Наибольшим из представленных является 321.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_biggest(), но не код, вызывающий ее."""
# 2.14 v1
def get_biggest(numbers=[]):
    if numbers:
        max_len_n = len(str(max(numbers, key=lambda x: len(str(x)))))
        answer = []
        for n in numbers:
            n_mod = str(n)*max_len_n
            answer.append((n_mod, n))
        answer = sorted(answer, reverse=True)
        answer = ''.join([str(elem[1]) for elem in answer])
        answer = int(answer)
        return answer
    else:
        return -1

#%% 2.14 v2
def get_biggest(numbers):
    if numbers:
        max_len = len(str(max(numbers)))
        return int(''.join(map(str, sorted(numbers, key=lambda x: str(x)*max_len, reverse=True))))
    return -1


# Testing
import pathlib
t_folder = '/Users/zwar/Downloads/tests_2310080'

# подсчет, сколько всего тестовых файлов (считаем файлы с ответами)
t_count = 0
for f in pathlib.Path(t_folder).iterdir():
    if str(f).endswith('.clue'):
        t_count += 1

# прогоняем все тесты и выводим решение
def code_test(t_c, folder):
    for test in range(1, t_c+1):
        print('test No', test)
        t_address = folder + f'/{test}'
        a_address = folder + f'/{test}.clue'
        with open(t_address, 'r', encoding='utf-8') as t,\
            open(a_address, 'r', encoding='utf-8') as a:
            print('answer:  ', end='')
            exec(t.readline().strip())
            print('correct:', a.readline())
            print()

code_test(t_count, t_folder)


#%% 2.2.1 - Тимур, Артур и новый курс

"""Сегодня Тимур ждёт в гости своего друга Артура, чтобы спланировать работу по новому курсу "ООП на Python". Чтобы подготовиться к встрече, Тимуру необходимо посетить два магазина, расположенных рядом с его домом. От дома до первого магазина ведёт дорожка длиной d1 метров, а до второго магазина ведёт дорожка длиной d2 метров. Также существует дорожка, соединяющая два магазина друг с другом, длиной d3 метров.

Напишите программу, которая вычисляет минимальное расстояние, которое потребуется пройти Тимуру, чтобы посетить оба магазина и вернуться домой. Тимур всегда стартует из дома. Он должен посетить оба магазина, перемещаясь только по имеющимся трём дорожкам, и вернуться назад домой. При этом его совершенно не смутит, если ему придётся посетить один и тот же магазин или пройти по одной и той же дорожке более одного раза. Единственная его задача — минимизировать суммарное пройденное расстояние.

Формат входных данных
На вход программе подаются 3 натуральных числа  d1, d2, d3 — длины дорожек, каждое на отдельной строке:
d1 — длина дорожки, соединяющая дом Тимура и первый магазин
d2 — длина дорожки, соединяющая дом Тимура и второй магазин
d3 — длина дорожки, соединяющая магазины
Формат выходных данных
Программа должна вывести минимальное количество метров, которое придётся пройти Тимуру, чтобы посетить оба магазина и вернуться домой."""

def min_way(d1:int, d2:int, d3:int):
    return min([d1+d3+d2, 2*(d1+d2), 2*(d1+d3), 2*(d2+d3)])
# print(min_way(int(input()), int(input()), int(input())))

# Testing
import pathlib
t_folder = '/Users/zwar/Downloads/tests_2310068'
# подсчитываем тесты (по файлам с ответами)
t_count = 0
for t in pathlib.Path(t_folder).iterdir():
    if str(t).endswith('.clue'):
        t_count += 1

for i in range(1, t_count + 1):
    t_address = t_folder + f'/{i}'
    a_address = t_folder + f'/{i}.clue'
    with open(t_address, 'r', encoding='utf-8') as t,\
        open(a_address, 'r', encoding='utf-8') as a:
        d1, d2, d3 = [int(t.readline().strip()) for _ in range(3)]
        print(min_way(d1, d2, d3))
        print(a.readline())
        print()


#%% 2.2.2 - Схожие буквы

"""В русском и английском языках есть буквы, которые выглядят одинаково. 
Вот список английских букв "AaBCcEeHKMOoPpTXxy", 
а вот их русские аналоги "АаВСсЕеНКМОоРрТХху". 
Напишите программу, которая для трёх букв из данных списков букв определяет, русские они, английские или и те и другие (смесь русских и английских букв).

Формат входных данных
На вход программе подаются три буквы из указанных в условии наборов букв, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести

ru, если все три буквы русские
en, если все три буквы английские
mix, если среди букв есть как русские, так и английские
Примечание 1. Гарантируется, что введенные три буквы находятся в наборе "AaBCcEeHKMOoPpTXxy" + "АаВСсЕеНКМОоРрТХху" (английские + русские буквы).
"""
# 2.2.2 v1
def check_lang_3_letters(l_list):
    answer = []
    for letter in l_list:
        # print(f'leter: {letter}, number: {ord(letter)}')
        if 64 < ord(letter) < 91 or 96 < ord(letter) < 123:
            answer.append('en')
        elif 1039 < ord(letter) < 1104:
            answer.append('ru')
        else:
            return None
    if all(map(lambda x: True if x == 'en' else False, answer)):
        return 'en'
    elif all(map(lambda x: True if x == 'ru' else False, answer)):
        return 'ru'
    elif any(map(lambda x: True if x == 'None' else False, answer)):
        return None
    else:
        return 'mix'

print(check_lang_3_letters([input(), input(), input()]))
    

# Testing
from pathlib import Path
t_folder = 'tests'

# подсчитываем тесты (по файлам с ответами)
t_count = 0
for t in Path(t_folder).iterdir():
    if str(t).endswith('.clue'):
        t_count += 1

# тестирование
for i in range(1, t_count + 1):
    t = t_folder + f'/{i}'
    a = t_folder + f'/{i}.clue'
    with open(t, 'r', encoding='utf-8') as f_t,\
        open(a, 'r', encoding='utf-8') as f_a:
        letters = [f_t.readline().strip() for _ in range(3)]
        print(f'test No {i}')
        print(f'leters: {letters}')
        print('answer: ', check_lang_3_letters(letters))
        print('correct:', f_a.readline())
        print()

#%% 2.2.2 v2
def check_lang_3_letters(l_list):
    l = ['ru', 'mix', 'mix', 'en']
    en = 'AaBCcEeHKMOoPpTXxy'
    return (l[sum(letter in en for letter in l_list)])

# print(check_lang_3_letters([input() for _ in range(3)]))


# Testing
from pathlib import Path
t_folder = 'tests'

# подсчитываем тесты (по файлам с ответами)
t_count = 0
for t in Path(t_folder).iterdir():
    if str(t).endswith('.clue'):
        t_count += 1

# тестирование
for i in range(1, t_count + 1):
    t = t_folder + f'/{i}'
    a = t_folder + f'/{i}.clue'
    with open(t, 'r', encoding='utf-8') as f_t,\
        open(a, 'r', encoding='utf-8') as f_a:
        letters = [f_t.readline().strip() for _ in range(3)]
        print(f'test No {i}')
        print(f'leters: {letters}')
        print('answer: ', check_lang_3_letters(letters))
        print('correct:', f_a.readline())
        print()


#%% 2.2.3 - Переворатор

"""Дана последовательность натуральных чисел от 1 до n. Напишите программу, которая сначала располагает в обратном порядке часть элементов этой последовательности от элемента с номером X до элемента с номером Y, а затем от элемента с номером A до элемента с номером B.
На вход программе подаются 5 натуральных чисел, разделенных пробелом: n, X, Y, A, B
Формат выходных данных
Программа должна сформировать последовательность чисел, согласно условию задачи, и вывести их, разделяя пробелом.

Примечание 1. Нумерация членов последовательности начинается с единицы.

"""

def rotate(st):
    # print(st)
    n, x, y, a, b = map(lambda x: int(x), st.split())
    arr = list(range(n+1))
    answer = arr[:x] + arr[y:x-1:-1] + arr[y+1:]
    answer = answer[:a] + answer[b:a-1:-1] + answer[b+1:]
    return ' '.join(map(str, answer[1:]))

# print(rotate(input()))


## testing
from pathlib import Path
t_folder = 'tests'

# подсчитываем тесты (по файлам с ответами)
t_count = 0
for t in Path(t_folder).iterdir():
    if str(t).endswith('.clue'):
        t_count += 1

# тестируем
for i in range(1, t_count + 1):
    t = t_folder + f'/{i}'
    a = t_folder + f'/{i}.clue'
    with open(t, 'r', encoding='utf-8') as f_t,\
        open(a, 'r', encoding='utf-8') as f_a:
        ans_1 = rotate(f_t.readline())
        ans_0 = f_a.readline().strip()
        print(f'test No {i}')
        print('answer ', ans_1)
        print('correct', ans_0)
        print(['wrong', 'O.K.'][ans_0 == ans_1])
        print()


#%% 2.2.4 - Более одного

"""Дана последовательность неотрицательных целых чисел. Напишите программу, которая выводит те числа, которые встречаются в данной последовательности более одного раза.

Формат входных данных
На вход программе подается строка, содержащая целые неотрицательные числа, разделенные пробелом.

Формат выходных данных
Программа должна вывести те числа, которые встречаются в данной строке более одного раза, разделяя их пробелом. Числа должны быть расположены в порядке возрастания и не должны повторяться.

Примечание 1. Если повторяющихся чисел в исходной строке нет, программа ничего не должна выводить."""

def more_then_one(st:str):
    answer = dict()
    for num in st.split():
        answer[num] = answer.get(num, 0) + 1
    answer = list(filter(lambda x: answer[x] > 1, answer))
    return ' '.join(sorted(answer, key=lambda x: int(x)))

# print(more_then_one(input()))


# TESTING
file_name = 'tests_2313029'
file_name = f'tests/{file_name}.zip'
# открываем zip-файл
from zipfile import ZipFile
with ZipFile(file_name, 'r') as zip_file:

    # zip_file.printdir()  # выводим соедржимое zip-файла
    
    # with zip_file.open('1') as f:
    #     print(f.read().decode('utf-8'))  # содержимое файла 1
    
    
    # подсчитываем к-во тестов
    t_numbers = int(len(zip_file.infolist()) / 2)
    for i in range(1, t_numbers+1):
        # открываем файл с тестом и с ответом
        with zip_file.open(f'{i}', 'r') as t,\
            zip_file.open(f'{i}.clue', 'r') as a:
            t = t.read().decode('utf-8')
            a = a.read().decode('utf-8')
            print(f'test No {i}')
            print('input:  ', t)
            print('answer: ', more_then_one(t))
            print('correct:', a)
            print()


#%% 2.2.5 - Максимальная группа
"""
Назовем набор различных натуральных чисел группой. Например (13, 4, 22 ,40) Тогда длиной группы будем считать количество чисел в группе. Например, длина группы (13, 4, 22 ,40)=4
Дана последовательность натуральных чисел от 1 до n включительно. Напишите программу, которая группирует все числа данной последовательности по сумме их цифр и определяет длину группы, содержащей наибольшее количество чисел.

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна сгруппировать все числа из натуральной последовательности от 1 до n по сумме их цифр и определить длину группы, содержащей наибольшее количество чисел.

Пример: 
n = 20
последовательность: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
Сгруппируем полученные числа по сумме их цифр:
(1, 10), (2, 11, 20), (3, 12), (4, 13), (5, 14), (6, 15), (7, 16), (8, 17), (9, 18), (19)
Длина группы с наибольшим количеством чисел равна 3
"""

def group_max_len(st:str):
    seq = [str(i) for i in range(int(st) + 1)]
    seq = list(map(lambda x: sum([int(i) for i in x]), seq))
    answer = dict()
    for elem in seq:
        answer[elem] = answer.get(elem, 0) + 1
    return max(answer.values())

# 2.2.5 v2
def group_max_len_2(st:str):
    answer = dict()
    for i in range(1, int(st) + 1):
        num_sum = sum(map(lambda x: int(x), str(i)))
        answer[num_sum] = answer.get(num_sum, 0) + 1
    return max(answer.values())

# print(group_max_len(input()))
# print(group_max_len('20'))

# TESTING
func_name = group_max_len_2###
file_name = 'tests_2959799.zip'
file_name = f'tests/{file_name}'
# открываем zip-файл
from zipfile import ZipFile
with ZipFile(file_name, 'r') as zip_file:
    pass

    # zip_file.printdir()  # выводим соедржимое zip-файла
    
    # with zip_file.open('1') as f:
    #     print(f.read().decode('utf-8'))  # содержимое файла 1
    
    
    # подсчитываем к-во тестов
    t_numbers = int(len(zip_file.infolist()) / 2)
    for i in range(1, t_numbers+1):
        # открываем файл с тестом и с ответом
        with zip_file.open(f'{i}', 'r') as t,\
            zip_file.open(f'{i}.clue', 'r') as a:
            t = t.read().decode('utf-8')
            a = a.read().decode('utf-8')
            print(f'test No {i}')
            print('input:  ', t)  # выводим входные данные
            print('answer: ', func_name(t))  # вызов функции
            print('correct:', a)  # выводим ответ
            print()


#%% 2.2.6 - Трудности перевода

"""Зачастую переводить сериалы, не теряя изначальный смысл, невозможно, особенно за счет игр слов. Сумасшедший режиссер хочет снять сериал, в котором бы в целях эксперимента задействовал как можно больше языков, чтобы пользоваться красотой каждого из них. Тем не менее если задействовать слишком много языков, то сериал станет непонятен абсолютно всем, поэтому режиссер достает случайных людей на улице и спрашивает их, какие языки они знают, таким образом он будет использовать языки которые знают все из них.

Напишите программу, которая определяет, какие языки будут использоваться в сериале.

Формат входных данных
На вход программе в первой строке подается число n — количество людей, которых донимает режиссер. В каждой из следующих n строк через запятую и пробел указывается список языков, которые знает человек.

Формат выходных данных
Программа должна вывести список языков для сериала в лексикографическом порядке. Если такой список составить нельзя, необходимо вывести текст: 
Сериал снять не удастся"""


def check_lang(list_0:list):
    answer = set(list_0[0].split(', '))
    for people in list_0:
        answer = answer & set(people.split(', '))
    return ', '.join(sorted(answer)) if answer else 'Сериал снять не удастся'

# list_for_input = [input() for _ in range(int(input()))]
# print(check_lang(list_for_input))


# TESTING
func_name = check_lang
file_name = 'tests_2310083.zip'
folder_name = 'tests'

# открываем zip-файл
from zipfile import ZipFile
with ZipFile(f'{folder_name}/{file_name}', 'r') as zip_file:
    pass

    # zip_file.printdir()  # выводим соедржимое zip-файла
    
    # with zip_file.open('1') as f:
    #     print(f.read().decode('utf-8'))  # выводим содержимое файла 1
    
    # подсчитываем к-во тестов
    t_numbers = int(len(zip_file.infolist()) / 2)
    
    # запускаем тесты
    for i in range(1, t_numbers+1):
        # открываем файлы с тестом и с ответом
        with zip_file.open(f'{i}', 'r') as t,\
            zip_file.open(f'{i}.clue', 'r') as a:
            t = t.read().decode('utf-8')
            a = a.read().decode('utf-8')
            print(f'test No {i}')

            # готовим данные для передачи в функицю
            list_for_input = [row for row in t.split('\n')][1:]

            # print('input:  ', t)  # выводим входные данные
            print('answer: ', func_name(list_for_input))  # вызов функции
            print('correct:', a)  # выводим ответ
            print()


#%% 2.2.7 - Схожие слова

"""Напишите программу, которая находит все схожие слова для заданного слова. Слова называются схожими, если имеют одинаковое количество и расположение гласных букв. При этом сами гласные могут различаться.

Формат входных данных
На вход программе подается одно слово, записанное в первой строке, затем натуральное число n — количество слов для сравнения и n строк со словами.

Формат выходных данных
Программа должна вывести все схожие слова для заданного слова, сохранив их исходный порядок следования.

Примечание 1. После последней гласной в начальном и проверяемом слове может быть любое количество согласных.

Примечание 2. В русском языке 
10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) и 
21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ)."""

v = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
c = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')
word = input()
word = (word, ''.join(['0' if l in v else '1' for l in word]))
# print('word', word)
n = int(input())
answer = list()
for _ in range(n):
    word_check = input()
    word_check = (word_check, ''.join(['0' if l in v else '1' for l in word_check]))
    # print('word      ', word)
    # print('word_check', word_check)
    # print('word_check', word_check[1][:word_check[1].rfind('0')+1])
    if word[1][:word[1].rfind('0')+1] == word_check[1][:word_check[1].rfind('0')+1]:
        answer.append(word_check[0])
    # print('answer', answer)
    # print()
print(*answer, sep='\n')


#%% 2.2.8 - Корпоративная почта 🌶️

"""В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая формируется как <имя-фамилия>@beegeek.bzz, например, timyr-guev@beegeek.bzz. При таком подходе существует проблема тёзок. Для решения такой проблемы было решено приписывать справа номер.

Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера), второй — timyr-guev1@beegeek.bzz, третий — timyr-guev2@beegeek.bzz, и так далее.

Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников в заранее подготовленном виде (латиницей с символом - между ними). Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

Формат входных данных
На вход программе в первой строке подается целое неотрицательное число n — количество выданных ящиков. В следующих n строках перечислены сами ящики в порядке выдачи, по одному на строке. На следующей строке задано целое неотрицательное число m — количество новых сотрудников, которым нужно раздать корпоративные ящики. Каждая из последующих m строк представляет собой имя и фамилию сотрудника в подготовленном к использованию формате.

Формат выходных данных
Программа должна вывести почтовые ящики (m строк) для новых сотрудников в том порядке, в котором они раздавались."""

t_in = [
    ['ivan-petrov@beegeek.bzz', 'petr-ivanov@beegeek.bzz', 'ivan-petrov1@beegeek.bzz', 'ivan-ivanov@beegeek.bzz', 'ivan-ivanov1@beegeek.bzz', 'ivan-ivanov2@beegeek.bzz'],
    ['timyr-guev2@beegeek.bzz', 'anri-tabuev@beegeek.bzz'],
    ['anri-tabuev1@beegeek.bzz', 'arthur-kharisov3@beegeek.bzz']
]
names = [
    ['ivan-ivanov', 'petr-petrov', 'petr-ivanov'],
    ['timyr-guev', 'timyr-guev', 'anri-tabuev'],
    ['anri-tabuev', 'anri-tabuev', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov']
]

test_n = 2
t_in = t_in[test_n]
names = names[test_n]
print('test No', test_n+1)

# t_in = [input() for _ in range(int(input()))]
# names = [input() for _ in range(int(input()))]

def rfind_alfa(text):
    """ищет индекс первой буквы справа"""
    letters = '0123456789'
    poz_alfa = len(text) - 1
    while poz_alfa >-1 and text[-1] in letters:
        poz_alfa -= 1
        text = text[:-1]
    return poz_alfa

# формируем словарь, связанный со старыми именами
mails_old = dict()
for mail in t_in:
    fio = mail.split('@')[0]
    number_index = rfind_alfa(fio)
    if number_index < len(fio) - 1:
        number = int(fio[number_index + 1:])
    else:
        number = 0
    fio = fio[:number_index + 1]
    mails_old.setdefault(fio, []).append(number)

# формируем словарь свзяанный с новыми именами
# и по ходу выводим новые добавленные имена
mails_new = mails_old.copy()
for name in names:
    if name in mails_new:
        j = 0
        while j in mails_new[name]:
            j += 1
        mails_new.setdefault(name, []).append(j)
        if mails_new[name][-1] == 0:
            print(f'{name}@beegeek.bzz')
        else:
            print(f'{name}{mails_new[name][-1]}@beegeek.bzz')
    else:
        mails_new.setdefault(name, []).append(0)
        print(f'{name}@beegeek.bzz')


# print('test No', test_n)
# print('mails_old\n', mails_old)
# print('mails_new\n', mails_new)

#%% 2.2.8 v2
t_in = [
    ['ivan-petrov@beegeek.bzz', 'petr-ivanov@beegeek.bzz', 'ivan-petrov1@beegeek.bzz', 'ivan-ivanov@beegeek.bzz', 'ivan-ivanov1@beegeek.bzz', 'ivan-ivanov2@beegeek.bzz'],
    ['timyr-guev2@beegeek.bzz', 'anri-tabuev@beegeek.bzz'],
    ['anri-tabuev1@beegeek.bzz', 'arthur-kharisov3@beegeek.bzz']
]
names = [
    ['ivan-ivanov', 'petr-petrov', 'petr-ivanov'],
    ['timyr-guev', 'timyr-guev', 'anri-tabuev'],
    ['anri-tabuev', 'anri-tabuev', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov', 'arthur-kharisov']
]

test_n = 2
t_in = t_in[test_n]
names = names[test_n]
print('test No', test_n+1)

# t_in = [input() for _ in range(int(input()))]
# names = [input() for _ in range(int(input()))]
for name in names:
    num = 1
    new_email = name + '@beegeek.bzz'
    while new_email in t_in:
        new_email = name + str(num) + '@beegeek.bzz'
        num += 1
    print(new_email)
    t_in.append(new_email)


# %% 2.2.9 - Файлы в файле 🌶️🌶️

"""Вам доступен текстовый файл files.txt, содержащий информацию о файлах. Каждая строка файла содержит три значения, разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:

cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...
Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы, и выводит полученные группы файлов, указывая для каждой ее общий объем. Группы должны быть расположены в лексикографическом порядке названий расширений, файлы в группах — в лексикографическом порядке их имен."""

size_mult = {'B': 1, 'KB':1024**1, 'MB':1024**2, 'GB':1024**3}
size_lable = {0:'B', 1:'KB', 2:'MB', 3:'GB'}

data_files = dict()
data_sizes = dict()
# раскидываем данные из файла по словорями
with open('files.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        file, *size = line.strip().split()
        file_name, file_ext = file.split('.')
        data_files[file_ext] = data_files.get(file_ext, []) + [file]
        data_sizes[file_ext] = data_sizes.get(file_ext, 0) + int(size[0])*size_mult[size[1]]

# округляем размер до максимально большого
for key, value in data_sizes.items():
    number = value
    count = 0
    while number > 1024:
        number /= 1024
        count += 1
    data_sizes[key] = f'{round(number)} {size_lable[count]}'

# выводим ответ
for key, value in sorted(data_files.items()):
    print(*sorted(value), sep = '\n')
    print('----------')
    print('Summary:', data_sizes[key])
    print()
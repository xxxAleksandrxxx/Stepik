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

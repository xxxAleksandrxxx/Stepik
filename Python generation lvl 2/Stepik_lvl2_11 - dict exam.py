#%%
# 11.1.14
'''
Дополните приведенный код, чтобы в списках значений элементов словаря my_dict  не было чисел, больших 20. При этом порядок оставшихся элементов меняться не должен.
'''
'''
# v1
my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}

for key, value in my_dict.items():
    value = [i for i in value if i <= 20]
    my_dict[key] = value
'''
'''
# v2
my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}

my_dict = {key : [i for i in value if i <= 20] for key, value in my_dict.items()}
print(my_dict)
'''
'''
# v3
my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}

# for value in my_dict.values():
#     for i in range(len(value)):
#         print(value[i], end=' ')
#     print()
# print()

for value in my_dict.values():
    for i in range(len(value)-1,-1,-1):
        if value[i] > 20:
            del value[i]

# for key, value in my_dict.items():
#     print(key, ': ', end = '')
#     for i in range(len(value)):
#         print(value[i], end=' ')
#     print()
'''


# 11.1.15
'''
Словарь emails содержит информацию об электронных адресах пользователей, сгруппированных по домену. Дополните приведенный код, чтобы он вывел все электронные адреса в алфавитном порядке, каждый на отдельной строке, в формате username@domain.

Примечание 1. Для сортировки в алфавитном порядке используйте встроенную функцию sorted(), либо списочный метод sort().

Примечание 2. Группировать электронные адреса по доменам не нужно.

emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'], 
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'], 
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'], 
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
'''
'''
emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'], 
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'], 
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'], 
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

emails_list = list()
for key, value in emails.items():
    for elem in value:
        emails_list.append(f'{elem}@{key}')

for elem in sorted(emails_list):
    print(elem)
'''


# 11.2.1 Минутка генетики
'''
Как известно из курса биологии ДНК и РНК – последовательности нуклеотидов.

Четыре нуклеотида в ДНК:
аденин (A);
цитозин (C);
гуанин (G);
тимин (T).
Четыре нуклеотида в РНК:
аденин (A);
цитозин (C);
гуанин (G);
урацил (U).
Цепь РНК строится на основе цепи ДНК последовательным присоединением комплементарных нуклеотидов:

G → C;
C → G;
T → A;
A → U.
Напишите программу, переводящую цепь ДНК в цепь РНК.

Формат входных данных
На вход программе подается корректная цепь ДНК в верхнем регистре.

Формат выходных данных
Программа должна вывести соответствующую цепь РНК в верхнем регистре.
'''
'''
# v1 
dna_to_rna_dict = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
for elem in input():
    print(dna_to_rna_dict[elem], end='')
'''
'''
# v2
dna_to_rna_dict = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
print(''.join([dna_to_rna_dict[letter] for letter in input()]))
'''


# 11.2.2 Порядковый номер
'''
Дана строка текста на русском языке, состоящая из слов и символов пробела. Словом считается последовательность букв, слова разделены одним пробелом или несколькими.

Напишите программу, определяющую для каждого слова порядковый номер его вхождения в текст именно в этой форме, с учетом регистра. Для первого вхождения слова программа выведет 1, для второго вхождения того же слова — 2 и т. д.

Формат входных данных
Программа получает на вход единственную строку текста, состоящую только из русских букв и символов пробела. 

Формат выходных данных
Для каждого слова исходного текста программа выводит одно целое число — номер вхождения этого слова в текст. Числа необходимо вывести на одной строке через пробел.

Примечание. Количество чисел должно совпадать с количеством слов исходного текста.
'''
'''
t = 'прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон'
a = '1 1 2 1 1 2 1 2 3 1'

t = input()

t_dict = dict()
answer = ''
for word in t.split():
    t_dict[word] = t_dict.get(word, 0) + 1
    answer = ' '.join([answer, str(t_dict[word])])
answer = answer[1:]
# print('a     ', a)
print('answer', answer)
# print(t_dict)
'''


# 11.2.3 Scrabble game
'''
В игре Scrabble каждая буква приносит определенное количество баллов. Общая стоимость слова – сумма баллов его букв. Чем реже буква встречается, тем больше она ценится:
Баллы	Буква
1       A, E, I, L, N, O, R, S, T, U
2       D, G
3       B, C, M, P
4       F, H, V, W, Y
5       K
8       J, X
10      Q, Z
Напишите программу подсчета итоговой стоимости введенного слова.

Формат входных данных
На вход программе подается одно слово в верхнем регистре на английском языке.

Формат выходных данных
Программа должна вывести суммарную стоимость букв введеного слова.
'''
'''
# v1
word_count_dict = dict.fromkeys(('A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'), 1)
word_count_dict = word_count_dict | dict.fromkeys(('D', 'G'), 2)
word_count_dict = word_count_dict | dict.fromkeys(('B', 'C', 'M', 'P'), 3)
word_count_dict = word_count_dict | dict.fromkeys(('F', 'H', 'V', 'W', 'Y'), 4)
word_count_dict = word_count_dict | dict.fromkeys(('K'), 5)
word_count_dict = word_count_dict | dict.fromkeys(('J', 'X'), 8)
word_count_dict = word_count_dict | dict.fromkeys(('Q', 'Z'), 10)

answer = 0
for letter in input():
    answer += word_count_dict[letter]
print(answer)
'''
'''
# v2
word_count_dict = dict.fromkeys(('A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'), 1)
word_count_dict = word_count_dict | dict.fromkeys(('D', 'G'), 2)
word_count_dict = word_count_dict | dict.fromkeys(('B', 'C', 'M', 'P'), 3)
word_count_dict = word_count_dict | dict.fromkeys(('F', 'H', 'V', 'W', 'Y'), 4)
word_count_dict = word_count_dict | dict.fromkeys(('K'), 5)
word_count_dict = word_count_dict | dict.fromkeys(('J', 'X'), 8)
word_count_dict = word_count_dict | dict.fromkeys(('Q', 'Z'), 10)

print(sum([word_count_dict[elem] for elem in input()]))
'''


# 11.2.4 Строка запроса
'''
Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения. Она начинается после вопросительного знака и идет до конца адреса. Например:

https://beegeek.ru?name=timur     # строка запроса: name=timur
Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:

https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green 
Напишите функцию build_query_string(), которая принимает на вход словарь с параметрами и возвращает строку запроса, сформированную из этих параметров.

Примечание 1. В итоговой строке параметры должны быть отсортированы в лексикографическом порядке ключей словаря.

Примечание 2. Следующий программный код:

print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
должен выводить:

age=28&name=timur
game=2&sport=hockey&time=17
Примечание 3. Вызывать функцию build_query_string() не нужно, требуется только реализовать. 
'''
'''
def build_query_string(my_dict):
    answer = []
    for key, value in my_dict.items():
        answer.append(f'{key}={value}')
    answer.sort()
    answer = '&'.join(answer)
    return answer

print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
'''

# 11.2.5 Слияние словарей 🌶️
'''
Напишите функцию merge(), объединяющую словари в один общий. Функция должна принимать список словарей и возвращать словарь, каждый ключ которого содержит множество (тип данных set) уникальных значений собранных из всех словарей переданного списка.

Примечание 1. Следующий программный код:

result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
создает словарь:

result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
Примечание 2. Вызывать функцию merge() не нужно, требуется только реализовать. 

Примечание 3. Слияние пустых словарей должно быть пустым словарем. 
'''
'''
t = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]
a = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}


def merge(values):      # values - это список словарей
    answer = dict()
    for elem in values:
        for key, value in elem.items():
            # print('elem', elem, 'key', key, 'value', value)
            answer.setdefault(key, set()).add(value)
            # print(answer.setdefault(key, value))
    return answer

print(merge(t))
print(a)
print(merge([{},{}]))
'''


# 11.2.6 Опасный вирус 😈
'''
В файловую систему компьютера, на котором развернута наша ❤️ платформа Stepik, проник опасный вирус и сломал контроль прав доступа к файлам. Говорят, вирус написал один из студентов курса Python для начинающих.

Для каждого файла известно, с какими действиями можно к нему обращаться:

запись W (write, доступ на запись в файл);
чтение R (read, доступ на чтение из файла);
запуск X (execute, запуск на исполнение файла).
Напишите программу для восстановления контроля прав доступа к файлам. Ваша программа для каждого запроса должна будет возвращать OK если выполняется допустимая операция, и Access denied, если операция недопустима.

Формат входных данных
Программа получает на вход количество файлов n, содержащихся в файловой системе компьютера. Далее идет n строк, на каждой имя файла и допустимые с ним операции, разделенные символом пробела. В следующей строке записано число m — количество запросов к файлам, и затем m строк с запросами вида операция файл. Одному и тому же файлу может быть адресовано любое количество запросов.

Формат выходных данных
Программа должна вывести для каждого из m запросов в отдельной строке Access denied или OK.
'''
'''
n = 5
t1 = ['my_pycode.exe W X', 'log_n X W R', 'ave R', 'lucky_m W R', 'dnsss.py W']
m = 6
t2 = ['execute ave', 'read dnsss.py', 'write log_n', 'execute log_n', 'read ave', 'write my_pycode.exe']
a = ['Access denied', 'Access denied', 'OK', 'OK', 'OK', 'OK']

# n = int(input())
# t1 = [input() for _ in range(n)]
# m = int(input())
# t2 = [input() for _ in range(m)]

word_to_letter_dict = {'write':'W', 'read':'R', 'execute':'X'}
t1_dict = {elem.split()[0] : elem.split()[1:] for elem in t1}

# print(t1_dict)
# print(t2_dict)

for elem in t2:
    print(('Access denied', 'OK')[word_to_letter_dict[elem.split()[0]] in t1_dict[elem.split()[1]]])
'''

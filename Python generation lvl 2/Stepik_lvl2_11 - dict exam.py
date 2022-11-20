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
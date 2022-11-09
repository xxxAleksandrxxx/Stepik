#%%
# 10.2.11
'''Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), чей номер оканчивается на 8.

Примечание. Имена необходимо вывести на одной строке, разделяя символом пробела.
'''

users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
'''
# v1
answer = list()
for line in users:
    if line['phone'][-1]=='8':
        answer.append(line['name'])
print(*sorted(answer))
'''
'''
# v2
print(*sorted([line['name'] for line in users if line['phone'].endswith('8')]))
'''


# 10.2.11

'''Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), у которых нет информации об электронной почте. 

Примечание 1. Ключ email может отсутствовать в словаре.
Примечание 2. Имена необходимо вывести на одной строке, разделяя символом пробела.
'''
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
'''
no_mail_usr = [user['name'] for user in users if 'email' not in user or user['email'] == '']
print(*sorted(no_mail_usr))
'''


# 10.2.12 Строковое представление
'''
Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:

0 на zero;
1 на one;
2 на two;
3 на three;
4 на four;
5 на five;
6 на six;
7 на seven;
8 на eight;
9 на nine.
Формат входных данных
На вход программе подается натуральное число.

Формат выходных данных
Программа должна вывести строковое представление числа.

Примечание. Используйте словарь вместо условного оператора.
'''
'''
# v1 меняем число в формате str
num_dict = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}

num = input()
for el in num:
    print(num_dict[el], end=' ')
'''
'''
# v2 меняем число в формате int
num_dict = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
n = int(input())
num_list = [num_dict[n%10]]
while n//10 != 0:
    n //= 10
    num_list.append(num_dict[n%10])

num_list = num_list[::-1]
print(*num_list)
'''
'''
# v3  меняем число в формате int
num_dict = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
n = int(input())
num_list = [num_dict[n%10]]
while n//10 != 0:
    n //= 10
    num_list.insert(0, num_dict[n%10])

print(*num_list)
'''


# 10.2.13 Информация об учебных курсах
'''
Напишите программу, которая по номеру курса выводит информацию о данном курсе. 
Формат входных данных
На вход программе подается одна строка – номер курса.

Формат выходных данных
Программа должна вывести номер курса, затем номер аудитории, имя преподавателя и время проведения курса в соответствии с примерами.

Примечание 1. Используйте словарь вместо условного оператора.
Примечание 2. Для удобного вывода используйте строковый метод format() или f-строки.
'''
'''
# v1
course_schedule = [{'CS101': [3004, 'Хайнс', '8:00']},
                   {'CS102': [4501, 'Альварадо', '9:00']},
                   {'CS103': [6755, 'Рич', '10:00']},
                   {'NT110': [1244, 'Берк', '11:00']},
                   {'CM241': [1411, 'Ли', '13:00']}]
group = input()
for elem in course_schedule:
    if group in elem:
        a,b,c = elem[group]
        print(f'{group}: {a}, {b}, {c}')
'''
'''
# v2
course_schedule = {
    'CS101': [3004, 'Хайнс', '8:00'],
    'CS102': [4501, 'Альварадо', '9:00'],
    'CS103': [6755, 'Рич', '10:00'],
    'NT110': [1244, 'Берк', '11:00'],
    'CM241': [1411, 'Ли', '13:00']
    }
group = input()
if group in course_schedule:
    print('{0}: {1}, {2}, {3}'.format(group, *course_schedule[group]))
'''
'''
# v3
course_schedule = {
    'CS101': {'aud': 3004, 'name': 'Хайнс', 'time': '8:00'},
    'CS102': {'aud': 4501, 'name': 'Альварадо', 'time': '9:00'},
    'CS103': {'aud': 6755, 'name': 'Рич', 'time': '10:00'},
    'NT110': {'aud': 1244, 'name': 'Берк', 'time': '11:00'},
    'CM241': {'aud': 1411, 'name': 'Ли', 'time': '13:00'}
    }
group = input()
print('{}: {}, {}, {}'.format(group, *course_schedule[group].values()))
'''



# 
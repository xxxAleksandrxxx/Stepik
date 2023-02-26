#%% 3.1.19
"""Вам доступен список dates, содержащий даты. Дополните приведенный ниже код, чтобы он вывел год и номер квартала каждой даты из данного списка. Компоненты дат должны быть расположены в исходном порядке, каждые на отдельной строке, в следующем формате:

<год>-Q<номер квартала>"""

# v1
from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

Q = {num+1:f'Q{1 + num//3}' for num in range(12)}

for d in dates:
    print(f'{d.year}-{Q[d.month]}')

#%% 3.1.19 v2
from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

for d in dates:
    print(f'{d.year}-Q{1 + (d.month - 1)//3}')


#%% 3.1.20 - Функция get_min_max()

"""Реализуйте функцию get_min_max(), которая принимает один аргумент:

dates — список дат (тип date)
Функция должна возвращать кортеж, первым элементом которого является минимальная дата из списка dates, вторым — максимальная дата из списка dates. Если список dates пуст, функция должна вернуть пустой кортеж.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_min_max(), но не код, вызывающий ее."""
from datetime import date

def get_min_max(dates):
    return (min(dates), max(dates)) if dates else ()


dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
print(get_min_max([]))

# # TESTING
# file_name = 'tests_2489841'
# file_name = f'tests/{file_name}.zip'
# # открываем zip-файл
# from zipfile import ZipFile
# with ZipFile(file_name, 'r') as zip_file:
#     # выводим соедржимое zip-файла
#     # zip_file.printdir()

#     # содержимое файла 1
#     with zip_file.open('2') as f:
#         print(f.read().decode('utf-8'))


#%% 3.1.11 - Функция get_date_range()

"""Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно. Если start > end, функция должна вернуть пустой список.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_date_range(), но не код, вызывающий ее."""

# 3.1.11 v1
from datetime import date

def get_date_range(start, end):
    start = start.toordinal()
    end = end.toordinal()
    answer = []
    while start < end + 1:
        answer.append(date.fromordinal(start))
        start += 1
    return answer

date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')


## TESTING
from zipfile import ZipFile
file_name = 'tests_2489842'
file_name = f'tests/{file_name}.zip'
with ZipFile(file_name, 'r') as z:
    z.printdir()
    with z.open('1.clue', 'r') as f:
        print(f.read().decode('utf-8'))


#%% 3.1.11 v2
from datetime import date

def get_date_range(start, end):
    return [date.fromordinal(d) for d in range(start.toordinal(), end.toordinal() + 1)]

## TESTING
from zipfile import ZipFile
file_name = 'tests_2489842'
file_name = f'tests/{file_name}.zip'
with ZipFile(file_name, 'r') as z:
    z.printdir()
    with z.open('1.clue', 'r') as f:
        print(f.read().decode('utf-8'))



#%% 3.1.12 - Функция saturdays_between_two_dates()

"""Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция должна возвращать количество суббот между датами start и end включительно.

Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию saturdays_between_two_dates(), но не код, вызывающий ее."""

from datetime import date

def saturdays_between_two_dates(start, end):
    start, end = sorted((start.toordinal(), end.toordinal()))
    answer = abs(start - end)//7
    for d in range(end - abs(start - end)%7, end + 1):
        if date.fromordinal(d).isoweekday() == 6:
            answer += 1
    return answer

#%% 3.1.12 v2
from datetime import date

def saturdays_between_two_dates(start, end):
    start, end = sorted((start.toordinal(), end.toordinal()))
    return (end - start)//7 + (date.fromordinal(start).isoweekday()%7 + (end - start)%7 >= 6)



## TESTING
from zipfile import ZipFile
file_name = 'tests_3057804.zip'
file_name = f'tests/{file_name}'
with ZipFile(file_name, 'r') as z:
    # z.printdir()
    test = 4
    print('\nTest:')
    with z.open(f'{test}', 'r') as f:
        print(f.read().decode('utf-8'))
    print('\nAnswer:')
    with z.open(f'{test}.clue', 'r') as f:
        print(f.read().decode('utf-8'))

#%% 3.3.13
from datetime import datetime

text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')

print(dt)

#%% 3.3.13 v2
from datetime import datetime

text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
dt = datetime.strptime(text, text.replace('15.07.2022 в 08:30', '%d.%m.%Y в %H:%M'))

print(dt)


#%% 3.3.14
"""
Дополните приведенный ниже код, чтобы он преобразовал секунды seconds (прошедшие от начала эпохи) в объект datetime и, наоборот, объект datetime в секунды (прошедшие от начала эпохи).
from datetime import datetime

seconds = 2483228800
dt = datetime(2011, 11, 4)

print(datetime.____(seconds))
print(dt.____())
"""

from datetime import datetime
seconds = 2483228800
dt = datetime(2011, 11, 4)

print(datetime.fromtimestamp(seconds))
print(dt.timestamp())


#%% 3.3.15
"""
Вам доступен список times_of_purchases, содержащий даты (тип datetime), в которые были совершены покупки в некотором интернет-магазине. Дополните приведенный ниже код, чтобы он вывел текст До полудня, если большее число покупок было совершено до полудня, или текст После полудня в противном случае.
"""
from datetime import datetime

times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26), datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59), datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53), datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3), datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5), datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54), datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45), datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57), datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42), datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12), datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27), datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41), datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44), datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

# for elem in times_of_purchases:
#     print(str(elem.time()) < '12:00:00')

b = map(lambda x: 'До полудня' if x.time() < datetime(x.year, x.month, x.day, 12, 0, 0).time() else 'После полудня', times_of_purchases)

c = dict()
for elem in map(lambda x: 'До полудня' if x.time() < datetime(x.year, x.month, x.day, 12, 0, 0).time() else 'После полудня', times_of_purchases):
    c[elem] = c.get(elem, 0) + 1
print(max(c))


#%% 3.3.15 v2

from datetime import datetime

times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26), datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59), datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53), datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3), datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5), datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54), datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45), datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57), datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42), datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12), datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27), datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41), datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44), datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

day_part = [elem.strftime('%p') for elem in times_of_purchases]
print(('До полудня', 'После полудня')[day_part.count('AM') < day_part.count('PM')])


#%% 3.3.16
"""
Вам доступны список dates, содержащий даты, и список times, содержащий времена. Количество элементов в этих списках одинаковое. Дополните приведенный ниже код, чтобы он вывел datetime объекты, полученные путем объединения элементов списков dates и times, находящихся на одинаковых позициях. Полученные объекты должны быть расположены в порядке возрастания секунд, каждый на отдельной строке.
"""

from datetime import date, time, datetime

dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4), date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24), date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59), time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2), time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]

dates_and_times = list()
for i in range(len(dates)):
    dates_and_times.append(datetime.combine(dates[i], times[i]))

print(*sorted(dates_and_times, key=lambda x: x.second), sep='\n')


#%% 3.3.16 v2

from datetime import date, time, datetime

dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4), date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24), date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59), time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2), time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]

date_and_time = [datetime.combine(d, t) for d, t in zip(dates, times)]
print(*sorted(date_and_time, key=lambda x: x.second), sep='\n')


#%% 3.3.17
"""
Ученики онлайн-школы BEEGEEK решили выяснить, кто из них быстрее всех решит домашнее задание по математике. Для этого каждый ученик зафиксировал время начала и окончания решения своей домашней работы.

Вам доступен словарь data, содержащий результаты учеников. Ключом в словаре является имя ученика, а значением — кортеж, первый элемент которого — время начала решения, второй элемент — время окончания решения. Дополните приведенный ниже код, чтобы он вывел имя ученика, который затратил на решение домашнего задания меньше всего времени.

Примечание 1. Гарантируется, что искомый ученик единственный.

Примечание 2. Дата-времена в кортежах представлены в виде строк в формате DD.MM.YYYY HH:MM:SS.
"""

from datetime import datetime

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'), 
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'), 
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'), 
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'), 
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'), 
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'), 
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'), 
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'), 
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'), 
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'), 
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

c = dict()

for k, v in data.items():
    c[k] = abs(datetime.strptime(v[0], '%d.%m.%Y %H:%M:%S').timestamp() - datetime.strptime(v[1], '%d.%m.%Y %H:%M:%S').timestamp())

print(min(c, key=lambda x: c[x]))

#%% 3.3.17 v2
from datetime import datetime

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'), 
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'), 
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'), 
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'), 
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'), 
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'), 
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'), 
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'), 
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'), 
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'), 
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

def g_sec(t_tuple):
    return abs(datetime.strptime(t_tuple[0], '%d.%m.%Y %H:%M:%S') - datetime.strptime(t_tuple[1], '%d.%m.%Y %H:%M:%S'))

print(min(data, key=lambda x: g_sec(data[x])))
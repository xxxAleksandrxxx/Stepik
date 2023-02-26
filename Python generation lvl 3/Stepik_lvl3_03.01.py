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
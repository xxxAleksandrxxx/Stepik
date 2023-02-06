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
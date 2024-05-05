# #######################
# 4.5.14
# Количество файлов
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит единственное число — количество файлов в этом архиве.
# from zipfile import ZipFile

# def count_files1(file_in):
#     with ZipFile(file_in, 'r') as zf:
#         info = zf.namelist()
#     count = 0
#     for elem in info:
#         if elem.endswith("/"):
#             continue
#         else:
#             count += 1
#     # print(count)


# def count_files2(file_in):
#     with ZipFile(file_in, 'r') as zf:
#         a = sum(not elem.is_dir() for elem in zf.infolist())
#         # print(a)


# def count_files3(file_in):
#     with ZipFile(file_in, 'r') as zf:
#         count = 0
#         for elem in zf.infolist():
#             if not elem.is_dir():
#                 count += 1
#     # print(count)


# def execution_time(func, *args, n=10000):
#     from time import monotonic
#     t0 = monotonic()
#     for _ in range(n):
#         func(*args)
#     t1 = monotonic()
#     print(f"{func.__name__:<15} {t1-t0:.2f}")

# if __name__ == "__main__":
#     file_in = "etc/workbook.zip"
#     # count_files2(file_in)

#     funcs = [count_files1, count_files2, count_files3]
#     for func in funcs:
#         execution_time(func, file_in, n=10**5)
    


# #######################
# 4.5.15
# Объем файлов
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит суммарный объем файлов этого архива в сжатом и не сжатом видах в байтах,

# from zipfile import ZipFile

# def print_size_info(file_in):
#     with ZipFile(file_in, "r") as zf:
#         info = zf.infolist()
#     size_decompressed = sum(elem.file_size for elem in info)
#     size_compressed = sum(elem.compress_size for elem in info)
#     print("Объем исходных файлов:", size_decompressed, "байт(а)")
#     print("Объем сжатых файлов:", size_compressed, "байт(а)")

# if __name__ == "__main__":
#     file_in = 'etc/workbook.zip'
#     print_size_info(file_in)



# #######################
# 4.5.16
# Наилучший показатель
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит название файла из этого архива, который имеет наилучший показатель степени сжатия.

# from zipfile import ZipFile
# import os

# # best solution
# def print_best_compression1(file_in):
#     with ZipFile(file_in, "r") as zf:
#         info = zf.infolist()
#     best_k = 1
#     file_name = None
#     for elem in info:
#         k = elem.compress_size/elem.file_size if elem.file_size else 1
#         if k < best_k:
#             best_k = k
#             file_name = elem.filename
#     p = os.path.basename(file_name)
#     # print(os.path.basename(file_name))

# def print_best_compression2(file_in):
#     with ZipFile(file_in) as zip_file:
#         filelist = zip_file.infolist()
#         t = ((f.filename, f.compress_size/f.file_size) for f in filelist
#             if f.file_size != 0)
#         p = min(t, key=lambda x: x[1])[0].split("/")[-1]
#         # print(min(t, key=lambda x: x[1])[0].split("/")[-1])

# def print_best_compression2(file_in):
#     with ZipFile(file_in) as zip_file:
#         info = [i for i in zip_file.infolist() if not i.is_dir()]
#         p = min(info,key=lambda x:(x.compress_size/x.file_size)*100).filename.split('/')[-1]
#         # print(min(info,key=lambda x:(x.compress_size/x.file_size)*100).filename.split('/')[-1])


# from pathlib import Path
# import zipfile
# def print_best_compression3(file_in):
#     def get_coeff(zipped_file: zipfile.ZipInfo) -> float:
#         return zipped_file.compress_size / zipped_file.file_size
#     with zipfile.ZipFile(file_in) as zf:
#         p = Path(min(filter(lambda x: not x.is_dir(), zf.infolist()), key=get_coeff).filename).name
#         # print(Path(min(filter(lambda x: not x.is_dir(), zf.infolist()), key=get_coeff).filename).name)


# def execution_time(func, *args, n=100000):
#     from time import monotonic
#     t0 = monotonic()
#     for _ in range(n):
#         func(*args)
#     t1 = monotonic()
#     print(f"{func.__name__:<20} {t1-t0:.2f}")

# if __name__ == "__main__":
#     file_in = "etc/workbook.zip"
#     # print_best_compression(file_in)


#     funcs = [print_best_compression1, print_best_compression2, print_best_compression3]
#     for func in funcs[::-1]:
#         execution_time(func, file_in)



# #######################
# 4.5.17
# Избранные
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия файлов из этого архива, которые были созданы или изменены позднее 2021-11-30 14:22:00. Названия файлов должны быть расположены в лексикографическом порядке, каждое на отдельной строке.

# from zipfile import ZipFile
# import os

# def print_files_after(file_in, the_date=(2021, 11, 30, 14, 22, 0)):
#     with ZipFile(file_in, "r") as zf:
#         info = zf.infolist()
#     print(*sorted([os.path.basename(elem.filename) for elem in info if not elem.is_dir() and elem.date_time > the_date]), sep="\n")

# if __name__ == "__main__":
#     file_in = "etc/workbook.zip"
#     print_files_after(file_in)



# #######################
# 4.5.18
# Форматированный вывод
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия всех файлов из этого архива в лексикографическом порядке, указывая для каждого его дату изменения, а также объем до и после сжатия

# from zipfile import ZipFile
# import os

# def print_zip(file_in):
#     with ZipFile(file_in, "r") as zf:
#         info = zf.infolist()
#     for elem in sorted([f for f in info if not f.is_dir()], key=lambda x: os.path.basename(x.filename)):
#         print(os.path.basename(elem.filename))
#         print(f"  Дата модификации файла: {elem.date_time[0]:04d}-{elem.date_time[1]:02d}-{elem.date_time[2]:02d} {elem.date_time[3]:02d}:{elem.date_time[4]:02d}:{elem.date_time[5]:02d}")
#         print(f"  Объем исходного файла: {elem.file_size} байт(а)")
#         print(f"  Объем сжатого файла: {elem.compress_size} байт(а)")
#         print()

# if __name__ == "__main__":
#     file_in = "etc/workbook.zip"
#     print_zip(file_in)



# #######################
# 4.5.19
# Вам доступен набор различных файлов, названия которых представлены в списке file_names. Дополните приведенный ниже код, чтобы он создал архив files.zip и добавил в него все файлы из данного списка.

# from zipfile import ZipFile

# def write_zip(file_out, files_list):
#     with ZipFile(file_out, "w") as zf:
#         for f in files_list:
#             zf.write(f)

# if __name__ == "__main__":
#     zip_file = "files.zip"
#     file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
#     write_zip(zip_file, file_names)



# #######################
# 4.5.20
# Вам доступен набор различных файлов, названия которых представлены в списке file_names. Также вам доступен архив files.zip. Дополните приведенный ниже код, чтобы он добавил в архив files.zip только те файлы из списка file_names, объем которых не превышает 100 байт.

# from os.path import getsize
# from zipfile import ZipFile

# def add_to_zip1(zip_file, files_list):
#     with ZipFile(zip_file, "a") as zf:
#         for f in files_list:
#             if getsize(f) <= 100:
#                 zf.write(f)


# def calc_file_size(file_name):
#     with open(file_name, "r+b") as f:
#         f.seek(0, 2)
#         return f.tell()

# def add_to_zip2(zip_file, files_list):
#     with ZipFile(zip_file, "a") as zf:
#         for f in files_list:
#             if calc_file_size(f) <= 100:
#                 zf.write(f)

# if __name__ == "__main__":
#     zip_file = "files.zip"
#     file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
#     add_to_zip2(zip_file, file_names)



# #######################
# 4.5.21
# Функция extract_this()
# Реализуйте функцию extract_this(), которая принимает один или более аргументов в следующем порядке:
# zip_name — название zip архива, например, data.zip
# *args — переменное количество позиционных аргументов, каждый из которых является названием некоторого файла
# Функция должна извлекать файлы *args из архива zip_name в папку с программой. Если в функцию не передано ни одного названия файла для извлечения, то функция должна извлечь все файлы из архива.

# from zipfile import ZipFile

# def extract_this(zip_name, *f_names):
#     with ZipFile(zip_name, "r") as zf:
#         if f_names:
#             for f in f_names:
#                 zf.extract(f)
#         else:
#             zf.extractall()

# if __name__ == "__main__":
#     # extract_this('workbook.zip', 'earth.jpg', 'exam.txt')
#     extract_this('workbook.zip')



# #######################
# 4.5.22
# Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов, каждый из которых содержит информацию о каком-либо футболисте
# Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов, выступающих за футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен, а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.
# Обратите внимание, что наличие у файла расширения .json не гарантирует, что он является корректным текстовым файлом в формате JSON.

from zipfile import ZipFile
import json

def print_team1(file_zip, the_team="Arsenal", the_keys={"first_name", "last_name", "team", "position"}):
    players = []
    with ZipFile(file_zip, "r") as zf:
        for f in zf.infolist():
            if f.filename.endswith(".json"):
                with zf.open(f) as f_json:
                    try:
                        data = json.loads(f_json.read().decode("utf-8"))
                        if data.keys() == the_keys:
                            if data["team"] == the_team:
                                players.append((data["first_name"], data["last_name"]))
                    except:
                        continue
    # for name, s_name in sorted(players, key=lambda x: (x[0], x[1])):
    #     print(name, s_name)
    a = [f"{name} {s_name}" for name, s_name in sorted(players, key=lambda x: (x[0], x[1]))]
    return a


def print_team2(file_zip, the_team="Arsenal", the_keys={"first_name", "last_name", "team", "position"}):
    players = []
    with ZipFile(file_zip, "r") as zf:
        for f in zf.infolist():
            if f.filename.endswith(".json"):
                with zf.open(f) as f_json:
                    try:
                        data = json.loads(f_json.read().decode("utf-8"))
                        if data.keys() == the_keys and data["team"] == the_team:
                            players.append((data["first_name"], data["last_name"]))
                    except:
                        continue
    # for name, s_name in sorted(players, key=lambda x: (x[0], x[1])):
    #     print(name, s_name)
    a = [f"{name} {s_name}" for name, s_name in sorted(players, key=lambda x: (x[0], x[1]))]
    return a


def print_team3(file_zip, the_team="Arsenal", the_keys={"first_name", "last_name", "team", "position"}):
    def jsloads(z, n):
        try:
            with z.open(n) as f:
                return json.loads(f.read().decode('utf-8'))
        except:
            return {'team': ''}

    with ZipFile(file_zip) as z:
        names = [n for n in z.namelist() if n[-5:] == '.json']
        n = {i['first_name'] + ' ' + i['last_name'] for n in names for i in [jsloads(z, n)] if i['team'] == 'Arsenal'}
        # print(*sorted(n), sep='\n')	
        a = sorted(n)
        return a


from time import monotonic
def execution_time(func, *args, n=1000):
    t0 = monotonic()
    for _ in range(n):
        func(*args)
    t1 = monotonic()
    print(f"{func.__name__:<20} {t1-t0:.2f}")


if __name__ == "__main__":
    file_zip = "etc/data.zip"
    # print(print_team3(file_zip))
    funcs = [print_team1, print_team2, print_team3]
    for func in funcs:
        execution_time(func, file_zip)


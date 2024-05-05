# #######################
# 4.5.14
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

from zipfile import ZipFile
import os

# best solution
def print_best_compression1(file_in):
    with ZipFile(file_in, "r") as zf:
        info = zf.infolist()
    best_k = 1
    file_name = None
    for elem in info:
        k = elem.compress_size/elem.file_size if elem.file_size else 1
        if k < best_k:
            best_k = k
            file_name = elem.filename
    p = os.path.basename(file_name)
    # print(os.path.basename(file_name))

def print_best_compression2(file_in):
    with ZipFile(file_in) as zip_file:
        filelist = zip_file.infolist()
        t = ((f.filename, f.compress_size/f.file_size) for f in filelist
            if f.file_size != 0)
        p = min(t, key=lambda x: x[1])[0].split("/")[-1]
        # print(min(t, key=lambda x: x[1])[0].split("/")[-1])

def print_best_compression2(file_in):
    with ZipFile(file_in) as zip_file:
        info = [i for i in zip_file.infolist() if not i.is_dir()]
        p = min(info,key=lambda x:(x.compress_size/x.file_size)*100).filename.split('/')[-1]
        # print(min(info,key=lambda x:(x.compress_size/x.file_size)*100).filename.split('/')[-1])


from pathlib import Path
import zipfile
def print_best_compression3(file_in):
    def get_coeff(zipped_file: zipfile.ZipInfo) -> float:
        return zipped_file.compress_size / zipped_file.file_size
    with zipfile.ZipFile(file_in) as zf:
        p = Path(min(filter(lambda x: not x.is_dir(), zf.infolist()), key=get_coeff).filename).name
        # print(Path(min(filter(lambda x: not x.is_dir(), zf.infolist()), key=get_coeff).filename).name)


def execution_time(func, *args, n=100000):
    from time import monotonic
    t0 = monotonic()
    for _ in range(n):
        func(*args)
    t1 = monotonic()
    print(f"{func.__name__:<20} {t1-t0:.2f}")

if __name__ == "__main__":
    file_in = "etc/workbook.zip"
    # print_best_compression(file_in)


    funcs = [print_best_compression1, print_best_compression2, print_best_compression3]
    for func in funcs[::-1]:
        execution_time(func, file_in)

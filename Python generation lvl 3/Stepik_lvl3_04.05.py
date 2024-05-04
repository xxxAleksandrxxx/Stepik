# #######################
# 4.5.14
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит единственное число — количество файлов в этом архиве.
from zipfile import ZipFile

def count_files1(file_in):
    with ZipFile(file_in, 'r') as zf:
        info = zf.namelist()
    count = 0
    for elem in info:
        if elem.endswith("/"):
            continue
        else:
            count += 1
    # print(count)


def count_files2(file_in):
    with ZipFile(file_in, 'r') as zf:
        a = sum(not elem.is_dir() for elem in zf.infolist())
        # print(a)


def count_files3(file_in):
    with ZipFile(file_in, 'r') as zf:
        count = 0
        for elem in zf.infolist():
            if not elem.is_dir():
                count += 1
    # print(count)


def execution_time(func, *args, n=10000):
    from time import monotonic
    t0 = monotonic()
    for _ in range(n):
        func(*args)
    t1 = monotonic()
    print(f"{func.__name__:<15} {t1-t0:.2f}")

if __name__ == "__main__":
    file_in = "etc/workbook.zip"
    # count_files2(file_in)

    funcs = [count_files1, count_files2, count_files3]
    for func in funcs:
        execution_time(func, file_in, n=10**5)
    


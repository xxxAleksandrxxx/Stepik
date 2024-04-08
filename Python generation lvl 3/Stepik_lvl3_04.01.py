# import sys

# # for line in sys.stdin:
# #     print(line.strip('\n'))

# # data = sys.stdin.readlines()
# # print("Data:")
# # print(data)

# # data = sys.stdin.read()
# # print("Data:")
# # print(data)
# # print("type:", type(data))


# sys.stdout.write("1")
# sys.stdout.write("2")



#######################
# 4.1.10
# Обратный порядок
# Напишите программу, которая принимает произвольное количество строк и в каждой введенной строке располагает все символы в обратном порядке.
# Формат входных данных
# На вход программе подается произвольное количество строк.
# Формат выходных данных
# Программа должна вывести все введенные строки, предварительно расположив в каждой строке все символы в обратном порядке.

import sys
def print_reversed_input():
    data = [line.strip() for line in sys.stdin]
    for line in data:
        print(line[::-1])

if __name__ == "__main__":
    print_reversed_input()
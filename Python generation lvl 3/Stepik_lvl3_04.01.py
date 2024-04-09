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

# import sys
# def print_reversed_input():
#     data = [line.strip() for line in sys.stdin]
#     for line in data:
#         print(line[::-1])

# if __name__ == "__main__":
#     print_reversed_input()



#######################
# 4.1.11
# Размах данных
# Дана последовательность дат. Напишите программу, которая выводит 
# количество дней между максимальной и минимальной датами данной 
# последовательности.
# Формат входных данных
# На вход программе подается произвольное количество строк, в каждой 
# строке записана дата в ISO формате (YYYY-MM-DD).
# Формат выходных данных
# Программа должна вывести единственное число — количество дней между 
# максимальной и минимальной датами введенной последовательности.

# from datetime import datetime
# import sys

# def dif_days(fmt="%Y-%m-%d"):
#     # data = [datetime.strptime(line.strip(), fmt) for line in sys.stdin]
#     data_min = datetime(9999, 12, 31)
#     data_max = datetime(1, 1, 1)
#     for line in sys.stdin:
#         line_date = datetime.strptime(line.strip(), fmt)
#         if line_date < data_min:
#             data_min = line_date
#         if line_date > data_max:
#             data_max = line_date
#     delta = (data_max - data_min).days
#     return delta


# if __name__ == "__main__":
#     a = dif_days()
#     print(a)



#######################
# 4.1.12
# Лемма о трёх носках
# Анри и Дима, имея на руках ящик с бесконечным количеством носков, 
# решили сыграть в игру. Ребята по очереди достают из ящика произвольное 
# количество носков, и после неопределенного числа ходов игра заканчивается. 
# Если тот, кто сделал последний ход, вытащил четное количество носков — он 
# побеждает, в противном случае проигрывает.
# Напишите программу, которая определяет победителя в данной игре, если 
# первый ход делает Анри.

# import sys

# def three_socks_game():
#     '''
#     anri - players[0]
#     dima - players[1]
#     '''
#     players = {
#         0: {"name": "Анри", "value": 0},
#         1: {"name": "Дима", "value": 0}
#     }
#     i = -1
#     for line in sys.stdin:
#         i = (i + 1)%2
#         players[i]["value"] = int(line.strip())
#     if players[i]["value"]%2 == 0:
#         return players[i]["name"]
#     else:
#         return players[(i + 1)%2]["name"]


# def three_socks_game2(rolls:list=sys.stdin):
#     '''
#     anri - players[0]
#     dima - players[1]
#     '''
#     players = {
#         0: {"name": "Анри", "value": 0},
#         1: {"name": "Дима", "value": 0}
#     }
#     i = -1
#     for line in rolls:
#         i = (i + 1)%2
#         players[i]["value"] = int(line.strip())
#     if players[i]["value"]%2 == 0:
#         return players[i]["name"]
#     else:
#         return players[(i + 1)%2]["name"]
    

# def execution_time(func, arg):
#     import time
#     t_0 = time.monotonic()
#     for _ in range(100000):
#         func(arg)
#     t_1 = time.monotonic()
#     print(f"{func.__name__:<20} {t_1 - t_0:.2f}")



# def ex1(rolls):
#     s = tuple(int(i.strip()) for i in rolls)
#     return(('Дима', 'Анри')[(len(s) - 1) % 2 == s[-1] % 2])

# # the best!!!
# def ex2(rolls):
#     pl1, pl2 = 'Дима', 'Анри'
#     for num in rolls:
#         pl1, pl2 = pl2, pl1
#     return (pl1 if int(num) % 2 == 0 else pl2)



# if __name__ == "__main__":
#     r = ["1", "3", "5", "10", "3", "2", "12"]
#     funcs = [three_socks_game2, ex1, ex2]
#     for func in funcs:
#         execution_time(func, r)
#     # print(three_socks_game2(r))



######################
# 4.1.12
# Урок статистики
# Дан список чисел, каждое из которых — рост очередного ученика 
# онлайн-школы BEEGEEK. Напишите программу, которая определяет рост 
# самого низкого и самого высокого учеников, а также средний рост среди 
# всех учеников.

# import sys

# def stat(heights=sys.stdin):
#     '''
#     calc min, max and average height
#     input could be unlimited
#     '''
#     h_min = float('inf')
#     h_max = float(0)
#     h_count = 0
#     h_sum = 0
#     for height in heights:
#         h = height.strip()
#         if not h.isdigit():
#             h = 0
#         else:
#             # h = int(h)  # works slowly then float(h)
#             h = float(h)
#         if h < h_min:
#             h_min = h
#         if h > h_max:
#             h_max = h
#         h_count += 1
#         h_sum += h
#     if h_count > 0:
#         return h_min, h_max, h_sum/h_count
#     else:
#         return None, None, None 
    

# def stat2(h):
#     numbers = [int(i) for i in h]
#     try:
#         return [
#             f'Рост самого низкого ученика: {min(numbers)}',
#             f'Рост самого высокого ученика: {max(numbers)}',
#             f'Средний рост: {sum(numbers)//len(numbers)}'
#         ]
#     except:
#         return 'нет учеников'


# def stat3(h):
#     a = [int(i.strip()) for i in h]
#     return(f'Рост самого низкого ученика: {min(a)}\nРост самого высокого ученика: {max(a)}\nСредний рост: {sum(a)/len(a)}' if a else 'нет учеников')



# import sys, math
# def stat4(h):


#     min_val, max_val, acc, count = math.inf, 0, 0, 0
#     for line in h:
#         height = int(line)
#         if height < min_val:
#             min_val = height
#         if height > max_val:
#             max_val = height
#         acc += height
#         count += 1
#     if count == 0:
#         return ('нет учеников')
#     else:
#         return [
#             f'Рост самого низкого ученика: {min_val}',
#             f'Рост самого высокого ученика: {max_val}',
#             f'Средний рост: {acc / count}'
#         ]



# def execution_time(func, arg, n):
#     import time
#     t0 = time.monotonic()
#     for _ in range(n):
#         func(arg)
#     t1 = time.monotonic()
#     print(f"{func.__name__:<20} {t1 - t0:.2f}")



# if __name__ == "__main__":
#     h_min, h_max, h_avg = stat()
#     if h_min == None:
#         print("нет учеников")
#     else:
#         print("Рост самого низкого ученика:", h_min)
#         print("Рост самого высокого ученика:", h_max)
#         print("Средний рост:", h_avg)

#     h = ["185", "170", "190", "155", "175"]
#     funcs = [stat, stat2, stat3, stat4]
#     for func in funcs:
#         execution_time(func, h, 1000000)




######################
# 4.1.14
# Комментатор
# Дан блок кода на языке Python. Напишите программу, которая определяет 
# количество строк в данном коде, которые содержат в себе только 
# комментарии. Если в строке помимо комментария имеется что-то еще, то 
# такую строку учитывать не нужно.
# Формат входных данных
# На вход программе подается произвольное количество строк, в 
# совокупности представляющих блок кода на языке Python.
# Формат выходных данных
# Программа должна вывести единственное число — количество строк в 
# введенном коде, которые содержат в себе только комментарии.

import sys

def count_comments(the_code=sys.stdin):
    comment_counter = 0
    for line in the_code:
        if line.strip().startswith("#"):
            comment_counter += 1
    return comment_counter

# if __name__ == "__main__":
    # print(count_comments())


def count_comments2(the_code=sys.stdin):
    return sum(line.lstrip().startswith('#') for line in the_code)



def execution_time(func, arg, n):
    import time
    t0 = time.monotonic()
    for _ in range(n):
        func(arg)
    t1 = time.monotonic()
    print(f"{func.__name__:<18} {t1 - t0:.2f}")




if __name__ == "__main__":

    t = '''s = str(input())
k = 0
#подсчитываем количество цифр
for i in range(len(s)):
    #проверяем каждый символ
    if s[i] in '0123456789': #проверяем, является ли элемент строки цифрой
        k += 1
print(k)'''.split('\n')
    
    funcs = [count_comments, count_comments2]
    for f in funcs:
        execution_time(f, t, 10000000)
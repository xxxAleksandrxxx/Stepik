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

# import sys

# def count_comments(the_code=sys.stdin):
#     comment_counter = 0
#     for line in the_code:
#         if line.strip().startswith("#"):
#             comment_counter += 1
#     return comment_counter

# # if __name__ == "__main__":
#     # print(count_comments())


# def count_comments2(the_code=sys.stdin):
#     return sum(line.lstrip().startswith('#') for line in the_code)



# def execution_time(func, arg, n):
#     import time
#     t0 = time.monotonic()
#     for _ in range(n):
#         func(arg)
#     t1 = time.monotonic()
#     print(f"{func.__name__:<18} {t1 - t0:.2f}")




# if __name__ == "__main__":

#     t = '''s = str(input())
# k = 0
# #подсчитываем количество цифр
# for i in range(len(s)):
#     #проверяем каждый символ
#     if s[i] in '0123456789': #проверяем, является ли элемент строки цифрой
#         k += 1
# print(k)'''.split('\n')
    
#     funcs = [count_comments, count_comments2]
#     for f in funcs:
#         execution_time(f, t, 10000000)




######################
# 4.1.15
# Без комментариев
# Дан блок кода на языке Python. Напишите программу, которая удаляет 
# все строки в данном коде, которые содержат в себе только комментарии. 
# Если в строке помимо комментария имеется что-то еще, то такую строку 
# учитывать не нужно.
# Формат входных данных
# На вход программе подается произвольное количество строк, в 
# совокупности представляющих блок кода на языке Python.
# Формат выходных данных
# Программа должна вывести введенный блок кода, предварительно удалив 
# из него все строки которые содержат в себе только комментарии.

# import sys

# def no_comments(the_code=sys.stdin):
#     return "\n".join([line for line in the_code if not line.strip().startswith("#")])

# if __name__ == "__main__":
#     t = '''digit = int(input())
# s = input()
# for i in s:
#     #комментирую потому что прикольно

#     if 97 > ord(i) - digit:
#         temp = ord(i) - digit + 26
#         print(chr(temp), end='')   #вывод
#     else:
#         #ахаха
#         temp = ord(i) - digit
#         print(chr(temp), end='')'''.split("\n")
#     print(no_comments(t))




######################
# 4.1.16
# Панорамное агентство
# По чатам одного немалоизвестного мессенджера начали появляться новости 
# сомнительного содержания. Оказалось, что некий молодежный клуб решил 
# подшутить, распространяя всякие глупости. Однако подобное хулиганство 
# мешает доверчивым людям, особенно пенсионного возраста, поэтому группа 
# независимых программистов решила разработать бота, который мог бы 
# оценить степень достоверности новости, а также отнести её к какой-либо 
# категории.
# Напишите программу, которая выводит все новости заданной категории, 
# располагая их по возрастанию степени достоверности.

# import sys

# def get_news1(the_news=sys.stdin):
#     data = []
#     for line in the_news:
#         if " / " in line:
#             data.append(line.strip().split(" / "))
#         else:
#             category = line.strip()
#     data_filtered = [n for n, c, _ in sorted(data, key=lambda x: (x[2], x[0])) if c == category]
#     return data_filtered


# # красивый способ сортировки!
# def get_news2(the_news=sys.stdin):
#     events, priority_tag = {}, None

#     for line in the_news:
#         line = line.strip().split(' / ')
#         if len(line) > 1:
#             event, tag, score = line
#             events.setdefault(tag, []).append((score, event))
#         else:
#             priority_tag = line[0]
#     result = []
#     for _, event in sorted(events[priority_tag]):
#         result.append(event)
#     return result



# def get_news3(the_news=sys.stdin):
#     news = [i.strip().split(' / ') for i in the_news]
#     filtered = filter(lambda x: x[1] == news[-1][0], news[:-1])

#     return (i[0] for i in sorted(filtered, key=lambda x: (float(x[2]), x[0])))


# def execution_time(func, arg, n):
#     import time
#     t0 = time.monotonic()
#     for _ in range(n):
#         func(arg)
#     t1 = time.monotonic()
#     print(f"{func.__name__:<18} {t1-t0:.2f}")

# # if __name__ == "__main__":
# #     for elem in get_news():
# #         print(elem)

# # test purpose 
# if __name__ == "__main__":
#     t = '''На рейсах Поражения второй пилот будет исполнять обязанности бортпроводника / Авиация / 0.3
# Огурец исключит из своих рядов членов, не проголосовавших за Единую Арстоцку на выборах / Политика / 0.8
# Орбистанские точки общепита будут закрыты для вакцинированных граждан / Общество / 0.7
# Джорджи Костава получил членский билет Независимого Кобрастана / Политика / 0.0
# В Колечии повысят призывной возраст до 40 лет / Политика / 1.0
# Всем гражданам Антегрии въезд в Арстоцку запрещен / Политика / 0.8
# Политика'''.split("\n")
#     funcs = [get_news1, get_news2, get_news3]
#     for f in funcs:
#         execution_time(f, t, 1000000)
# #     for elem in get_news(t):
# #         print(elem)



######################
# 4.1.17
# Это точно Python?
# Дана последовательность дат. Напишите программу, которая определяет, в 
# каком порядке расположены даты в данной последовательности.
# Формат входных данных
# На вход программе подается произвольное количество строк (две или более), 
# в каждой строке записана дата в формате DD.MM.YYYY.
# Формат выходных данных
# Программа должны вывести текст:
# ASC, если даты в введенной последовательности расположены строго в порядке возрастания
# DESC, если даты в введенной последовательности расположены строго в порядке убывания
# MIX, если даты в введенной последовательности расположены ни в порядке возрастания, ни в порядке убывания

# import sys

# # my solution -  оказалось самым лучим! 
# def check_order1(the_dates=sys.stdin):
#     '''
#     input mostly from stdin but cold be a list of strings
#     date format DD.MM.YYYY
#     '''
#     # print("Func1")
#     flag_increase = True
#     flag_decrease = True
#     if type(the_dates) == list:
#         date_0 = the_dates[0]
#         the_dates = the_dates[1:]
#     else:
#         date_0 = the_dates.readline()
#     date_0 = date_0[6:10] + date_0[2:6] + date_0[:2]# YYYY.MM.DD
#     for elem in the_dates:
#         date_1 = elem[6:10] + elem[2:6] + elem[:2]  # YYYY.MM.DD
#         if date_1 > date_0:
#             flag_decrease = False
#         elif date_1 < date_0:
#             flag_increase = False
#         elif date_1 == date_0:
#             flag_increase = False
#             flag_decrease = False
#             break
#         date_0 = date_1
#     if flag_increase == True and flag_decrease == False:
#         return "ASC"
#     elif flag_increase == False and flag_decrease == True:
#         return "DESC"
#     else:
#         return "MIX"
    

# # other learners 
# from datetime import datetime
# def check_order2(the_dates=sys.stdin):
#     # print("Func2")
#     is_asc = is_desc = True
#     dates = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in the_dates]
#     for prev_date, cur_date in zip(dates[:-1], dates[1:]):
#         if prev_date >= cur_date and is_asc:
#             is_asc = False
#         if prev_date <= cur_date and is_desc:
#             is_desc = False
#     if is_asc:
#         return 'ASC'
#     elif is_desc:
#         return 'DESC'
#     else:
#         return 'MIX'


# # other learners 
# def check_order3(the_dates=sys.stdin):
#     # print("Func3")
#     dates = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in the_dates]
#     if sorted(list(set(dates))) == dates:
#         return('ASC')
#     elif sorted(list(set(dates)), reverse=True) == dates:
#         return('DESC')
#     else:
#         return('MIX')


# # other learners 
# from collections import deque
# def check_order4(the_dates=sys.stdin):
#     # print("Func4")
#     dq, record = deque(maxlen=2), set()
#     for dt in the_dates:
#         dq.append(datetime.strptime(dt.strip(), '%d.%m.%Y'))
#         if len(dq) != 2:
#             continue
#         if dq[0] < dq[1]:
#             record.add('ASC')
#         elif dq[0] > dq[1]:
#             record.add('DESC')
#         else:
#             record.add('')
#         if len(record) == 2:
#             return('MIX')
#             break

#     else:
#         return(record)


# def execution_time(func, arg, n):
#     import time
#     t0 = time.monotonic()
#     for _ in range(n):
#         func(arg)
#     t1 = time.monotonic()
#     print(f"{func.__name__:<18} {t1-t0:.2f}")


# # if __name__ == "__main__":
# #     d = '''14.06.2022
# # 20.06.2022
# # 21.06.2022
# # 17.01.2031
# # 18.11.2031
# # 19.11.2031
# # 23.11.2031
# # 01.01.2033
# # 01.11.2043
# # 05.07.2051
# # 05.07.2051'''.split('\n')
# #     print(check_order1(d))



# if __name__ == "__main__":
#     funcs = [check_order1, check_order2, check_order3, check_order4]
#     d = '''14.06.2022
# 20.06.2022
# 21.06.2022
# 17.01.2031
# 18.11.2031
# 19.11.2031
# 23.11.2031
# 01.01.2033
# 01.11.2043
# 05.07.2051
# 05.07.2051'''.split('\n')
#     for f in funcs:
#         execution_time(f, d, 100000)





######################
# 4.1.18
# Гуру прогрессий
# Дана последовательность целых чисел. Напишите программу, которая 
# определяет, является ли данная последовательность прогрессией, и 
# если да, то определяет её вид.
# Формат входных данных
# На вход программе подается произвольное количество строк (не менее 
# трёх), в каждой строке записано натуральное число — очередной член 
# последовательности.
# Формат выходных данных
# Программа должна вывести текст:
# Арифметическая прогрессия, если введенная последовательность чисел является арифметической прогрессией
# Геометрическая прогрессия, если введенная последовательность чисел является геометрической прогрессией
# Не прогрессия, если введенная последовательность чисел не является прогрессией

# import sys

# def check_sequence(the_numbers=sys.stdin):
#     flag_aryth = True
#     flag_geom = True

#     num_0 = float(sys.stdin.readline().strip())
#     num_1 = float(sys.stdin.readline().strip())
#     d_aryth = num_1 - num_0
#     q_geom = num_1 / num_0
#     # aryth = num_1 + d_aryth
#     # geom = num_1 * q_geom
#     aryth = num_1
#     geom = num_1

#     # print("num_0", num_0)
#     # print("num_1", num_1)
#     # print("d_aryth", d_aryth)
#     # print("q_geom", q_geom)
#     # print("aryth", aryth)
#     # print("geom", geom)

#     for elem in sys.stdin:
#         num = float(elem.strip())

#         # print("in loop: num=", num)

#         if num != aryth + d_aryth:
#             flag_aryth = False
#         if num != geom * q_geom:
#             flag_geom = False
#         if flag_aryth:
#             aryth += d_aryth
#         if flag_geom:
#             geom *= q_geom
        
#         # print("in loop: flag_aryth=", flag_aryth)
#         # print("in loop: flag_geom=", flag_geom)

#         if flag_aryth == False and flag_geom == False:
#             break
#         # aryth += d_aryth
#         # geom *= q_geom

#         # print("in loop: aryth=", aryth)
#         # print("in loop: geom=", geom)
#         # print()

#     if not flag_aryth and not flag_geom:
#         return "Не прогрессия"
#     elif flag_aryth:
#         return "Арифметическая прогрессия"
#     else:
#         return "Геометрическая прогрессия"


# # if __name__ == "__main__":
# #     print(check_sequence())


# # for testing




# #___________
# def is_arithmetic_progression(seq: list) -> bool:
#     for i in range(1, len(seq)-1):
#         if seq[i-1] + seq[i+1] != 2 * seq[i]:
#             return False
#     return True

# def is_geometric_progression(seq: list) -> bool:
#     for i in range(1, len(seq)-1):
#         if seq[i-1] * seq[i+1] != seq[i] ** 2:
#             return False
#     return True

# def check_sequence2():
#     numbers = list(map(int, sys.stdin))
#     if is_arithmetic_progression(numbers):
#         return "Арифметическая прогрессия"
#     elif is_geometric_progression(numbers):
#         return "Геометрическая прогрессия"
#     else:
#         return "Не прогрессия"
# #___________
    


# #___________
# def check_sequence2():
#     n1, n2 = [int(sys.stdin.readline()) for _ in range(2)]

#     for num in sys.stdin:
#         if ((int(num) - n2) != (n2 - n1)) and (int(num) / n2) != (n2 / n1):
#             result = 'Не прогрессия'
#             break
#         elif int(num) - n2 == n2 - n1:
#             result = 'Арифметическая прогрессия'
#             n1, n2 = n2, int(num)
#         elif int(num) / n2 == n2 / n1:
#             result = 'Геометрическая прогрессия'
#             n1, n2 = n2, int(num)
#     return (result)
# #___________


# #___________
# def check_sequence3():
#     from sys import stdin

#     nums = [int(n) for n in stdin]
#     nums1 = map(lambda a, b: b - a, nums, nums[1:])
#     nums2 = map(lambda a, b: b / a, nums, nums[1:])

#     if len(set(nums1)) == 1:
#         return ('Арифметическая прогрессия')
#     elif len(set(nums2)) == 1:
#         return ('Геометрическая прогрессия')
#     else:
#         return ('Не прогрессия')    
# #___________


# #___________
# def check_sequence4():
#     current_number = multr = summr = None

#     for new_num in sys.stdin:
#         new_num = int(new_num)
        
#         if current_number is None:
#             current_number = new_num
#             continue
#         if new_num <= current_number:
#             return('Не прогрессия')
#             break
#         if multr is None:
#             multr = new_num / current_number
#             summr = new_num - current_number
#             current_number = new_num
#             continue
        
#         if summr and new_num - current_number != summr:
#             summr = False
#         if multr and new_num / current_number != multr:
#             multr = False
#         if multr == summr == False:
#             return('Не прогрессия')
#             break

#         current_number = new_num

#     else:
#         return('Арифметическая' if summr else 'Геометрическая', 'прогрессия')



# # Run tests 
# def execution_time(func, arg, n):
#     import time
#     from io import StringIO
#     t0 = time.monotonic()
#     for _ in range(n):
#         input_io = StringIO(arg)
#         sys.stdin = input_io
#         result = func()
#     t1 = time.monotonic()
#     print(f"{func.__name__:<20} {t1 - t0:.2f}   result: {result}")



# if __name__ == "__main__":
#     # from io import StringIO  # to take control of sys.stdin and send to it test data

#     test_data = '''15
# 30
# 60
# 120
# 240
# 480
# 960
# 1920
# '''
   
#     # input_io = StringIO(test_data)
#     # sys.stdin = input_io
#     funcs = [check_sequence, check_sequence2, check_sequence3, check_sequence4]
#     for f in funcs:
#         execution_time(f, test_data, 1000000)



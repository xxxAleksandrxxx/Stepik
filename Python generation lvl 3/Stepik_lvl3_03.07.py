##########################################
##########################################
# 3.7
# import calendar, locale
# def print_week_days():
#     for day in calendar.day_name:
#         print(day.title(), end=" ")
#     print()

# locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
# print_week_days()

# locale.setlocale(locale.LC_ALL, "")
# print_week_days()

# import calendar
# d_list = [day.upper() for day in calendar.day_name]
# print(*d_list)
# d_num_list = [getattr(calendar, day) for day in d_list]
# print(*d_num_list)


# import calendar
# print(*calendar.monthcalendar(2024, 4), sep="\n")


# import calendar
# print(calendar.month(2024, 4))


# import calendar
# print(calendar.calendar(2024))


##########################################
# 3.7.7
# Напишите программу, которая определяет, является ли год високосным.
# import calendar

# def check_year(year_range):
#     for year in year_range:
#         print(calendar.isleap(year))

# if __name__ == "__main__":
#     y = [1999, 2000, 2001, 2002]
#     check_year(y)

# import calendar

# def check_year(year_range):
#     for year in year_range:
#         print(calendar.isleap(year))

# if __name__ == "__main__":
#     y = [int(input()) for _ in range(int(input()))]
#     check_year(y)



##########################################
# 3.7.8
# Напишите программу, которая выводит календарь на заданные год и месяц.
# import calendar

# def print_calendar_month(y_m:str):
#     y, m = y_m.split(' ')
#     month_dict = {m: i for i, m in enumerate(calendar.month_abbr)}
#     print(calendar.month(int(y), month_dict[m]))

# if __name__ == "__main__":
#     print_calendar_month(input())



##########################################
# 3.7.9
# День недели
# Напишите программу, которая определяет день недели, соответствующий заданной дате.

# import calendar, time
# def week_day(the_date:str, fmt="%Y-%m-%d"):
#     the_date = time.strptime(the_date, fmt)
#     week_days = {i: d_name for i, d_name in enumerate(calendar.day_name)}
#     return week_days[calendar.weekday(the_date.tm_year, the_date.tm_mon, the_date.tm_mday)]

# if __name__ == "__main__":
#     the_date = input()
#     print(week_day(the_date))



##########################################
# 3.7.10
# Количество дней
# Напишите программу, которая определяет количество дней в заданном месяце.

# import calendar

# def days_in_month(y_m:str):
#     y, m = map(int, y_m.split(' '))
#     return calendar.monthrange(y, m)[1]

# if __name__ == "__main__":
#     print(days_in_month(input()))



##########################################
# 3.7.11
# Количество дней
# Напишите программу, которая определяет количество дней в заданном месяце.
# Формат входных данных
# На вход программе подаются год и полное название месяца на английском, разделенные пробелом.

# import calendar

# def days_in_month(y_m:str):
#     y, m = y_m.split(' ')
#     m_names = {m: i for i, m in enumerate(calendar.month_name)}
#     return calendar.monthrange(int(y), m_names[m])[1]

# if __name__ == "__main__":
#     print(days_in_month(input()))





##########################################
# 3.7.12
# Функция get_days_in_month()   
# Реализуйте функцию get_days_in_month(), которая принимает два 
# аргумента в следующем порядке:
# year — натуральное число
# month — полное название месяца на английском
# Функция должна возвращать отсортированный по возрастанию список 
# всех дат (тип date) месяца month и года year.

# import calendar
# from datetime import date

# def get_days_in_month(y:int, m:str):
#     m_digit = list(calendar.month_name).index(m)
#     date_max = calendar.monthrange(y, m_digit)[1]
#     return [date(y, m_digit, i) for i in range(1, date_max+1)]

# if __name__ == "__main__":
#     for elem in get_days_in_month(2021, "December"):
#         print(elem)




##########################################
# 3.7.13
# Функция get_all_mondays()
# Реализуйте функцию get_all_mondays(), которая принимает один аргумент:
# year — натуральное число
# Функция должна возвращать отсортированный по возрастанию список всех 
# дат (тип date) года year, выпадающих на понедельник.

# from datetime import date
# import calendar
# def get_all_mondays(the_year):
#     '''
#     check all the dates in the given year and return sorted list
#     of Monday dates
#     '''
#     date_list = [date(the_year, m, d) for m in range(1, 13) for d in range(1, calendar.monthrange(the_year, m)[1] + 1) if calendar.weekday(the_year, m, d) == 0]
#     return date_list


# def get_all_mondays2(year):
#     mondays = []
#     for month in range(1, 13):
#         for week in calendar.monthcalendar(year, month):
#             monday = week[0]
#             if monday:
#                 mondays.append(date(year, month, monday))
#     return mondays


# from datetime import timedelta, date
# def get_all_mondays3(y):
#     weekday1 = date(y, 1, 1).weekday()
#     if weekday1 != 0:
#         monday_date = date(y, 1, 8 -  weekday1)
#     else:
#         monday_date = date(y, 1, 1)
#     mondays = list()
#     while monday_date.year == y:
#         mondays.append(monday_date)
#         monday_date += timedelta(days=7)
#     return mondays
    

# def get_all_mondays4(y):
#     weekday1 = date(y, 1, 1).weekday()
#     if weekday1 != 0:
#         monday_date = date(y, 1, 8 -  weekday1)
#     else:
#         monday_date = date(y, 1, 1)
#     mondays = [monday_date + timedelta(days=i) for i in range(0, 367, 7) if (monday_date + timedelta(days=i)).year == y]
#     return mondays



# def execution_time(func, arg):
#     import time
#     t_start = time.monotonic()
#     for _ in range(10000):
#         func(arg)
#     t_end = time.monotonic()
#     print(f"{func.__name__:<18} {t_end - t_start:.2f}")


# if __name__ == "__main__":
#     the_year = 2024

#     # f1 = get_all_mondays(the_year)
#     # f2 = get_all_mondays2(the_year)
#     # f3 = get_all_mondays3(the_year)
#     # f4 = get_all_mondays4(the_year)
#     # print("f1 == f2:", f1 == f2)
#     # print("f1 == f3:", f1 == f3)
#     # print("f1 == f4:", f1 == f4)

#     for func in [get_all_mondays, get_all_mondays2, get_all_mondays3, get_all_mondays4]:
#         execution_time(func, the_year)

# # print(len([date(the_year, m, d) for m in range(1, 13) for d in range(1, calendar.monthrange(the_year, m)[1] + 1)]



##########################################
# 3.7.14
# ТЧМ
# Во многих музеях существует один день месяца, когда посещение музея 
# для всех лиц или отдельных категорий граждан происходит без взимания 
# платы. Например, в Эрмитаже это третий четверг месяца.
# Напишите программу, которая определяет даты бесплатных дней посещения 
# Эрмитажа в заданном году.

import calendar

def third_thursdays(the_year):
    import calendar
    from datetime import date
    third_thursdays_list = []
    for i in range(1, 13):
        thursday_1 = calendar.monthcalendar(the_year, i)[0][3]
        if thursday_1 == 0:
            thursday_3 = calendar.monthcalendar(the_year, i)[3][3]
        else:
            thursday_3 = calendar.monthcalendar(the_year, i)[2][3]
        # third_thursdays_list.append(f"{thursday_3}.{str(i).zfill(2)}.{the_year}")
        # third_thursdays_list.append(f"{thursday_3}.{i}.{the_year}")
        third_thursdays_list.append(date(the_year, i, thursday_3))
    return third_thursdays_list


def third_thursdays2(the_year):
    import calendar
    from datetime import datetime
    free_days = []
    year = the_year
    for i in range(1, 13):
        c = calendar.monthcalendar(year, i)
        first_week = c[0]
        third_week = c[2]
        fourth_week = c[3]
        if first_week[calendar.THURSDAY]:
            free_day = third_week[calendar.THURSDAY]
        else:
            free_day = fourth_week[calendar.THURSDAY]
        free_days.append(datetime(year, i, free_day))
    return free_days


def third_thursdays3(the_year):
    from calendar import weekday, THURSDAY
    from datetime import datetime

    year = the_year
    free_days = []
    for month in range(1, 13):
        for day in range(15, 22):
            if weekday(year, month, day) == THURSDAY:
                thursday = datetime(year, month, day)
                free_days.append(thursday.strftime('%d.%m.%Y'))
                break
    return 


def execution_time(func, arg):
    import time
    t_start = time.monotonic()
    for _ in range(10000):
        func(arg)
    t_end = time.monotonic()
    print(f"{func.__name__:<18}: {t_end - t_start:.2f}")


if __name__ == "__main__":
    # for elem in third_thursdays(int(input())):
    #     print(elem)
    funcs = [third_thursdays, third_thursdays2, third_thursdays3]
    for func in funcs:
        execution_time(func, 2024)
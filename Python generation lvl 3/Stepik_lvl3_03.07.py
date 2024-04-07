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
import calendar

def print_calendar_month(y_m:str):
    y, m = y_m.split(' ')
    month_dict = {m: i for i, m in enumerate(calendar.month_abbr)}
    print(calendar.month(int(y), month_dict[m]))

if __name__ == "__main__":
    print_calendar_month(input())
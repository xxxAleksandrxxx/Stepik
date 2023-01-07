#%% 16.1.15

"""Письмо для экзамена

Напишите функцию generate_letter(), которая будет собирать электронное письмо в соответствии с шаблоном:

To: <mail>
Приветствую, <name>!
Вам назначен экзамен, который пройдет <date>, в <time>.
По адресу: <place>. 
Экзамен будет проводить <teacher> в кабинете <number>. 
Желаем удачи на экзамене!
Функция должна получать на вход пять обязательных аргументов mail, name, date, time, place и два необязательных teacher, number и возвращать текст готового письма. При отсутствии аргумента teacher учителем будет Тимур Гуев, а если нет аргумента number, то кабинет будет 17.

Примечание 1. Следующий программный код:

print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 
                      'Часова 23, корпус 2', 'Василь Ярошевич', 23))
должен выводить:

To: lara@yandex.ru
Приветствую, Лариса!
Вам назначен экзамен, который пройдет 10 декабря, в 12:00.
По адресу: Часова 23, корпус 2. 
Экзамен будет проводить Тимур Гуев в кабинете 17. 
Желаем удачи на экзамене!

To: lara@yandex.ru
Приветствую, Лариса!
Вам назначен экзамен, который пройдет 10 декабря, в 12:00.
По адресу: Часова 23, корпус 2. 
Экзамен будет проводить Василь Ярошевич в кабинете 23. 
Желаем удачи на экзамене!"""

def generate_letter(mail, 
                    name, 
                    date, 
                    time, 
                    place, 
                    teacher='Тимур Гуев', 
                    number=17):
    return f'''To: {mail}
Приветствую, {name}!
Вам назначен экзамен, который пройдет {date}, в {time}.
По адресу: {place}. 
Экзамен будет проводить {teacher} в кабинете {number}. 
Желаем удачи на экзамене!'''

print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 
                      'Часова 23, корпус 2', 'Василь Ярошевич', 23))


#%% 16.1.16 - Печать таблицы / таблица

"""Pretty print

Напишите функцию pretty_print(), которая выводит содержимое списка с рамкой. 

Функция должна получать на вход один обязательный аргумент data – список, который следует вывести и два необязательных строковых односимвольных  аргумента side и delimiter и выводить содержимое списка в соответствии с примерами.

В случае если отсутствует аргумент side, то полагаем side='-', а если отсутствует аргумент delimiter, то полагаем delimiter='|'."""

def pretty_print(data, side='-', delimiter='|'):
    horizon_line = ' ' + side*(2 + 4*(len(data)-1)) + side*(sum(map(lambda x: len(str(x)), data)) - (len(data) - 1))
    print(horizon_line)
    for elem in data:
        print(delimiter, elem, end=' ')
    print(delimiter)
    print(horizon_line)

# pretty_print([10000, 100, 100, '12'])
pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


#%% 16.1.16 v2 - Печать таблицы / таблица
def pretty_print(data, side='-', delimiter='|'):
    st = f'{delimiter} ' +\
         f' {delimiter} '.join(map(str, data)) +\
         f' {delimiter}'
    horizon_line = f' {side*(len(st) - 2)}'
    print(horizon_line)
    print(st)
    print(horizon_line)

pretty_print([10, 1])
pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


#%% 16.3.1

"""Напишите функцию concat(), принимающую переменное количество аргументов и объединяющую их в одну строку через разделитель (sep). Если разделитель не задан, им служит пробел.

Примечание 1. Обратите внимание, что функция concat() должна принимать не список, а именно переменное количество аргументов."""

def concat(*arg, sep=' '):
    answer = ''
    for elem in arg:
        answer += str(elem) + sep
    return answer[:-len(sep)]

print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))
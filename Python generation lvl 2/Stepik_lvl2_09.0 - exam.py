#%%
# 9.1.14 
'''
Наполните множество set1 содержимым так, чтобы программа вывела {'p'}.
set1 = {...}
set2 = {'a', 't', 'f'}
'''
'''
set1 = {'a', 't', 'f', 'p'}
set2 = {'a', 't', 'f'}

print(set1 - set2)
'''

#%%
# 9.2.2 
'''
Домашнее задание

Учитель проверяет домашнее задание в классе и получил следующие ответы: из n школьников у m домашнее задание съела собака, у k отключили свет, а p учеников постигли оба несчастья. Напишите программу, которая определяет сколько человек выполнило домашнее задание.

Формат входных данных
На вход программе подаются числа n,m,k,p, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести количество учеников, сделавших домашнее задание.'''
'''
n = int(input())
m = int(input())
k = int(input())
p = int(input())

print(n-m-k+p)
'''


# 9.2.3 Восход
'''
На спутнике «Восход» установлен прибор для измерения солнечной активности. Каждую минуту он передаёт в обсерваторию по каналу связи положительное целое число — количество энергии солнечного излучения. Для правильного анализа результатов нет необходимости держать повторяющиеся данные. Напишите программу, которая выводит максимальное количество показаний спутника, при удалении которых результат будет правильно проанализирован.

Формат входных данных
На вход программе подаётся одна строка, содержащая числа – показания спутника «Восход». Числа указываются через пробел и не содержат ведущих нулей.

Формат выходных данных
Программа должна вывести максимальное количество показаний, после удаления которых анализ результатов будет произведен верно.
'''
'''
t1 = '10 20 30 10 40'
t2 = '1 2 3 4 5 6 7 8 9 1 2 3'
t = list(input().split())
print(len(t) - len(set(t)))
'''


# 9.2.3 Города
'''
Тимур и Руслан играют в игру города. Они очень любят эту игру и знают много городов, особенно Тимур, однако к концу игры ввиду своего возраста забывают, какие города уже называли.

Напишите программу, считывающую информацию об игре и сообщающую ребятам, что очередной город назван повторно.

Формат входных данных
На вход программе в первой строке подаётся натуральное число n – количество названных городов, в последующих n строках вводятся названные города и ещё одна строка с новым, только что названым городом.

Формат выходных данных
Программа должна вывести OK, если этот город ещё не вспоминали, и REPEAT, если город уже был назван.
'''
'''
# v1
n = int(input())
s = set()
for _ in range(n):
    s.add(input())
if input() not in s:
    print('OK')
else:
    print('REPEAT')
'''
'''
# v2
c = {input() for _ in range(int(input()))}
print(('OK', 'REPEAT')[input() in c])
'''


# 9.2.4 Книги на прочтение
'''
Руслан получил в конце учебного года список литературы на лето. Теперь ему надо выяснить, какие книги из этого списка у него есть. У Руслана на компьютере в текстовом файле записаны все книги из его домашней библиотеки в случайном порядке.

Напишите программу, определяющую для каждой книги из списка на прочтение, есть она у Руслана или нет.

Формат входных данных
На вход программе в первой строке подается натуральное число m — количество книг в домашней библиотеке Руслана. Во второй строке записано натуральное число n —  количество книг в списке на лето. Далее идут m строк с названиями книг из домашней библиотеки и n строк названий из списка на лето.

Формат выходных данных
Программа должна вывести n строк, в каждой из которых написано слово YES, если книга найдена в библиотеке, и NO, если нет.
'''

'''
#m,n = [int(input()) for _ in range('mn')]
m = int(input())
n = int(input())


library = {input() for _ in range(m)}
for _ in range(n):
    if input() in library:
        print('YES')
    else:
        print('NO')
'''


# 9.2.5 Странное увлечение
'''
Как известно, математики странные люди. Не составляет исключения и Тимур — автор данного курса. Каждый день Тимур решает ровно две сложные математические задачи. Решая первую задачу, он записывает на первом листочке все числа, которые в ней встречаются. Далее он делает паузу и берется за вторую задачу. Затем записывает на втором листочке все числа, которые в ней встречаются. После этого он берет еще один листок и выписывает на него все совпадающие числа из первых двух листочков. Если такие числа есть, день удался, если общих чисел нет, Тимур считает день неудачным.

Напишите программу, которая находит общие числа двух листочков или сообщает, что день не удался 😏

Формат входных данных
На вход программе подаются две строки с числами: в первой строке числа с первого листочка, во второй со второго.

Формат выходных данных
Программа должна вывести числа, встретившиеся на обоих листках в отсортированном по убыванию порядке, либо словосочетание BAD DAY, если таких чисел нет.
'''
'''
s1, s2 = [set(int(i) for i in input().split()) for _ in range(2)]
if s1.isdisjoint(s2):
    print('BAD DAY')
else:
    print(*sorted(s1&s2, reverse=True))
'''


# 9.2.6 Онлайн-школа BEEGEEK 1
'''
При приёме новых сотрудников в онлайн-школу BEEGEEK её руководитель тестирует не только профессиональные качества кандидата, но и его память.

Кандидату показывают ненадолго несколько различных чисел, а затем кандидат должен их назвать. Причем неважно, в каком порядке он их вспоминает, и повторяется он или нет, главное он должен назвать все числа, не добавляя лишних.

Напишите программу, определяющую, успешно ли прошел кандидат тестирование памяти.

Формат входных данных
На вход программе подаются две строки с числами: в первой строке показанные кандидату, а во второй ответы кандидата.

Формат выходных данных
Программа должна вывести YES, если кандидат прошел испытание и его можно брать на работу и NO в противном случае.
'''
'''
q, a = [{int(i) for i in input().split()} for _ in 'qa']
print(('NO', 'YES')[q==a])
'''


# 9.2.7 Онлайн-школа BEEGEEK 2
'''
Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба эти предмета. У руководителя школы есть списки изучающих каждый предмет.

Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только математику.

Формат входных данных
На вход программе в первых двух строках подаются числа m и n – количества учеников, изучающих математику и информатику соответственно. Далее идут m строк — фамилии учеников, которые изучают математику и n строк с фамилиями учеников, изучающих информатику.

Формат выходных данных
Программа должна вывести количество учеников, которые изучают только математику.

Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.
'''
'''
m, n = [int(input()) for _ in range(2)]
math = {input() for _ in range(m)}
info = {input() for _ in range(n)}
print(len(math - info))
'''


# 9.2.8 Онлайн-школа BEEGEEK 3
'''
Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета. У руководителя школы есть списки изучающих каждый предмет.

Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только один предмет.

Формат входных данных
На вход программе в первых двух строках подаются числа m и n – количества учеников, изучающих математику и информатику соответственно. Далее идут m строк — фамилии учеников, которые изучают математику и n строк с фамилиями учеников, изучающих информатику.

Формат выходных данных
Программа должна вывести количество учеников, которые изучают только один предмет. Если таких учеников не окажется, то необходимо вывести NO.

Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.
'''
'''
# v1
m, n = [int(input()) for _ in range(2)]
math = {input() for _ in range(m)}
info = {input() for _ in range(n)}
if math == info:
    print('NO')
else:
    print(len(math - info) + len(info - math))
'''
'''
# v2
m, n = [int(input()) for _ in range(2)]
math = {input() for _ in range(m)}
info = {input() for _ in range(n)}
print(len(math^info) or 'NO')
'''


# 9.2.9 Онлайн-школа BEEGEEK 4
'''
Руководитель онлайн-школы BEEGEEK и его помощник составили списки учеников их школы.

Напишите программу, которая выведет все фамилии учеников, которые вспомнили руководитель и его помощник.

Формат входных данных
На вход программе в первой строке подаются фамилии, записанные руководителем школы, а на второй строке - помощником руководителя. Фамилии указываются через пробел.

Формат выходных данных
Программа должна вывести все фамилии учеников, отсортированных в лексикографическом порядке, записанные руководителем и его помощником.

Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.
'''
'''
s = set(input().split())|set(input().split())
print(*sorted(s))
'''


# 9.2.10 Онлайн-школа BEEGEEK 5 🌶️
'''
Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета. У руководителя школы есть списки учеников, изучающих каждый предмет. Случайно списки всех учеников перемешались.

Напишите программу, которая позволит руководителю выяснить, сколько учеников изучает только один предмет.

Формат входных данных
На вход программе в первых двух строках подаются числа m и n – количества учеников, изучающих математику и информатику соответственно. Далее идут m+n строк — фамилии учеников, изучающих математику и информатику, в произвольном порядке.

Формат выходных данных
Программа должна вывести количество учеников, которые изучают только один предмет. Если таких учеников не окажется, то необходимо вывести NO.

Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.
'''
'''
m,n = [int(input()) for _ in range(2)]
s = {input() for _ in range(m+n)}

print(len(s)*2 - m - n or 'NO')
'''


# 9.2.11
'''
Онлайн-школа BEEGEEK 6 🌶️

Руководителю онлайн-школы BEEGEEK захотелось узнать, кто из его учеников присутствовал на всех уроках с начала учебного года. Для каждого урока есть листок со списком присутствовавших учеников.

Напишите программу, определяющую фамилии учеников, которые присутствовали на всех уроках.

Формат входных данных
На вход программе в первой строке дается число m – количество уроков, проведенных с начала учебного года. Далее идёт m блоков строк, описывающих листки с фамилиями. На первой строке каждого блока указано количество фамилий ni, затем идёт ni строчек с фамилиями тех, кто был на i-ом уроке.

Формат выходных данных
Программа должна вывести фамилии учеников, которые были на всех уроках, отсортированных в лексикографическом порядке. Каждая фамилия должна быть записана на отдельной строке.

Примечание 1. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

Примечание 2. Гарантируется, что хотя бы один ученик был на всех уроках.
'''
'''
m = int(input())
good_students = {input() for _ in range(int(input()))}
for _ in range(m-1):
    students = {input() for _ in range(int(input()))}
    good_students.intersection_update(students)

print(*sorted(good_students), sep='\n')
'''

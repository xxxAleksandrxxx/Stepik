#%% 18.1.1 - Количество строк в файле

"""На вход программе подается строка текста с именем текстового файла. Напишите программу для вывода на экран количества строк данного файла.

Формат входных данных
На вход программе подается строка текста, содержащая имя существующего текстового файла.

Формат выходных данных
Программа должна вывести количество строк файла.

Примечание. Считайте, что исполняемая программа и указанный файл находятся в одной папке."""
with open(input(), 'r', encoding='utf-8') as f:
    print(len(f.readlines()))


#%% 18.1.2 - Суммарная стоимость

"""Вам доступен текстовый файл ledger.txt с данными о продажах фирмы за месяц. На каждой строке файла указано, сколько клиент заплатил за товар, в долларах (целое число):

$47
$100
$60
$12
$8
...
Напишите программу для подсчета суммарной месячной выручки фирмы. 

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести выручку фирмы (сумму всех чисел из файла) в соответствии с примером ниже.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке."""
file = r'/Users/zwar/Downloads/ledger.txt'
# file = 'ledger.txt'
with open(file, 'r', encoding='utf-8') as f:
    print('$', sum(map(lambda x: int(x[1:-1]) if x[-1] == '\n' else int(x[1:]), f.readlines())), sep ='')


#%% 18.1.3 - Goooood students

"""Вам доступен текстовый файл grades.txt, содержащий оценки студента за три теста в каждом из триместров. Строки файла имеют вид: фамилия оценка_1 оценка_2 оценка_3.

Напишите программу для подсчета количества студентов, сдавших все три теста. Тест считается сданным, если количество баллов по нему не меньше 65.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести количество студентов, сдавших все три теста.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке."""
# 18.1.3 v1
file = r'/Users/zwar/Downloads/grades.txt'
# file = 'grades.txt'
with open(file, 'r', encoding='utf-8') as f:
    count = 0
    for student in f:
        name, t1, t2, t3 = student.strip().split()
        if int(t1) >= 65 and int(t2)>= 65 and int(t3)>= 65:
            count += 1
print(count)
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
file = r'/Users/xxXXXxx/Downloads/ledger.txt'
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
file = r'/Users/xxXXXxx/Downloads/grades.txt'
# file = 'grades.txt'
with open(file, 'r', encoding='utf-8') as f:
    count = 0
    for student in f:
        name, t1, t2, t3 = student.strip().split()
        if int(t1) >= 65 and int(t2)>= 65 and int(t3)>= 65:
            count += 1
print(count)

#%% 18.1.3 v2
file = r'/Users/xxXXXxx/Downloads/grades.txt'
# file = 'grades.txt'
with open(file, 'r', encoding='utf-8') as f:
#    print(sum(1 for i in f.readlines()))
   print(sum(1 for i in f.readlines() if all([int(j)>=65 for j in i.split()[1:]])))

#%% 18.1.3 v3 - красивое решение с перебором индекса в lambda. жаль, сам не додумался до такого.
file = r'/Users/xxXXXxx/Downloads/grades.txt'
# file = 'grades.txt'

with open(file, 'r', encoding='utf-8') as f:
    print(len(list(filter(lambda x: all(int(x[i]) >= 65 for i in (1, 2, 3)), (map(str.split, f))))))


#%% 18.1.4 - Самое длинное слово в файле

"""Вам доступен текстовый файл words.txt со словами, разделенными пробелом. Напишите программу, которая находит и выводит самые длинные слова этого файла, не меняя порядка их следования.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести самые длинные слова файла words.txt, каждое с новой строки, не меняя их порядка следования.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Словом считайте любую группу символов без пробелов, даже если она включает цифры или знаки препинания."""
# 18.1.4 v1 через подсчет длинны
file = r'/Users/xxXXXxx/Downloads/words.txt'
# file = 'words.txt'
with open(file, 'r', encoding='utf-8') as f:
    longest_len = 0
    answer = []
    for word in f.read().strip().split():
        word_len = len(word)
        if word_len > longest_len:
            longest_len = word_len
            answer = [word]
        elif word_len == longest_len:
            answer.append(word)
print(*answer, sep='\n')

#%% 18.1.4 v2 через словарь из длин слов
file = r'/Users/xxXXXxx/Downloads/words.txt'
# file = 'words.txt'
with open(file, 'r', encoding='utf-8') as f:
    answer = dict()
    for word in f.read().strip().split():
        answer.setdefault(len(word), []).append(word)

print(*answer[max(answer)], sep='\n')



#%% 18.1.5 - Tail of a File

"""На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран последние 10 строк данного файла.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.

Формат выходных данных
Программа должна вывести последние 10 строк этого файла.

Примечание 1. Считайте, что исполняемая программа и файл находятся в одной папке.

Примечание 2. Если количество строк в файле меньше 10, необходимо вывести содержимое файла полностью.
Примечание 4. Подумайте над ситуацией, когда файл очень большой и нерационально считывать все его содержимое в память компьютера."""
file = r'/Users/xxXXXxx/Downloads/grades.txt'
# file = r'/Users/xxXXXxx/Downloads/ledger.txt'

# file = input()
with open(file, 'rb') as f:
    pos = 0
    f.seek(pos, 2)
    count = 1
    answer = ''
    # ищем 10-ю строку снизу подсчитывая '\n'
    while count <11 and f.tell() != 1:
        pos -= 1
        f.seek(pos, 2) # перемещаемся в позицию pos, 2 - от конца файла
        a = f.read(1).decode('utf-8')
        answer += a
        if a == '\n':
            count += 1

print(answer[::-1])

print('strok', count)


#%%
file = r'/Users/xxXXXxx/Downloads/grades.txt'
# file = r'/Users/xxXXXxx/Downloads/ledger.txt'
# file = input()

with open(file, 'r') as f:
    print(*f.readlines()[-10:], sep='')



#%% 18.1.6 - Forbidden words 🌶️

"""На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран содержимое этого файла, но с заменой всех запрещенных слов звездочками * (количество звездочек равно количеству букв в слове).

Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Гарантируется, что все слова в этом файле записаны в нижнем регистре.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла, в котором необходимо заменить запрещенные слова звездочками.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание 1. Ваша программа должна заменить запрещенные слова, где бы они ни встречались, даже если они встречаются в середине другого слова.

Примечание 2. Программа должна заменять запрещенные слова независимо от их регистра. Например, если файл forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и подобные должны быть заменены на ****."""

# почему-то не принимает решение, хотя вроде работает на тестовых файлах..

forbiden_f = r'/Users/xxXXXxx/Downloads/forbidden_words.txt'
file1 =  r'/Users/xxXXXxx/Downloads/data.txt'
file2 = r'/Users/xxXXXxx/Downloads/stepik.txt'
file3 = r'/Users/xxXXXxx/Downloads/beegeek.txt'

file = file2

# forbiden_f = 'forbidden_words.txt'
# file = input()

with open(forbiden_f, 'r', encoding='utf-8') as f: 
    forbiden_w = f.read().split()

with open(file, 'r+', encoding='utf-8') as f:#,\
    #open(r'/Users/xxXXXxx/Downloads/TTT.txt', 'w+', encoding='utf-8') as f2:
    content = [row.strip().split() for row in f.readlines()]
    for r in range(len(content)):
        for w in range(len(content[r])):
            for word in forbiden_w:
                if word in content[r][w].lower():
                    pos = content[r][w].lower().find(word)
                    new_w = [leter for leter in content[r][w]]
                    for _ in range(len(word)):
                        new_w.pop(pos)
                    new_w.insert(pos, '*'*len(word))
                    new_w = ''.join(new_w)
                    print()
                    print('old word', content[r][w])
                    print('forbiden', word)
                    print('new     ', new_w)
                    content[r][w] = new_w
    for r in range(len(content)):
        print(' '.join(content[r]))        
        # print(' '.join(content[r]), file=f2)

#%% 18.1.6 v2

forbiden_f = r'/Users/xxXXXxx/Downloads/forbidden_words.txt'
file1 =  r'/Users/xxXXXxx/Downloads/data.txt'
file2 = r'/Users/xxXXXxx/Downloads/stepik.txt'
file3 = r'/Users/xxXXXxx/Downloads/beegeek.txt'

file = file2

# forbiden_f = 'forbidden_words.txt'
# file = input()

with open(forbiden_f, 'r', encoding='utf-8') as f: 
    forbiden_w = f.read().split()

with open(file, 'r+', encoding='utf-8') as f:
    content = f.read()
    content_l = content.lower()
    for w in forbiden_w:
        if w in content_l:
            content_l = content_l.replace(w, '*'*len(w))

for i in range(len(content)):
    if content_l[i] != '*':
        print(content[i], end='')
    else:
        print(content_l[i], end='')


#%% 18.1.7 - Транслитерация 🌶️

"""Транслитерация — передача знаков одной письменности знаками другой письменности, при которой каждый знак (или последовательность знаков) одной системы письма передаётся соответствующим знаком (или последовательностью знаков) другой системы письма.

Вам доступен текстовый файл cyrillic.txt, содержащий текст. Напишите программу для транслитерации этого файла, то есть замены кириллических символов на латинские в соответствии с предложенной таблицей. Все остальные символы надо оставить без изменений. Результат транслитерации требуется записать в файл transliteration.txt."""

file = r'/Users/xxXXXxx/Downloads/cyrillic.txt'
result_file =  r'/Users/xxXXXxx/Downloads/transliteration.txt'

# file = 'cyrillic.txt'
# result_file =  'transliteration.txt'

translit = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je', 'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya', 'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch', 'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya',
    }

with open(file, 'r', encoding='utf-8') as f:
    text = f.read()

for i in range(len(text)):
    if text[i] in translit:
        text = text.replace(text[i], translit[text[i]])

with open(result_file, 'w+', encoding='utf-8') as f:
    f.write(text)



#%% 18.1.8 - Пропущенные комменты 🌶️

"""При написании собственных функций рекомендуется в комментарии описывать назначение функции, ее параметры и возвращаемое значение. Часто программисты откладывают написание таких комментариев напоследок, а потом и вовсе забывают о них 😂.

На вход программе подается строка текста с именем текстового файла, в котором написан код на языке Python. Напишите программу, выводящую на экран имена всех функций для которых отсутствует поясняющий комментарий. Будем считать, что любая строка, начинающаяся со слова def и пробела, является началом определения функции. Функция содержит комментарий, если первый символ предыдущей строки - #.

Формат входных данных
На вход программе подается строка текста, содержащая имя существующего текстового файла с кодом на языке Python.

Формат выходных данных
Программа должна вывести названия всех функций (не меняя порядка их следования в исходном файле), каждое на отдельной строке, для которых отсутствует поясняющий комментарий. Если все функции в файле имеют поясняющий комментарий, то следует вывести: Best Programming Team."""

file = r'/Users/xxXXXxx/Downloads/test_file_with_functions.txt'

# file = input()
st1, st2 = '', ''
flag = True
with open(file, 'r', encoding='utf-8') as f:
    for row in f:
        st1 = st2
        st2 = row
        if st2.startswith('def '):
            if not st1.startswith('#'):
                print(st2.split()[1][:st2.split()[1].find('(')])
                flag = False
if flag:
    print('Best Programming Team')


#%% 18.1.8 v2
file = r'/Users/xxXXXxx/Downloads/test_file_with_functions.txt'

# file = input()
st = ''
flag = True
with open(file, 'r', encoding='utf-8') as f:
    for row in f:
        if row.startswith('def '):
            if not st.startswith('#'):
                print(row[4:row.find('(')])
                flag = False
        st = row
if flag:
    print('Best Programming Team')
'''
###
Иногда нужно создать вложенный список, заполненный по
определенному правилу – шаблону. Например, список длиной n,
содержащий списки длиной m, каждый из которых заполнен нулями.

Рассмотрим несколько способов решения задачи.
'''
n = 3
m = 2
###version 1
### пустой список заполняется списком длины m из нулей
##l = list()
##for _ in range(n):
##    l.append([0]*m)
##print(l)

###version 2
### создаем список из n заполненный нулями. Каждый элемент списка
### делаем ссылкой на другой список из m элементов, заполненных 0
##l = [0]*n
##for i in range(n):
##    l[i] = [0]*m
##print(l)

### version 3 - предпочтительный
### через генератор списка: список из n элементов, каждый из
### которых - список из m нулей
##l = [[0]*m for _ in range(n)]
##print(l)



'''
###
Считываение списков
Если элементы списка вводятся через клавиатуру (каждая строка
на отдельной строке, всего n строк, числа в строке разделяются
пробелами), для ввода списка можно использовать следующий код:
'''
### количество строк (элементов)
##my_list = []
##for _ in range(n):
##    # создаем список из элементов строки
##    elem = [int(i) for i in input().split()]
##    my_list.append(elem)

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in l:
    for j in i:
        print(j, end = ' ')
    print()

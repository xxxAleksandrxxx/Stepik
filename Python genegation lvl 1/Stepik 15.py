'''
бросаем игральный кубик, пока не ответят нет
'''
'''
from random import randint

def roll():
    return randint(1, 12)

def answer(text):
    answ = ''
    while answ not in ['y', 'n', 'д', 'н']:
        answ = input(text)
    return answ

answ = answer('бросить кубик? y/n\n')
while answ in ['y', 'д']:
    print('вы выбросили', roll())
    answ = answer('продолжить? y/n\n')
'''


'''
орел или решка
'''
'''
from random import choice

def coin():
    return choice(['орел', 'решка'])

count = 0
n = int(input("введите число бросков монеты\n"))
for _ in range(n):
    a = choice(['орел', 'решка'])
    if a == 'орел':
        count += 1
print("количество 'орлов'", count, count/n, "%")
print("количество 'решек'", n - count, (n-count)/n, "%")
'''

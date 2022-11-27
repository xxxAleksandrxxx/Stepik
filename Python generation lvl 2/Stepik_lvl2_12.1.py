# 12.1.1 
'''
#%%
import random
l = list()
for _ in range(100):
    l.append(random.randint(0, 100))

print(sorted(l))


#%%
import random
a = 0
b = 2.2
c = 1
l = list()
for _ in range(100):
    l.append(random.randrange(a, b))

print(sorted(l))

#%%
import random
l = list()
for _ in range(100):
    l.append(random.random())

print(sorted(l))

#%%
import random
l = list()
a = 0.9
b = 1
for _ in range(100000000):
    l.append(random.uniform(a, b))
    if l[-1] == b:
        print(l[-1])

#print(sorted(l))

# %%
l = list()
for i in range(1, 10):
    l.append(2**i - 1)
print(l)
'''
#%%
# 12.1.11
'''
Напишите программу, которая с помощью модуля random моделирует броски монеты. Программа принимает на вход количество попыток и выводит результаты бросков: Орел или Решка (каждое на отдельной строке).

Примечание. Например, при 
n
=
7
n=7 ваша программа может выводить:

Орел
Решка
Решка
'''
'''
import random

n = int(input())
for _ in range(n):
    print(('Орел', 'Решка')[random.random() > 0.5])
'''
'''
# v2
import random
coin = {1:'Орел', 2:'Решка'}
for _ in range(int(input())):
    print(coin[random.randint(1, 2)])
'''


#%%
# 12.1.12
'''
Напишите программу, которая с помощью модуля random моделирует броски игрального кубика c 
6
6 гранями. Программа принимает на вход количество попыток и выводит результаты бросков — выпавшее число, которое написано на грани кубика (каждое на отдельной строке).

Примечание. Например, при 
n
=
7
n=7 ваша программа может выводить:
5
5
6
6
2
6
2
'''
'''
# v1
import random
n = int(input())
for _ in range(n):
    print(random.randrange(1, 7))
'''
'''
# v2
import random
n = int(input())
for _ in range(n):
    print(random.randint(1, 6))
'''
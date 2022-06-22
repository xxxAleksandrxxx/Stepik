'''
st = input()
for i in range(0, len(st), 2):
    print(st[i])
'''
'''
st = input()
for i in range(len(st)-1, -1, -1):
    print(st[i])
'''
'''
st = input()
for i in range(len(st)):
    print(st[(len(st)-1-i)])
'''
'''
name, s_name, f_name = input(), input(), input()
print(name[0], s_name[0], f_name[0], sep = '')
'''
'''
number = int(input())
sum_n = 0
while number:
    sum_n += number % 10
    number //= 10
print(sum_n)
'''
'''
n = input()
sum_n = 0
for i in n:
    sum_n += int(i)
print(sum_n)
'''
'''
st = input()
numbers = '0123456789'
flag = False
for i in st:
    if i in numbers:
        flag = True
        break
if flag:
    print('Цифра')
else: print('Цифр нет')
'''
'''
st = input()
msg = 'Цифр нет'
for i in st:
    if i in '0123456789':
        msg = 'Цифра'
        break
print(msg)
'''
import time

st = input()
start = time.time()
count1, count2 = 0, 0
for i in st:
    if i == '+':
        count1 += 1
        #continue
    if i == '*':
        count2 += 1
print('Символ + встречается', count1, 'раз')
print('Символ * встречается', count2, 'раз')
end = time.time()
print('time:', end - start)

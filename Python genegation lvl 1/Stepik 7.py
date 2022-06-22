'''
n = int(input())
for i in range(n+1):
    print("Квадрат числа %s равен %s"%(i, i*i))
'''
'''
qty = int(input())
for i in range(qty, 0, -1):
    print("*"*i)
'''
'''
m = int(input())
p = 0.01*int(input())
n = int(input())
for i in range(1, n+1):
    print(i, m)
    m = m + m * p
'''
'''
m = int(input())
n = int(input())
if m < n:
    for i in range(m, n+1):
        print(i)

else:
    for i in range(m, n-1, -1):
        print(i)
'''
'''
m = int(input())
n = int(input())
if m > n:
    for i in range(m, n-1, -1):
        if i % 2 != 0:
            print(i)
'''
'''
m, n = int(input()), int(input())
for i in range(m - 1 + m % 2, n-1, -2):
    print(i)
'''
'''
m, n = int(input()), int(input())
for i in range(m, n+1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
       print(i) 
'''
'''
cat = '　　　　  　 ／＞　 フ' + '\n' + \
'　　  　　　| _　 _|' + '\n' + \
'　  　　　／`ミ _x彡' + '\n' + \
'　　 　 /　　　 　|' + '\n' + \
'　　　 /　ヽ　   ﾉ' + '\n' + \
'　／￣|　　|　| |' + '\n' + \
' | (￣ヽ＿_ヽ_)_)' + '\n' + \
'　＼二つ' + '\n'
print(cat)
'''
'''
total = 0
for i in range(1, 6):
    total += i
    print(total, end='')
'''
'''
a, b = int(input()), int(input())
qty = 0
for i in range(a, b+1):
    if i * i * i % 10 == 4 or i * i * i % 10 == 9:
        qty += 1
print(qty)
'''
'''
qty = 0
for i in range (int(input())):
    qty += int(input())
print(qty)          
'''
'''
from math import log
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += 1/i
sum = sum - log(n)
print('total', sum)
'''
'''
n = int(input())
sum = 0
for i in range(1, n+1):
    if str(i * i % 10) in "258":
        sum += i
print(sum)
'''
'''
payment = int(input())
coins = 0
while payment >= 25:
    payment -= 25
    coins += 1
while payment >= 10:
    payment -= 10
    coins += 1
while payment >= 5:
    payment -= 5
    coins += 1
while payment >= 1:
    payment -= 1
    coins += 1
print('coins: ', coins)
'''
'''
n = int(input())
while n != 0:
    last_digit = n % 10
    n = n // 10
    print('n: ', n, ' ', 'last_digit: ', last_digit)
'''
'''
n = int(input())
flag = False
count = 0
while n != 0:
    last_digit = n % 10
    if last_digit == 7:
        flag = True
        count += 1
    n = n // 10
if flag:
    print('В числе имеется цифра 7. потворяется ', count, ' раз')
else:
    print('Цифра 7 не обнаружена')
'''
'''
n = int(input())
if '7' in str(n):
    print('В числе имеется цифра 7')
else:
    print('Цифра 7 не обнаружена')
'''
'''
num = int(input())
while num != 0:
    print(num % 10)
    num = num // 10
'''
'''
num = int(input())
num_reverse = ''
while num != 0:
    num_reverse += str(num % 10)
    num = num // 10
print(num_reverse)
'''
'''
n, t = int(input()), ''
while n:                    #True = 1, False = 0. когда n = 0, результат проверки: False.
    t += str(n%10)
    n//=10
print(t)
'''
'''
n = int(input())
max_num, min_num = 0, 9
if n >= 10:
    while n:
        if n % 10 < min_num:
            min_num = n % 10
        if n % 10 > max_num:
            max_num = n % 10
        n //= 10
print('Максимальная цифра равна', max_num)
print('Минимальная цифра равна', min_num)
'''
'''
import time
start = time.time()
print(start)

for a in range(1, 151):
    a5 = a**5
    for b in range(a, 151):
        b5 = b**5
        for c in range(b, 151):
            c5 = c**5
            for d in range(c, 151):
                d5 = d**5
                for e in range(d, 151):
                    e5 = e**5
                    if a5 + b5 + c5 + d5 == e5:
                        print('a =', a,\
                              'b =', b,\
                              'c =', c,\
                              'd =', d,\
                              'e =', e,\
                              'a+b+c+d+e =', a+b+c+d+e)

end = time.time()
print('Итого: ', int(end - start), 'sec')
'''
'''
from time import time
start = time()

for a in range(1, 151):
    a5 = a**5
    for b in range(a, 151):
        b5 = b**5
        for c in range(b, 151):
            c5 = c**5
            for d in range(c, 151):
                d5 = d**5
                sum5 = a5 + b5 + c5 + d5
                e = int((sum5)**0.2)
                if e**5 == sum5:
                    print('a =', a,\
                          'b =', b,\
                          'c =', c,\
                          'd =', d,\
                          'e =', e)
                    print('sum =', a + b + c + d + e)
                    end1 = time()
                    print('end1 =', int(end1 - start),\
                          'sec')

end = time()
print('total time =', int(end - start), 'sec')
'''
'''
n = int(input())
output = ''
count = 0
for i in range(1, n+1):
        for j in range(i):
            count += 1
            output += str(count) + ' '
        output += '\n'
print(output)
'''
'''
n = int(input())
item_per_string = 0
count1 = 0
count2 = 0
flag = True
stroka = ''
while count2 < n+1 and flag:
    count1 += 1
    for _ in range(count1):
        count2 += 1
        stroka += str(count2) + ' '
        if count2 == n:
            flag = False
            break
    stroka += '\n'
print(stroka)
'''
'''
n = int(input())
count = 0
num = 0
end = 0
for _ in range(n):
    count += 1
    end = 2*count
    #print('count =', count, 'end = ', end)
    for i in range(1, end):
        num = count - abs(i - count)
        #print('num = count - abs(i - count) =',\
        #      count, ' - abs(', i, '- ', count, ') =', num)
        print(num, end = '')
    print()
'''      
'''
n = int(input())
count = 0
for _ in range(n):
    count += 1
    for i in range(1, 2*count):
        print(count - abs(i - count), end = '')
    print()
'''
'''
a = int(input())
b = int(input())
sum_delitel_max = 0
max_delitel = 0

for i in range(a, b+1):
    sum_delitel = 0
    for j in range(1, i+1):
        if i % j == 0:
            sum_delitel += j
            #print(i, '/', j, ' =', i/j, 'summa delit ',\
            #      sum_delitel)
    if sum_delitel >= sum_delitel_max:
        sum_delitel_max = sum_delitel
        max_delitel = i
        #print('max_delitel ', max_delitel, 'sum_delitel_max ', sum_delitel_max)
print(max_delitel, sum_delitel_max)
'''
'''
n = int(input())
for i in range(1, n+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    print(i, '+'*count, sep = '')
'''
'''
n = int(input())
while n // 10:
    n = n//10 + n % 10
print(n)
'''
'''
n = int(input())
i, j = 1, 1
output1 = 0
if n == 0:
    output1 = 1
else:
    for i in range(1, n+1):
        output2 = 1
        for j in range(1, i+1):
            output2 *= j
        output1 += output2
print(output1)
'''
'''
n = int(input())
if n == 0:
    sum_f = 1
else:
    f, sum_f = 1, 0
    for i in range(1, n+1):
        f *= i
        sum_f += f
print(sum_f)
'''
'''
a, b = int(input()), int(input())
if a >= b:
    print('error: "a" (', a,\
          ') have to be less than "b" (', b,\
          ')', sep = '')
else:
    prost = ''    
    for i in range(a, b+1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag and i != 1:
            prost += str(i) + '\n'
    print(prost)
'''
'''
n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)
'''
'''
n = 8
count = 0
maximum = -1000000000000
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
'''
'''
n = int(input())
out = '*' * 19 + '\n'
for _ in range(n-2):
    out += '*' + ' ' * 17 + '*' + '\n'
out += '*' * 19
print(out)
'''
'''
print(input()[2])
'''
'''
n = int(input())
while n // 100 > 0:
    out = n % 10
    n //= 10
print(out)
'''
'''
n = int(input())
count3 = 0
last = n % 10
count_chet = 0
count_last = 0
sum_5 = 0
mult_7 = 1
count_0_5 = 0
while n > 0:
    num = n % 10
    if num == 3:
        count3 += 1
    if num == last:
        count_last += 1
    if num % 2 == 0:
        count_chet += 1
    if num > 5:
        sum_5 += num
    if num > 7:
        mult_7 *= num
    if num == 0 or num == 5:
        count_0_5 += 1
    n //= 10
print(count3, count_last, count_chet,\
      sum_5, mult_7, count_0_5, sep = '\n')
'''
'''
for i in range (1, 6):
    for j in range(1, 6):
        print(i, '**3 + ', j, '**3 = ', i**3+j**3, sep = '')
'''
'''
count = 0
k = 1720
while count < 6:
    k += 1
    count_2 = 0
    for i in range(1, k+1):
        i_qube = i**3
        for j in range(i, k+1):
            j_qube = j**3
            if k == i_qube + j_qube:
                count_2 += 1
                if count_2 == 2:
                    count += 1
                    print('count_2: k =', k) 
                    #print(k, '=', i_qube,\
                    # '+', j_qube)
'''
'''
n = 50000
for i in range(1, n + 1):
	count = 0
	for x in range(1, int(i**(1/3)) + 1):
		for y in range(x, int(i**(1/3)) + 1):
			if x**3 + y**3 == i:
				count += 1
			elif x**3 + y**3 > i:
				break
	if count >= 2:
		print(i)
'''
'''
for a in range(1, 41):
    for c in range(1, a):
        for d in range(1, c+1):
            for b in range(1, d):
                if a**3 + b**3 == d**3 + c**3:
                    print(a**3+b**3)
'''
from datetime import datetime

start = datetime.now()

for a in range(1, 41):
    for c in range(1, a):
        for d in range(1, c+1):
            for b in range(1, d):
                if a**3 + b**3 == d**3 + c**3:
                    print(a**3+b**3)
end = datetime.now()
print('calculation time:', end - start) 

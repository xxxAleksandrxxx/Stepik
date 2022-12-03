#%%
if 0.1+0.1+0.1 == 0.3:
    print('YES')
else:
    print('NO')

#%%
import decimal

a = 10
b = decimal.Decimal(a)
print(a, type(a))
print(b, type(b))
 
#%%
import decimal

a = 0.1
b = decimal.Decimal(a)
print(type(a), a, sep='\n')
print()
print(type(b), b, sep='\n')

#%%
from decimal import Decimal
a = '123.456789000'
b = Decimal(a)
print(a, type(a))
print(b, type(b))

#%%
# встроенные функции, выводящие Decimal
from decimal import Decimal

a = Decimal('12.2')

print(a, type(a))
print(a.exp(), type(a.exp()))
print(a.sqrt(), type(a.sqrt()))
print(a.ln(), type(a.ln()))
print(a.log10(), type(a.log10()))

#%%
# а сколько знаков после запятой?
b = a.sqrt()
print()
print('b', b)
print(len(str(b).split('.')[1]))

#%%
# детализация вывода - as_tuple()
import decimal

a = decimal.Decimal('123.05')
b = a.as_tuple()
print(a, type(a))
print(b, type(b))
print('sign:    ', type(b.sign), b.sign)
print('digits:  ', type(b.digits), b.digits)
print('exponent:', type(b.exponent), b.exponent)

#%%
# Работа с контекстом decimal

import decimal

decimal.getcontext()

a = decimal.Decimal('31.1428')

decimal.getcontext().prec = 3
print(a)
print(a*1)

#%%
# 13.1.10
'''
Decimal числа, разделенные символом пробела, хранятся в строковой переменной s. Дополните приведенный код, чтобы он вывел сумму наибольшего и наименьшего Decimal числа.
s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
'''
from decimal import Decimal
s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
s_dec = [Decimal(number) for number in s.split()]
print(min(s_dec)+max(s_dec))

#%%
# 3.1.11
'''
Decimal числа, разделенные символом пробела, хранятся в строковой переменной s. Дополните приведенный код, чтобы он вывел на первой строке сумму всех чисел, а на второй строке 5 самых больших чисел в порядке убывания, разделенных символом пробела.
s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
'''
from decimal import Decimal
s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
s_dec = [Decimal(number) for number in s.split()]
print(sum(s_dec))
print(*sorted(s_dec, reverse=True)[:5])
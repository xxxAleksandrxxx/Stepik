'''
BOH
На вход программе подается натуральное число в десятичной системе счисления. Напишите программу, которая переводит его в двоичную, восьмеричную и шестнадцатеричную системы счисления.
Формат входных данных 
На вход программе подается натуральное число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание 1. Используйте встроенные функции bin(), oct(), hex().
Примечание 2. Для шестнадцатеричной системы счисления используйте заглавные буквы A, B, C, D, E, F.
Примечание 3. BOH = Binary, Octal, Hex.
'''

'''
#BOH - lasy
num = int(input())
print(bin(num)[2:])
print(oct(num)[2:])
print(format(num, 'X'))
'''

'''
#BOH - normal
num = int(input())
print(bin(num)[2:])
print(oct(num)[2:])
print(hex(num)[2:].upper())
'''


#BOH - custom
def dec_to_any(num, base):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:base - 10]
    num = int(num)
    answer = ''
    rest = base - 1
    while num > rest:
        count = num % base
        if count > 9:
            answer += alphabet[count - 10]
        else:
            answer += str(num % base)
        num //= base
    if num > 9:
        answer += alphabet[num - 10]
    else:
        answer += str(num)
    return answer[::-1]

number = input()
print(dec_to_any(number, 2))
print(dec_to_any(number, 8))
print(dec_to_any(number, 16))

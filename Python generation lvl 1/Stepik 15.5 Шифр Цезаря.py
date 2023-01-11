'''
Описание проекта: требуется написать программу, способную шифровать и
дешифровать текст в соответствии с алгоритмом Цезаря. Она должна
запрашивать у пользователя следующие данные:

направление: шифрование или дешифрование;
язык алфавита: русский или английский;
шаг сдвига (со сдвигом вправо).

Примечание 1. Считайте, что в русском языке 32 буквы
(буква ё отсутствует).

Примечание 2. Неалфавитные символы — знаки препинания,
пробелы, цифры — не меняются.

Примечание 3. Сохраните регистр символов. Например, текст:
"Умом Россию не понять" при сдвиге на одну позицию вправо
будет преобразован в: "Фнпн Спттйя ож рпоауэ".
'''
# Ввод int
def input_int(text):
    numbers = '-0123456789'
    flag_is_num = False
    answer = input(text + ' ')
    while flag_is_num == False:
        flag_is_num = True
        if answer[0] in numbers: # первый символ может быть цифра или минус
            for i in answer[1:]: # второй и последующие символы только цифры
                flag_is_num = True
                if i not in numbers[1:]:
                    flag_is_num = False
                    break
        else:
            flag_is_num = False
        if flag_is_num == False:
            answer = input('Это не целое число. Попробуйте ещё раз: ')
    return int(answer)

# Вопрос с простым ответом типа да/нет
def choose_answer(text, True_answ, False_answ):
    answer = input(text + '  ')
    while True:
        if answer in [True_answ, False_answ]:
            if answer == True_answ:
                return True
            else:
                return False
        else:
            answer = input(f'Не понятно. Попробуйте использовать {True_answ}/{False_answ}  ')

# Шифрование
def crypt(text, delta, vocab): # общее уравнение пилы y = a0 + (x + shift) % mod
    answer = ''
    a0 = ord(vocab[0])
    mod = len(vocab)
    shift = -a0 % mod
    for i in text:
        flag_upper = False
        if i.upper() == i:
                flag_upper = True
                i = i.lower()
        if i in vocab:
            askii_num = ord(i)
            symbol = chr(a0 + (askii_num + shift + delta) % mod)
            if flag_upper:
                symbol = symbol.upper()
        else:
            symbol = i
        answer += symbol
    return answer

# Константы
vocab_ru = [chr(1072 + i) for i in range(32)]
vocab_en = [chr(i) for i in range(97, 123)]

# Основная часть программы
if choose_answer('Зашифровать или расшифровать? да - 1/ нет - 2', '1', '2'):
    way = 1
else:
    way = -1
if choose_answer('Какой язык, русский - 1 / английский - 2', '1', '2'):
    vocabular = vocab_ru
else:
    vocabular = vocab_en
delta = input_int('Введите шаг сдвига (целое висло, вправо: +, влево: -): ')
print('delta:', delta, type(delta))
text = input('Введите текст:\n')

cr = crypt(text, way*delta, vocabular)
uncr = crypt(cr, -delta, vocabular)

print('text:     ', text)
print('crypted:  ', cr)
print('uncrypted:', uncr)

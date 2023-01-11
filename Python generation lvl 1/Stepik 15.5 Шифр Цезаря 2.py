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


# Шифрование только одного символа с автопроверкой языка
# Общее уравнение "пилы" y = a0 + (x - a0 % mod + delta) % mod
def crypt_one(symbol, delta):
    askii_num = ord(symbol)
    flag_is_letter = False
    if askii_num in range(97, 123):   # en
        a0 = 97
        mod = 26
        flag_is_letter = True
    elif askii_num in range(65, 91):  # EN
        a0 = 65
        mod = 26
        flag_is_letter = True
    elif askii_num in range(1072, 1104):  # ru
        a0 = 1072
        mod = 32
        flag_is_letter = True
    elif askii_num in range(1040, 1072):  # RU
        a0 = 1040
        mod = 32
        flag_is_letter = True
    if flag_is_letter:
        answer = chr(a0 + (askii_num - a0 % mod + delta) % mod)
    else:
        answer = symbol
    return answer


# Константы
vocab_ru = [chr(1072 + i) for i in range(32)]
vocab_en = [chr(i) for i in range(97, 123)]


# Основная часть программы
if choose_answer('Зашифровать - 1 / Расшифровать - 2', '1', '2'):
    way = 1
else:
    way = -1
text = input('Текст:\n')
delta = way * input_int('Шаг сдвига:')
crypt_text = ''
for i in text:
    crypt_text += crypt_one(i, delta)
print(crypt_text)

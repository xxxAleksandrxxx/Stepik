from random import sample


# Очищаем окно вывода для IDLE
def idle_semi_clear():
    for i in range(30):
        print()

# добиваемся, чтобы при ответе на вопрос ответили y/n д/н
def yes_or_no(text):
    variable = input(text + '  ').strip()
    while True:
        if variable in ['y', 'д']:
            return True
        elif variable in ['n', 'н']:
            return False
        else:
            variable = input('Не понятно.\nПожалуйста, используйте y/n д/н:  ').strip()

# Добиваемся, чтобы ввели целое число
def input_int(text):
    variable = input(text + '  ').strip()
    while True:
        if variable.isdigit():
            return int(variable)
        else:
            variable = input('Попробуйте еще раз.\nВведите целое число:  ')

# Функция генерации пароля
def generate_password(vocabular, length, numbers):
    return [''.join(sample(vocabular, length)) for _ in range(numbers)]

# Константы
digits = '0123456789'
l_letters = 'qwertyuiopasdfghjklzxcvbnm'
u_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
symbols = '!#$%&*+-=?@^_'


# Основная часть программы
idle_semi_clear()

chars = ''

print('Привет! Сейчас мы сгенерируем для вас безопсные пароли')
pasw_numbers = input_int('Сколько потребуется паролей?')
pasw_len = input_int('Какая длина пароля?')
if yes_or_no('Прописные буквы включить в пароль?  y/n д/н'):
    chars += u_letters
if yes_or_no('А строчные буквы включаем в пароль?  y/n д/н'):
    chars += l_letters
if yes_or_no('Цифры использовать?  y/n д/н'):
    chars += digits
if yes_or_no('А такое используем? !#$%&*+-=?@^_  y/n д/н'):
    chars += symbols
if yes_or_no('Исключить неоднозначные символы? il1Lo0O  y/n д/н'):
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

pasw_generated = generate_password(chars, pasw_len, pasw_numbers)

for i in pasw_generated:
    print(i)

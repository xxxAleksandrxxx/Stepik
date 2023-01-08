#%% 17.2.11 - Содержимое файла

"""
Содержимое файла

На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его содержимое."""

f_content = open(input(), 'r')
for raw in f_content:
    print(raw.strip())
f_content.close()

#%% 17.2.12 - Предпоследняя строка
"""На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его предпоследнюю строку."""

# v1
f_content = open(input(), 'r')
print(f_content.readlines()[-2].strip())
f_content.close()

# v2
f_content = open(input(), 'r', encoding='utf-8')
print(list(f_content)[-2].rstrip())
f_content.close()

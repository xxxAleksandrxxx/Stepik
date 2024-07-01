import requests
import os
import re

def get_user_question():
    question = input("Enter your question: ")
    return question

def send_api_request(question):
    api_key=os.environ["OPENAI_API_KEY"]

    if api_key is None:
        raise ValueError("API_KEY didn't found in environment variables")

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {"model": "gpt-3.5-turbo",
            "temperature": 0.7,
            "messages": [{"role": "system", "content": ""},
                         {"role": "user", "content": question}]}

    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def extract_python_code(api_response):
    if "```python" not in api_response:
        return ""  # code wan't found in the response
    pattern = r'```python(.*?)```'
    matches = re.findall(pattern, api_response, re.DOTALL)
    return "\n".join(matches)

def execute_code(code_to_execute):
    if input("Run the code? y/n  ") == "y":
        print()
        exec(code_to_execute)

def main():
    # try:
    question = get_user_question()
    api_response = send_api_request(question)
    python_code = extract_python_code(api_response)
    if python_code:
        print("Generated code:")
        print(python_code, end='\n\n')
        execute_code(python_code)
    else:
        print("\nThere is no code in the response.\n\nResponse:")
        print(api_response)

if __name__ == "__main__":
    main()






# import sys
# my_variable = [1, 2, 3]
# print(sys.getrefcount(my_variable))


# import sys
# my_var_1 = [1, 2]
# my_var_2 = [3, 4]
# my_var_1.append(my_var_2)
# my_var_2.append(my_var_1)

# counter = 0
# def iterate_cyclic_lists(start_list):
#     global counter
#     # Use a stack to keep track of the lists to visit
#     stack = [start_list]
#     while stack:
#         current_list = stack.pop()
#         for item in current_list:
#             if isinstance(item, list):
#                 stack.append(item)
#             else:
#                 print(item)
#                 counter += 1
#                 if counter > 10:
#                     print('counter:', counter)
#                     break

# iterate_cyclic_lists(my_var_1)


# import sys
# my_var_1 = [1, 2]
# my_var_2 = [3, 4]
# my_var_1.append(my_var_2)
# my_var_2.append(my_var_1)

# def iterate_cyclic_lists(start_list):
#     # Use a stack to keep track of the lists to visit
#     stack = [start_list]
#     # Use a set to keep track of visited lists to avoid infinite loops
#     visited = set()
#     while stack:
#         current_list = stack.pop()
#         if id(current_list) in visited:
#             continue 
#         visited.add(id(current_list))  # that's how we control looping
#         for item in current_list:
#             if isinstance(item, list):
#                 stack.append(item)
#             else:
#                 print(item)

# iterate_cyclic_lists(my_var_1)



# import requests
# import os
# import re

# def get_user_question():
#     question = input("Enter your question: ")
#     return question

# def send_api_request(question):
#     api_key=os.environ["OPENAI_API_KEY"]

#     if api_key is None:
#         raise ValueError("API_KEY didn't found in environment variables")

#     headers = {
#         'Authorization': f'Bearer {api_key}',
#         'Content-Type': 'application/json'
#     }
#     data = {"model": "gpt-3.5-turbo",
#             "temperature": 0.7,
#             "messages": [{"role": "system", "content": ""},
#                          {"role": "user", "content": question}]}

#     response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
#     response.raise_for_status()
#     return response.json()["choices"][0]["message"]["content"]

# def extract_python_code(api_response):
#     if "```python" not in api_response:
#         return ""  # code wan't found in the response
#     pattern = r'```python(.*?)```'
#     matches = re.findall(pattern, api_response, re.DOTALL)
#     return "\n".join(matches)

# def execute_code(code_to_execute):
#     if input("Run the code? y/n  ") == "y":
#         print()
#         exec(code_to_execute)

# def main():
#     # try:
#     question = get_user_question()
#     api_response = send_api_request(question)
#     python_code = extract_python_code(api_response)
#     if python_code:
#         print("Generated code:")
#         print(python_code, end='\n\n')
#         execute_code(python_code)
#     else:
#         print("\nThere is no code in the response.\n\nResponse:")
#         print(api_response)

# if __name__ == "__main__":
#     main()


# import os
# import requests
# import re

# def get_user_question():
#     question = input("Введите ваш вопрос: ")
#     return question

# def send_api_request(question):
#     api_key=os.environ["OPENAI_API_KEY"]

#     if api_key is None:
#         raise ValueError("API_KEY не найден в переменных окружения")

#     headers = {
#         'Authorization': f'Bearer {api_key}',
#         'Content-Type': 'application/json'
#     }
#     data = {"model": "gpt-3.5-turbo",
#             "temperature": 0.7,
#             "messages": [{"role": "system", "content": ""},
#                          {"role": "user", "content": question}]}

#     response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
#     response.raise_for_status()
#     return response.json()["choices"][0]["message"]["content"]

# def extract_python_code(api_response):
#     if "```python" not in api_response:
#         # return -1  # no code found
#         return "print('А нету кода')"  # no code found
#     pattern = r'```python(.*?)```'
#     matches = re.findall(pattern, api_response, re.DOTALL)
#     return "\n".join(matches)

# def execute_code(code_to_execute):
#     if input("run the code? y/n  ") == "y":
#         print()
#         exec(code_to_execute)

# def main():
#     # try:
#     question = get_user_question()
#     api_response = send_api_request(question)
#     python_code = extract_python_code(api_response)
#     print("Сгенерированный код:")
#     print(python_code, end='\n\n')
#     execute_code(python_code)

# if __name__ == "__main__":
#     main()
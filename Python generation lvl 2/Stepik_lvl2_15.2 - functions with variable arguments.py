'''
def count_args(*args):
	return len(args)
	
print(count_args())
print(count_args(10))
print(count_args('stepik', 'beegeek'))
print(count_args([], (''), 'a', 12, False))
'''

'''
# 15.2.11 v1
def sq_sum(*args):
	answer = 0
	for number in args:
		answer += number**2
	return answer
'''
'''
# 15.2.11 v2
def sq_sum(*args):
	return sum(map(lambda x: x**2, args))
'''
'''
#15.2.11 v3
def sq_sum(*args):
	return sum(num**2 for num in args)

print(sq_sum())
print(sq_sum(2))
print(sq_sum(1.5, 2.5))
print(sq_sum(1, 2, 3))
print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
'''

'''
#15.2.12 v1
def mean(*args):
	count = 0
	sum = 0
	flag = False
	for elem in args:
		if type(elem) in (int, float):
			flag = True
			sum += elem
			count += 1
	if flag:
		return sum/count
	else:
		return 0
'''
'''
#15.2.12 v2
def mean(*args):
	l = [elem for elem in args if type(elem) in (int, float)]
	return sum(l)/len(l) if l else 0.0
	
print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
'''
'''
#15.2.13 v1
def greet(name, *args):
	answer = f'Hello, {name}'
	if args:
		for elem in args:
			answer += f' and {elem}'
	answer += '!'
	return answer
'''
'''
#15.2.13 v2
def greet(name, *args):
	return f'Hello, {" and ".join((name,)+args)}!'
	
print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
'''

'''
#15.2.14 v1

def print_products(*args):
	count = 0
	for elem in args:
		if type(elem) == str and elem:
			count += 1
			print(f'{count}) {elem}')
	if count == 0:
		print('Нет продуктов')
		
print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print()
print_products([4], {}, 1, 2, {'Beegeek'}, '') 
'''


# 15.2.15.1
def info_kwargs(**kwargs):
	for key in sorted(kwargs):
		print(f'{key}: {kwargs[key]}')
		

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher') 

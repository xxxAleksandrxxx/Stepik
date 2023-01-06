#15.9 base info
#%%
a = []
a1 = ()
a2 = {}
b = [[], []]
b1 = 
print(type(b1))
f = all(b1)
print(f)
#%% all()
def if_all_less(numbers0, num0):
    """проверяем, все ли элементы меньше заданного значения num0"""
    flag = all(map(lambda x: x < num0, numbers0))
    if flag:
        print(f'все элементы меньше {num0}')
    else:
        print(f'хоть один элемент больше {num0}')
    return flag

numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]
if_all_less(numbers, 2000)

#%% enumerate()
numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]

en = enumerate(numbers)
print(type(en))
print(*en)

#%% zip()
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = ['apple', 'banana', 'carrot']
z = zip(a, b, c)
print(type(z))
print(*z)
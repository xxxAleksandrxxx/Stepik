# Theory
"""
from datetime import timedelta

t_delta = timedelta(days = 7, hours = 2, minutes = 37)
print(t_delta)
"""


"""from datetime import timedelta

delta1 = timedelta(days=50, seconds=27, microseconds=10)
delta2 = timedelta(weeks=1, hours=23, minutes=61)
delta3 = timedelta(hours = 25)
delta4 = timedelta(minutes=300)

for i in range(1, 5):
    v_name = 'delta'+str(i)
    v_value = vars()[v_name]
    print(v_name, v_value)

print(delta2 - delta2)"""


"""from datetime import timedelta 
t_delta = timedelta(weeks=3, days=2, hours=12, minutes=33, seconds=5, milliseconds=280, microseconds=10)

print(t_delta)
print('days ', t_delta.days)
print('sec  ', t_delta.seconds)
print('mcsec', t_delta.microseconds)
print('/n')
# + - * /
print(t_delta)
print(t_delta + timedelta(minutes=100))
print()
print(t_delta)
print(t_delta - timedelta(hours=2))
print()
print(t_delta)
print(t_delta * 5)
print()
print(t_delta)
print(t_delta / 3)
print(t_delta // 3)"""


"""
рабочая смена длится 7 часов 30 минут, сколько полных смен в 3-х сутках?
"""

from datetime import timedelta
all_time = timedelta(days=3)
smena = timedelta(hours=7, minutes=30)
print('количество смен в 3-х сутках:', all_time // smena)


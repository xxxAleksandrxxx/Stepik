'''
city_1, city_2, city_3 = input(), input(), input()
if len(city_1) > len(city_2):
    city_1, city_2 = city_2, city_1
if len(city_2) > len(city_3):
    city_2, city_3 = city_3, city_2
if len(city_1) > len(city_2):
    city_1, city_2 = city_2, city_1
print(city_1)
print(city_3)
'''
c1, c2, c3 = input(), input(), input()
print(min(c1, c2, c3, key = len))
print(max(c1, c2, c3, key = len))
'''
к ознакомлению:
https://medium.com/analytics-vidhya/how-to-use-key-function-in-max-and-min-in-python-1fdbd661c59c
'''

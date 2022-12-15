# 14.2
'''
import turtle

t1 = turtle.Turtle()
t1.speed(0)
t1.pencolor('DarkOrange')
def paint():
    for i in range(1, 5):
        t1.pensize(i)
        t1.forward(100)
        t1.left(90)

for i in range(10):
    paint()
    t1.left(10)
turtle.exitonclick()
'''
'''
import turtle

turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 255)

turtle.exitonclick()
'''


# 14.2.2
'''
Напишите программу, которая рисует пунктирную линию
'''
'''
import turtle

turtle.speed(9)
l = 10
line = 100
for i in range(0, line, l):
    turtle.dot()
    turtle.up()
    turtle.fd(l)
turtle.exitonclick()
'''

# 14.2.3
'''
Напишите программу, которая рисует прямоугольник с точкой в каждом углу
'''
'''
import turtle
turtle.speed(0)
a = 100
b = 50
for num in [a, b]*2:
    turtle.fd(num)
    turtle.dot()
    turtle.left(90)
turtle.exitonclick()
'''


# 14.2.4
'''
Напишите программу для рисования паутины в соответствии с примером. Программа должна считывать количество лучей паутины, число n
'''
'''
import turtle
turtle.speed(0)
n = 6
l = 100
turtle.dot(10)
# turtle.shape('triangle')
alfa = 360/n
count = 0
while count < 360:
    turtle.fd(l)
    turtle.stamp()
    turtle.back(l)
    turtle.left(alfa)
    count += alfa
# turtle.fd(l/10)
i = 0
while i < 100:
    turtle.left(alfa)
    turtle.fd(i)
    i += 1

turtle.exitonclick()
'''


# 14.2.5
'''
Напишите программу, которая рисует черепашек в соответствии с образцом.
'''
'''
import turtle
turtle.speed(5)
turtle.shape('turtle')
turtle.stamp()
turtle.up()
n = 6
l = 100
angle = 360/n
for i in range(0, 360, 360//n):
    turtle.fd(l)
    turtle.stamp()
    turtle.back(l)
    turtle.left(angle)
turtle.hideturtle()
turtle.exitonclick()
'''


# 14.2.6
'''
Напишите программу, которая рисует циферблат часов в соответствии с образцом.
'''
'''
import turtle
turtle.speed(0)
turtle.shape('turtle')
turtle.pensize(4)
l = 200
l1 = 20
n = 12
angle = 360/n
for _ in range(0, 360, 360//n):
    turtle.up()
    turtle.fd(l - 2*l1)
    turtle.down()
    turtle.fd(l1)
    turtle.up()
    turtle.fd(l1)
    turtle.stamp()
    turtle.back(l)
    turtle.left(angle)
turtle.exitonclick()
'''


# 14.2.7
'''
Напишите программу, которая рисует черепашью спираль в соответствии с образцом.
'''
'''
import turtle
turtle.speed(0)
turtle.shape('turtle')
turtle.up()
for i in range(0, 150, 5):
    turtle.stamp()
    turtle.fd(i)
    turtle.right(27)
turtle.exitonclick()
'''


# Плавное изменение цвета в RGB формате
'''
import turtle
turtle.colormode(255)
turtle.bgcolor('black')
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0, 0)  # скрыть перемещение черепашки для ускорения отрисовки
r = 0
g = 0 
b = 255
color_step = 3
l = 5
for i in range(1, 1000): 
    if 0 < i % 379 < 64: 
        r += color_step
    elif 63 < i % 379 < 127: 
        b -= color_step 
    elif 126 < i % 379 < 190: 
        g += color_step
    elif 189 < i % 379 < 253:
        r -= color_step
    elif 252 < i % 379 < 316:
        b += color_step
    elif 315 < i % 379 < 379:
        g -= color_step
    turtle.pencolor(r, g, b) 
    l += 0.1
    turtle.left(45)
    turtle.forward(l)
turtle.update()  # отобразить нарисованное
turtle.mainloop()
'''


# 14.2.8
'''
Напишите программу, которая рисует узор в соответствии с образцом.
спираль, постепенно меняется толщина линии и ее цвет
'''

import turtle
turtle.tracer(0, 0)
turtle.hideturtle()
tire = '2'
colors = [f'SpringGreen{tire}', f'SlateBlue{tire}', f'tomato{tire}', f'red{tire}', f'SteelBlue{tire}']
colors_len = len(colors)
angle = 45
turtle.pensize(0.1)
l = 10
for i in range(50):
    turtle.fd(l)
    turtle.left(angle)
    turtle.pensize(i/1)
    turtle.pencolor(colors[i%colors_len])
    l += 5
turtle.update()
turtle.exitonclick()
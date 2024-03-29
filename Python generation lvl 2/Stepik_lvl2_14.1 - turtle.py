# 14.1
'''
import turtle
import math
t1 = turtle.Turtle()


def paint1(dist, ang, n):
    t1.reset()
    t1.speed(100)
    t1.hideturtle()
    turtle.tracer(0, 0)
    for _ in range(n):
        t1.fd(dist)
        t1.left(ang)
        dist += 30/dist
    turtle.update()

def paint1_c(dist, ang, n):  #color 
    t1.reset()
    t1.speed(100)
    t1.hideturtle()
    turtle.tracer(0, 0)
    # r_i = hex(r_i)
    turtle.colormode(255)
    t1.pencolor(r, g, b)
    
    for _ in range(n):
        t1.fd(dist)
        t1.left(ang)
        dist += 30/dist
    turtle.update()


def paint2(dist, ang, n):
    t1.reset()
    t1.speed(100)
    t1.hideturtle()
    turtle.tracer(0, 0)
    for _ in range(n):
        t1.fd(dist)
        t1.left(ang)
        dist += dist**0.2
    turtle.update()

def paint3(dist, ang, n):
    t1.reset()
    t1.speed(100)
    t1.hideturtle()
    turtle.tracer(0, 0)
    for _ in range(n):
        t1.fd(dist)
        t1.left(ang)
        dist += 0.1
    turtle.update()


n = 2500
dist = 10
ang_step = 0.001
ang = 78
end = 100

turtle.bgcolor('gray')
r0 = 1
r_max = 20
r = r0
g = 30
b = 80
t = 1
while ang < end:
    turtle.title(f'угол = {ang:.3f}')
    print(f'r = {r}  g = {g}  b = {b}')
    r = (r + t)
    if r == r_max or r == r0:
        t *= -1

    paint1_c(dist, ang, n)
    ang += ang_step

turtle.done()
'''

'''
import turtle
import random

x = 1
SN = turtle.Screen()
SN.bgcolor("gray")
a = turtle.Turtle()
a.speed(0)
a.hideturtle()

i = 0
while x < 256:

    r = random.randint(0,255)
    g = 100
    b = 150
    
    turtle.colormode(255)
    a.pencolor(i,i,b)
    if x<252:
        a.pensize(1)
        a.forward(50 + x)
        a.right(91.5)
       
    x = x+1
    i = (i+1)%255    

turtle.done()   
'''


# 14.1.2
'''
Напишите программу, которая рисует прямоугольник.
Примечание. Программу нужно оформить в виде функции rectangle(width, height), где width, height – ширина и высота прямоугольника.
'''
'''
import turtle
t = turtle.Turtle()

def rectangel(len = 30, hight = 10):
    for i in [len, hight, len, hight]:
        t.forward(i)
        t.left(90)

rectangel(30, 20)

turtle.done()
'''


# 14.1.3
'''
Напишите программу, которая рисует правильный треугольник.
Программу нужно оформить в виде функции triangle(side), где side – длина стороны треугольника в пикселях.
'''
'''
import turtle

def triangle(side):
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)

triangle(190)

turtle.done()
'''


# 14.1.4
'''
Напишите программу, которая рисует изображенную фигуру, состоящую из трех квадратов.
Примечание 1. Напишите функцию square(side), где side – длина стороны квадрата в пикселях.
Примечание 2. Поэксперементируйте с углом поворота черепашки при переходе от одного квадрата к другому.
'''
'''
import turtle

turtle.speed(0)

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

n = 12
a0 = 45/n
a1 = 10
s = 100

for i in range(n):
    turtle.setheading(a0)
    square(s)
    a0 += 90/n

turtle.done()
'''

# 14.1.5 
'''
Напишите программу, которая рисует изображенную фигуру из восьми квадратов.
'''
'''
import turtle

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

turtle.speed(9)
side = 100

for _ in range(8):
    square(side)
    turtle.left(45)

# turtle.done()
turtle.exitonclick()
'''


# 14.1.6
'''
Напишите программу, которая рисует правильный шестиугольник.
'''
'''
import turtle

turtle.speed(9)
side = 50

for _ in range(6):
    turtle.forward(side)
    turtle.left(60)

turtle.exitonclick()
'''


'''
правильный n-угольник
'''
'''
import turtle

turtle.speed(9)
side = 50
n = 7
angle = 360 / n

for _ in range(n):
    turtle.forward(side)
    turtle.left(angle)

turtle.exitonclick()
'''


# 14.1.7
'''
Напишите программу, которая рисует соты.
'''
'''
import turtle

def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)

turtle.speed(0)
side = 50

for i in range(0,6):
    hexagon(side)
    turtle.forward(side)
    turtle.right(60)

turtle.exitonclick()
'''


# 14.1.8
'''
Напишите программу, которая рисует ромб с углами 60 и 120 градусов.
'''
'''
import turtle

def rhombus(side, angle = 120):
    for alfa in [angle, 180-angle]*2:
        turtle.forward(side)
        turtle.left(alfa)

turtle.speed(0)
side = 150
rhombus(side)

turtle.exitonclick()
'''

# 14.1.9
'''
Напишите программу, которая рисует снежинку из 10 ромбов.
'''
'''
import turtle

def rhombus(side0, angle0 = 36):
    # color = ['purple']*4
    for alfa in [180 - angle0, angle0]*2:
        # turtle.pencolor(color.pop(0))
        turtle.left(alfa)
        turtle.forward(side0)

turtle.speed(0)
n = 10
side = 150
alfa_shift = 30  # смещение лепестков снежинок

for i in range(n):
    rhombus(side, 360/n + alfa_shift)
    turtle.left(360/n)

turtle.exitonclick()
'''


# анимация снежинки
'''
import turtle

def rhombus(side0, angle0 = 36):
    # color = ['purple']*4
    for alfa in [180 - angle0, angle0]*2:
        # turtle.pencolor(color.pop(0))
        turtle.left(alfa)
        turtle.forward(side0)

def rhombus_circle(n0, side0, alfa_shift0):
    for _ in range(n0):
        rhombus(side0, 360/n0 + alfa_shift0)
        turtle.left(360/n0)

turtle.speed(0)
n = 39
side = 150
alfa_shift = 30  # смещение лепестков снежинок

turtle.hideturtle()
alfa_step = 0.1
alfa_max = 178

for i_n in range(200, 300):
    alfa = 90
    while alfa < alfa_max:
        turtle.clear()
        turtle.title(f'alfa = {alfa:.2f}')
        turtle.tracer(0, 0)
        rhombus_circle(i_n, side, alfa)
        turtle.update()
        alfa += alfa_step


turtle.exitonclick()
'''


# 14.1.10
'''
Напишите программу, которая рисует лучи звезды, показанной на рисунке.
'''
'''
import turtle

turtle.speed(0)
n = 12
length = 100
angle = 360 / n
for _ in range(n):
    turtle.forward(length)
    turtle.up()
    turtle.backward(length)
    turtle.down()
    turtle.left(angle)

turtle.exitonclick()
'''


# 14.1.11
'''
Напишите программу, которая рисует правильную пятиконечную звезду.
'''
'''
import turtle

turtle.speed(3)
length = 200
angle0 = 180-144
angle = 144
turtle.right(angle0)
for _ in range(5):
    turtle.left(angle)
    turtle.fd(length)

turtle.exitonclick()
'''


# 14.1.12
'''
Напишите программу, которая рисует квадраты, чтобы создать узор, показанный на рисунке.
'''
'''
import turtle

turtle.speed(0)
side0 = 15
side_max = 200
step = 5
for l in range(side0, side_max, step):
    turtle.setheading(0)
    turtle.left(90)
    for _ in range(4):
        turtle.fd(l)
        turtle.left(90)

turtle.exitonclick()
'''


# 14.1.13
'''
Напишите программу, которая рисует узор, показанный на рисунке.
квадратная спираль
'''
'''
import turtle

turtle.speed(0)
n = 50
l0 = 10
step = 3
angle = 90
turtle.left(angle)
l = l0
for _ in range(n):
    turtle.fd(l)
    l += step
    turtle.left(angle)

turtle.exitonclick()
'''
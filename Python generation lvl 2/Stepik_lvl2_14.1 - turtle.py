# 14.1
'''
import turtle
import math
t1 = turtle.Turtle()
# t1.showturtle()
# t1.bk(100)
# t1.hideturtle()

n = 1000
dist = 30
ang_step = 0.001
ang = 73
end = 115



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



turtle.bgcolor('gray')
r = 1
g = 50
b = 100
t = 1
while ang < end:
    turtle.title(f'угол = {ang:.3f}')
    print(f'r = {r}  g = {g}  b = {b}')
    r = (r + t)
    if r == 115 or r == 1:
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
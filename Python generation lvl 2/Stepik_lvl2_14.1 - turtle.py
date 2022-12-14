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
import turtle
t = turtle.Turtle()

def rectangel(len = 30, hight = 10):
    for i in [len, hight, len, hight]:
        t.forward(i)
        t.left(90)

rectangel(30, 20)

turtle.done()
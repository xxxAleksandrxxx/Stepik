# 14.3
'''
import turtle
import random
c = random.choice(['gray10', 'gray20', 'gray30', 'gray40', 'gray50'])
turtle.Screen().bgcolor(c)
# создаем много черепашек
t_list = []
n = 10
for _ in range(n):
    t = turtle.Turtle()
    t.speed(2)
    t.fillcolor(c)
    t.pensize(5)
    #t.hideturtle()
    t.pencolor([random.random(), random.random(), random.random()])
    t_list.append(t)

ang = 0
for turt in t_list:
    turtle.Screen().tracer(5)
    ang += 30
    turt.right(ang)
    turt.fd(ang)
    turt.circle(50)
    #turtle.update()

print('t_list', t_list)
turtle.exitonclick()
'''


# 14.3.2
'''
Напишите программу, которая рисует изображение домика по образцу.
'''
'''
import turtle

# turtle.tracer(0, 0)
turtle.hideturtle()
a = 150
b = a*1.5
h = a*0.75

def sq(length, x0, y0):
    turtle.up()
    turtle.goto(x0, y0)
    turtle.down()
    turtle.setheading(0)
    turtle.fillcolor('DodgerBlue')
    turtle.begin_fill()
    turtle.goto(x0 + length/2, y0)
    turtle.goto(x0 + length/2, y0 - length)
    turtle.goto(x0 - length/2, y0 - length)
    turtle.goto(x0 - length/2, y0)
    turtle.goto(x0, y0)
    turtle.end_fill()

def tri(length, hight, x0=0, y0=0):
    turtle.up()
    turtle.goto(x0, y0)
    turtle.down()
    c = (length**2/4 + h**2)**0.5
    turtle.setheading(0)
    turtle.fillcolor('chocolate4')
    turtle.begin_fill()
    turtle.goto(x0+length/2, y0-hight)
    turtle.goto(x0-length/2, y0-hight)
    turtle.goto(x0, y0)
    turtle.end_fill()


sq(a, 0, h/2)
turtle.up()
turtle.goto(0, h+h/2)
turtle.down()
tri(b, h, 0, h+h/2)

turtle.update()

turtle.exitonclick()
'''


# 14.3.3
'''
Напишите программу, которая рисует изображение светофора
'''
'''
import turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
size = 200
h = size
l = size*0.4
r = 0.7*l/2

def circle(r0, x0=0, y0=0, color0='red'):
    t.up()
    t.goto(x0, y0)
    t.down()
    t.fillcolor(color0)
    t.begin_fill()
    t.circle(r0)
    t.end_fill()

X0 = 0
Y0 = h/2
t.up()
t.goto(X0, Y0)
t.down()
t.fillcolor('black')
t.begin_fill()
t.goto(l/2+X0, Y0)
t.goto(l/2+X0, Y0-h)
t.goto(-l/2+X0, Y0-h)
t.goto(-l/2+X0, Y0)
t.goto(X0, Y0)
t.end_fill()
Y0 -= h/2+r
circle(r, X0, Y0+h/2*0.62, 'red')
circle(r, X0, Y0+0, 'yellow')
circle(r, X0, Y0-h/2*0.62, 'green')

turtle.exitonclick()
'''


# 14.3.4
'''
Напишите программу, которая рисует оптическую иллюзию по образцу.
'''
'''
import turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
a = 200
r = a*0.15
x0 = -a/2
y0 = -a/4

def tri(length, X0=0, Y0=0, fill='False'):
    if fill:
      t.fillcolor('white')
      t.begin_fill()
      t.pencolor('white')
    t.up()
    t.goto(X0, Y0)
    t.down()
    for _ in range(3):
        t.fd(length)
        t.left(120)
    t.end_fill()

def circ(radius, X=0, Y=0, bk_color='black'):
    t.up()
    t.goto(X, Y)
    t.down()
    t.fillcolor(bk_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

tri(a, x0, y0, False)
circ(r, x0+a/2, y0 - (a*3**0.5)/6 - r)
circ(r, x0+a, y0 + 2*(a*3**0.5)/6 - r)
circ(r, x0, y0 + 2*(a*3**0.5)/6 - r)
tri(-a, a/2, a/3, True)

turtle.exitonclick()
'''


# 14.3.5
'''
Напишите программу, которая рисует изображение радуги по образцу.
'''
'''
import turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
radius = 150
step = radius/7
colors = ['#fc0303', '#fc8003', '#fcdb03', '#0ffc03', '#03dbfc', '#0307fc', '#9803fc']
t.up()
t.goto(0, -radius)
t.down()
y = -radius
for color in colors:
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    y += step
    t.up()
    t.goto(0, y)
    t.down()
    radius -= step

turtle.exitonclick()
'''


# 14.3.6
'''
Напишите программу, которая рисует изображение полумесяца 
'''
'''
import turtle
a = 400
r = a*0.7/2
x0 = -a/2
y0 = -a/2
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.up()
t.goto(x0, y0)
t.down()
t.fillcolor('#324ca8')
t.begin_fill()
for _ in range(4):
    t.fd(a)
    t.left(90)
t.end_fill()
t.up()
t.goto(0, -r)
t.fillcolor('#ffde05')
t.begin_fill()
t.circle(r)
t.end_fill()
t.fd(r*0.2)
t.fillcolor('#324ca8')
t.begin_fill()
t.circle(r)
t.end_fill()

turtle.exitonclick()
'''


# 14.3.7
'''
Напишите программу, которая рисует анимированное изображение фаз луны
'''
'''
# v1
import turtle
r = 150
turtle.tracer(0, 0)
turtle.Screen().bgcolor('#324ca8')
t = turtle.Turtle()
t.hideturtle()
t.up()
x = 2*r
y = -r
for _ in range(2*r):
    t.goto(0, -r)
    t.fillcolor('#ffde05')
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.goto(x, y)
    t.fillcolor('#324ca8')
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    turtle.update()
    x -= 2
turtle.exitonclick()
'''
'''
# v2
import turtle
r = 100
m = turtle.Turtle()
m.shape('circle')
m.shapesize(r/10)
m.pencolor('#ffde05')
m.fillcolor('#ffde05')
turtle.tracer(0, 0)
turtle.Screen().bgcolor('#324ca8')
m.stamp()
m.up()
m.pencolor('#324ca8')
m.fillcolor('#324ca8')
m.goto(2*r, 0)
turtle.update()
turtle.tracer(1, 50)
m.speed(1)
m.goto(-2*r, 0)

turtle.exitonclick()
'''


# 14.3.8
'''
Напишите программу, которая рисует много 5-ти конечных зведочек. Звезды должны быть рассыпаны случайно, иметь разный размер и цвет.
'''
'''
import turtle
import random
size_min = 5
size_max = 15
n = 100
l = 300
h = 300

def star_random(size0, x0=0, y0=0):
    s = turtle.Turtle()
    s.hideturtle()
    s.up()
    s.goto(x0,  y0)
    turtle.tracer(0, 0)
    s.setheading(random.uniform(0, 90))
    s.fillcolor(random.random(), random.random(), random.random())
    s.begin_fill()
    for _ in range(5):
        s.fd(size0)
        s.left(144)
        s.fd(size0)
        s.right(72)
    s.end_fill()
    turtle.update()

turtle.colormode(1)
turtle.Screen().bgcolor(0, 0, 0.1)
for _ in range(n):
    x = random.uniform(-l, l)
    y = random.uniform(-h, h)
    size = random.randrange(size_min, size_max, 1)
    star_random(size, x, y)

turtle.exitonclick()
'''


# 14.3.9
'''
Напишите программу, которая рисует изображение правильных многоугольников по образцу. Многоугольники должны иметь разный цвет.
'''
'''
import turtle, math, random

turtle.colormode(255)
l = 50
s = 3000
x = -200
y = -200
i = 2

def fig(len0, n0=3, x0=0, y0=0, color0=[120, 120, 120]):
    angle = 360/n0
    turtle.tracer(0, 0)
    f = turtle.Turtle()
    f.hideturtle()
    f.up()
    f.goto(x0, y0)
    f.fillcolor(color0)
    f.begin_fill()
    f.fd(len0/2)
    f.left(angle)
    for _ in range(n0-1):
        f.fd(len0)
        f.left(angle)
    f.fd(len0/2) 
    f.end_fill()
    turtle.update()

for x_i in range(x, -x, int(s**0.5*1.8)):
    for y_i in range(y, -y, int(s**0.5*1.8)):
        i = random.randrange(3, 9)
        color = [random.randrange(10, 200) for _ in range(3)]
        a = (4*s*math.tan(math.radians(180/i))/i)**0.5
        fig(a, i, x_i, y_i, color)

turtle.exitonclick()
'''


# 14.3.10
'''
Напишите программу, которая рисует изображение шахматной доски 
'''

import turtle
length = 200
n = 5
l = length/n
y = -length/2

def sq(len0, x0=0, y0=0, color0='black'):
    turtle.tracer(0, 0)
    ch = turtle.Turtle()
    ch.hideturtle()
    ch.up()
    ch.goto(x0, y0)
    ch.down()
    ch.fillcolor(color0)
    ch.begin_fill()
    for _ in range(4):
        ch.fd(len0)
        ch.left(90)
    ch.end_fill()
    turtle.update()

colors = ('black', 'white')
count = 1
for i in range(0, n):
    x = -length/2
    for j in range(0, n):
        color = colors[(i+j)%2]
        sq(l, x, y, color)
        x += l
    y += l

turtle.exitonclick()
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
'''


# 14.2.11
'''
Напишите программу, которая рисует звезду, показанную на рисунке. Такую звезду можно создать из двух треугольников. Однако их невозможно нарисовать непрерывной линией, поэтому перо нужно будет поднять для перехода ко второму треугольнику.
'''
'''
# v1
import turtle
turtle.speed(4)
a = 100
for _ in range(6):
    turtle.right(60)
    turtle.fd(a)
    turtle.left(60+60)
    turtle.fd(a)
for _ in range(6):
    turtle.fd(a)
    turtle.left(60)
turtle.exitonclick()
'''

# v2
'''
import turtle
turtle.speed(8)
c = 100
b = 0.5 * c * 3**0.5
a = 0.5 * c
turtle.up()
turtle.setpos(0, -2*b)
turtle.down()
x = turtle.xcor()
y = turtle.ycor()


x += a
y += b
turtle.setpos(x, y)
x += c
y += 0
turtle.setpos(x, y)
x -= a
y += b
turtle.setpos(x, y)
x += a
y += b
turtle.setpos(x, y)
x -= c
y += 0
turtle.setpos(x, y)
x -= a
y += b
turtle.setpos(x, y)
x -= a
y -= b
turtle.setpos(x, y)
x -= c
y -= 0
turtle.setpos(x, y)
x += a
y -= b
turtle.setpos(x, y)
x -= a
y -= b
turtle.setpos(x, y)
x += c
y += 0
turtle.setpos(x, y)
x += a
y -= b
turtle.setpos(x, y)
x += 2*a
y += 2*b
turtle.setpos(x, y)
x -= a
y += b
turtle.setpos(x, y)
x -= c
y -= 0
turtle.setpos(x, y)
x -= a
y -= b
turtle.setpos(x, y)
x += a
y -= b
turtle.setpos(x, y)
x += c
y += 0
turtle.setpos(x, y)
turtle.exitonclick()
'''
# v3
'''
import turtle
turtle.speed(8)
c = 50
a = 0.5 * c
b = 0.5 * c * 3**0.5
x, y = 0, 0
x += 3*c
y += 0
turtle.goto(x, y)
for i in range(2):
    x -= 0.5*3*c
    y += 3*b*(-1)**i
    turtle.goto(x, y)
turtle.up()
x += 0.5*3*c
y -= b
turtle.goto(x, y)
turtle.down()
x += 0.5*3*c
y += 3*b
turtle.goto(x, y)
x -= 3*c
y -= 0
turtle.goto(x, y)
x += 0.5*3*c
y -= 3*b
turtle.goto(x, y)
turtle.exitonclick()
'''
# v4
'''
import turtle
turtle.speed(8)
c = 150
a = 0.5 * c
b = 0.5 * c * 3**0.5
turtle.up()
x, y = -0.5*3*c, -b
turtle.goto(x, y)
turtle.down()
x += 3*c
y += 0
turtle.goto(x, y)
for i in range(2):
    x -= 0.5*3*c
    y += 3*b*(-1)**i
    turtle.goto(x, y)
turtle.up()
x += 3*c
y += 2*b
turtle.goto(x, y)
turtle.down()
x -= 3*c
y += 0
turtle.goto(x, y)
for i in range(2):
    x += 0.5*3*c
    y -= 3*b*(-1)**i
    turtle.goto(x, y)

turtle.exitonclick()
'''


# 14.2.12
'''
Напишите программу, которая рисует изображение в соответствии с образцом.
лучи вниз из центральной точки наверху
'''
'''
import turtle

turtle.speed(0)
turtle.hideturtle()
n = 5
h = 100
l = 350
dot_size = 20
step = l / (n-1)
x0, y0 = -l/2, -h/2
turtle.up()
turtle.goto(x0, y0)
turtle.down()
for i in range(0, n):
    turtle.pencolor('green')
    turtle.goto(l/2 + x0, h + y0)
    turtle.down()
    turtle.goto(i * step + x0, 0 + y0)
    turtle.pencolor('blue')
    turtle.dot(dot_size)
    turtle.up()
turtle.pencolor('green')
turtle.goto(l/2 + x0, h + y0)
turtle.pencolor('red')
turtle.dot(dot_size)

turtle.exitonclick()
'''


# 14.2.13
'''
Напишите программу, которая рисует цветные олимпийские кольца
'''
'''
import turtle

turtle.speed(0)
turtle.hideturtle()
turtle.pensize(10)
r = 50
shift = -30*r/100
x0 = -2*r + 1*shift
y0 = -1*r
x, y = x0, y0
turtle.up()
for color in ['blue', 'black', 'red', 'orange', 'green']:
    if color == 'orange':
        x = x0 + r - shift/2
        y = y0 - r - abs(shift/2)
    turtle.goto(x, y)
    turtle.down()
    turtle.pencolor(color)
    turtle.circle(r)
    turtle.up()
    x += 2*r - shift

turtle.exitonclick()
'''


# 14.2.14
'''
Напишите программу, которая рисует изображение мордашки мишки.
'''
'''
import turtle

turtle.tracer(0, 0)
turtle.hideturtle()
head = 150
mouth = 1.1*head/2
nose = 0.2*mouth
eye = nose*1.9
ear = mouth/2
x0, y0 = 0, -head-ear
turtle.up()
turtle.goto(x0, y0)
turtle.down()
# head
turtle.circle(head)
# mouth and nose
turtle.circle(mouth)
turtle.up()
turtle.goto(x0, y0 + 2*nose)
turtle.down()
turtle.goto(x0, y0 + 2*mouth - 3*nose)
turtle.circle(nose)
# eyes
turtle.up()
turtle.goto(x0 + head/2, y0 + 1.1*head)
turtle.down()
turtle.dot(eye)
turtle.up()
turtle.goto(x0 - head/2, y0 + 1.1*head)
turtle.down()
turtle.dot(eye)
# ears
turtle.up()
turtle.goto(x0 + 7*head/8, y0 + 1.65*head)
turtle.down()
turtle.circle(ear)
turtle.up()
turtle.goto(x0 - 7*head/8, y0 + 1.65*head)
turtle.down()
turtle.circle(ear)

turtle.update()
turtle.exitonclick()
'''


# 14.2.15
'''
Напишите программу, которая случайным образом рисует снежинки разного цвета и размера
'''

import turtle
import random

def snowflake(size0, color0, x0, y0):
    s = turtle.Turtle()
    s.hideturtle()
    turtle.tracer(0, 0)
    s.pencolor(color0)
    s.pensize(size0/30)
    s.up()
    s.goto(x0, y0)
    s.down()
    s.speed(9)
    sl = size0/4
    ss = 0.5*sl*2**0.5
    for _ in range(8):
        for _ in range(3):
            s.fd(sl)
            s.left(45)
            s.fd(sl)
            s.up() 
            s.bk(sl) 
            s.down()
            s.right(90)
            s.fd(sl)
            s.up() 
            s.bk(sl) 
            s.down()
            s.left(45)
        s.fd(ss)
        s.up()
        s.bk(size0-sl+ss)
        s.down()
        s.left(45)
    turtle.update()

h = 600
w = 600

turtle.Screen().setup(h, w)
turtle.Screen().bgcolor('azure')
n = 50
for _ in range(n):
    x, y = [random.uniform(-0.47*w, 0.47*w) for _ in range(2)]
    color = (random.uniform(0, 1) for _ in range(3))
    snowflake(random.uniform(5, 50), color, x, y)
    # turtle.update()

turtle.exitonclick()

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
'''


# 14.3.11
'''
Напишите программу, которая рисует изображение компаса
'''
'''
import turtle
l = 100
r = l/3
words = ['Восток', 'Север', 'Запад', 'Юг']
align = ['left', 'center', 'right', 'center']
shift = [r/2, r/2, r/2, 1.7*r/2]
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

for i in range(4):
    t.fd(l)
    t.up()
    t.fd(shift[i])
    t.write(words[i], False, align[i], font=('Arial', 14))
    t.back(l+shift[i])
    t.left(90)
    t.down()

t.goto(0, -r)
t.circle(r)

turtle.exitonclick()
'''


# 14.3.12
'''
Напишите программу, которая рисует солнечную систему
'''
'''
import turtle
# t = turtle.Turtle()

def planet(r0=100, name0='test', x0=0, y0=0, color0='red'):
    y0 -= r0
    turtle.tracer(0, 0)
    p = turtle.Turtle()
    p.hideturtle()
    p.up()
    p.goto(x0, y0)
    p.down()
    p.fillcolor(color0)
    p.begin_fill()
    p.circle(r0)
    p.end_fill()
    y0 -= 20
    p.up()
    p.goto(x0, y0)
    p.down()
    p.write(name0, False, 'center', ('Arial', 14))
    turtle.update()

r = 5
s = 700
planets = {
    'Солнце' : [s, '#f5e238'],
    'Меркурий' : [0.382, '#eb9234'],
    'Венера' : [0.949, '#f5cf38'],
    'Земля' : [1, '#38dcf5'],
    'Марс' : [0.53, '#f25c11'],
    'Юпитер' : [11.2, '#f5d922'],
    'Сатурн' : [9.41, '#c9713e'],
    'Уран' : [3.98, '#22cef5'],
    'Нептун' : [3.81, '#225af5'],
    'Плутон' : [0.186, '#905ae0']
    }

x = -2*s*r-300
y = 0
for elem in planets:
    x += r*planets[elem][0] + 30
    planet(r*planets[elem][0], elem, x, y, planets[elem][1])
    x += r*planets[elem][0] + 30

turtle.exitonclick()
'''


# 14.3.13
'''
Напишите программу, которая рисует знак STOP
'''
'''
import turtle

def octaedr(a0=50, x0=0, y0=0, color0='black'):
    angle = 360/8
    o = turtle.Turtle()
    o.hideturtle()
    o.speed(0)
    o.up()
    o.goto(x0, y0)
    # o.down()
    o.fillcolor(color0)
    o.begin_fill()
    o.fd(a0/2)
    o.left(angle)
    for _ in range(7):
        o.fd(a0)
        o.left(angle)
    o.fd(a0/2)
    o.end_fill()

a = 150
shift = a/20
x = 0
y = -(a+2*a/(2**0.5))/2
k = 0.8
for color in ['black', 'white', 'red']:
    octaedr(a, x, y, color)
    y += 1.25*shift
    a -= shift

turtle.hideturtle()
turtle.speed(9)
turtle.up()
turtle.goto(0, -a*k/2)
turtle.pencolor('white')
turtle.write('STOP', False, 'center', ('Arial', int(a*k)))

turtle.exitonclick()
'''


# 14.3.14
'''
Напишите программу, которая рисует силуэты многоэтажек по образцу. Разделите программу на функции:

рисования контуров зданий;
рисования нескольких окон в зданиях;
рисования случайно разбросанных звезд в виде точек (убедитесь, что звезды появляются на небе, а не на зданиях).
'''
'''
import turtle, random

#draw stars
def stars():
    color0 = '#f5ec42'
    size_min = 1
    size_max = 4
    coord_min = -300
    coord_max = 300
    n = 20
    for _ in range(n):
        turtle.tracer(0, 0)
        s = turtle.Turtle()
        s.hideturtle()
        s.up()
        x0, y0 = [random.uniform(coord_min, coord_max) for _ in range(2)]
        r0 = random.uniform(size_min, size_max)
        s.goto(x0, y0)
        s.fillcolor(color0)
        s.begin_fill()
        s.circle(r0)
        s.end_fill()
    turtle.update()

# draw building
def building(x0=0, y0=0, w0=50, h0=100):
    color0 = '#2a4087'
    b = turtle.Turtle()
    b.hideturtle()
    b.speed(9)
    b.up()
    b.goto(x0, y0)
    b.down()
    b.fillcolor(color0)
    b.begin_fill()
    b.goto(x0, y0+h0)
    b.goto(x0+w0, y0+h0)
    b.goto(x0+w0, y0)
    b.end_fill()

# draw window
def window(x0=0, y0=0, width0=0):
    color0 = '#f5ec42'
    w = turtle.Turtle()
    w.up()
    w.goto(x0, y0)
    w.down()
    w.fillcolor(color0)
    w.begin_fill()
    for _ in range(4):
        w.fd(width0)
        w.left(90)
    w.end_fill()


turtle.Screen().bgcolor('#343752')

stars()

h_min = 1
h_max = 15
window_w = 20
x = -200
y = -200

# draw buldings with windows
length = 0
while length < 600:
    w = random.randrange(2*window_w, 3*2*window_w, window_w*1.5)
    h = random.randrange(h_min*2*window_w, h_max*2*window_w, window_w*1.5)
    building(x, y, w, h)
    windows_number = random.randint(0, int(w*h/window_w**2)//10)
    if windows_number > 0:
        for _ in range(windows_number):
            x_w = random.randrange(x+window_w*0.5, x+w-window_w*0.5, window_w*1.5)
            y_w = random.randrange(y+window_w*0.5, y+h-window_w*0.5, window_w*1.5)
            window(x_w, y_w, window_w)
    x += w
    length += w

turtle.exitonclick()
'''


# 14.3.15
'''
Напишите программу, которая рисует изображение сердца
x = 128*sin(t)**3
y = 8*(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t) - 5)
0 <= t <= 2pi
Примечание 1. Изменяйте значение параметра t с маленьким шагом, равным 0.01
Примечание 2. Для перемещения черепашки в заданную точку используйте команду goto(x, y)
'''
'''
import turtle, math

heart = turtle.Turtle()
heart.speed(9)
color = '#e30e35'
heart.fillcolor(color)
heart.pencolor(color)
turtle.Screen().bgcolor('black')
heart.begin_fill()
for t in range(0, 360+1):
    x = 128*math.sin(math.radians(t))**3
    y = 8*(13*math.cos(math.radians(t))-5*math.cos(2*math.radians(t))-2*math.cos(3*math.radians(t))-math.cos(4*math.radians(t)) - 5)
    heart.goto(x, y)
heart.end_fill()

turtle.exitonclick()
'''


#14.3.16
'''
Напишите программу, которая по нажатию на левую кнопку мыши рисует звезду в месте клика. Фон изображения должен быть черным, при этом звезды могут иметь разные размеры, цвета и иметь разное количество сторон.
'''
'''
# v1
import turtle, random
turtle.Screen().bgcolor('black')
turtle.Screen().colormode(255)
a = 25

def star_random(x0=0, y0=0):
    length0 = 200#random.randint(5, 50)
    color0 = [random.randint(0, 255) for _ in range(3)]
    n0 = random.randint(2, 9)
    #alfa0 = 360/n0
    turtle.Screen().tracer(2, 5)
    s = turtle.Turtle()
    s.up()
    s.goto(x0, y0)
    s.down()
    s.hideturtle()
    s.setheading(random.randint(0, 360))
    s.speed(2)
    s.fillcolor(color0)
    s.pencolor(color0)
    s.begin_fill()
    if n0 == 2:
        for _ in range(2):
            s.fd(length0)
            s.left(30)
            s.fd(length0)
            s.left(30+120)
    elif n0 == 3:
        for _ in range(3):
            s.fd(length0)
            s.left(30+360/n0)
            s.fd(length0)
            s.right(30)
    elif n0 == 4:
        for _ in range(4):
            s.fd(length0)
            s.left(60 + 360/n0)
            s.fd(length0)
            s.right(60)
    elif n0 > 4:
        for _ in range(n0):
            s.fd(length0)
            s.left(360/n0**0.7 + 360/n0)#(2*alfa0)
            s.fd(length0)
            s.right(360/n0**0.7)#(alfa0)
    s.end_fill()
    turtle.update()

def left_click(x, y):
    star_random(x, y)

# turtle.Screen().onclick(left_click)
# turtle.Screen().listen()

while True:
    star_random()

turtle.done()
'''


# v2
import turtle, random, time
turtle.Screen().colormode(255)
turtle.Screen().bgcolor('black')
turtle.tracer(0, 0)

s = turtle.Turtle()
s.hideturtle()

def star_random(x0=0, y0=0):
    color0 = [random.randint(0, 255) for _ in range(3)]
    n0 = random.randint(3, 7)
    alfa0 = 360/n0
    k0 = random.randint(18, 22)
    size0 = random.randint(45, 50)
    s.up()
    s.goto(x0, y0)
    s.setheading(random.randint(0, 360))
    s.pencolor(color0)
    s.fillcolor(color0)
    s.down()
    s.begin_fill()
    for _ in range(n0):
        s.fd(size0)
        s.left(n0*k0 + alfa0)
        s.fd(size0)
        s.right(n0*k0)
    s.end_fill()
    turtle.update()

# turtle.Screen().listen()
# turtle.Screen().onclick(star_random)

def clear(x, y):
    s.reset()

turtle.Screen().listen()
turtle.Screen().onclick(clear)
flag = 0
while True:
    
    x, y = [random.randint(-300, 300) for _ in range(2)]
    time.sleep(0.2)
    star_random(x, y)
    turtle.update()
    flag += 1



turtle.done()
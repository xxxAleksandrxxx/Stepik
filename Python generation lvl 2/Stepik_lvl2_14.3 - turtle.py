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

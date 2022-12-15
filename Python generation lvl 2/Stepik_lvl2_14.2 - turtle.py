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
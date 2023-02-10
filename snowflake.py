import random
import turtle
t=turtle.Turtle()
turtle.Screen().bgcolor('black')
colorname = "cyan"
t.color(colorname)
t.penup()
t.forward(90)
t.left(45)
t.pendown()
t.hideturtle()
t.width(2)
t.speed(3)

def branch():
    for a in range(3):
        for b in range(3):
            t.forward(30)
            t.backward(30)
            t.right(45)
        t.left(90)
        t.backward(30)
        t.left(45)
    t.right(90)
    t.forward(90)

for c in range(8):
    branch()
    t.left(45)

turtle.done()

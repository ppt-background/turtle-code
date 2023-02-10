import turtle
t = turtle.Turtle()
t.speed(0)
t.getscreen().bgcolor("black")
t.color("coral")
t.width(2)
t.penup()
t.goto((-200, 50))
t.pendown()
def star(turtle, size):
	if size <= 10:
		return
	else:
		for i in range(5):
			turtle.forward(size)
			star(turtle, size/3)
			turtle.left(216)


star(t, 360)
turtle.done()

import turtle
colors = ['orange', 'yellow', 'red', 'coral', 'pink', 'purple']
t= turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
for x in range(2000):
	t.pencolor(colors[x%6])
	t.width(x/100 + 1)
	t.forward(x)
	t.left(59)
turtle.done()
t.speed(10)
turtle.bgcolor("black")
for x in range(2000):
	t.pencolor(colors[x%6])
	t.width(x/100 + 1)
	t.forward(x)
	t.left(59)
turtle.done()

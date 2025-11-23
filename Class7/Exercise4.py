import turtle

turtle.bgcolor("black")
turtle.pencolor("white")
turtle.speed(0)
turtle.shape("circle")
turtle.shapesize(1)
def forward(a):
    turtle.forward(a)
def left(a):
    turtle.left(a)
def right(a):
    turtle.right(a)
turtle.penup()
turtle.goto(150,-150)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.pendown()
for i in range(4):
    forward(100)
    right(90)
turtle.end_fill()
forward(50)
left(90)
turtle.fillcolor("white")
turtle.speed(5)
for i in range(90):
    left(1)
    forward(3.7)
turtle.shapesize(0.5)
turtle.color("yellow")
for i in range(1, 5):
    turtle.shapesize(i)
turtle.color("orange")
turtle.delay(0)
turtle.shapesize(1)
turtle.speed(0)
turtles = []
for i in range(36):
    turtles.append(turtle.clone())
    turtles[i].right(i*10)
for j in range(10):
    for i in range(36):
        turtles[i].forward(20)


turtle.done()

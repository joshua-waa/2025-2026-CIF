import turtle
turtle.speed(5)
def forward(a):
    turtle.forward(a)
def left(a):
    turtle.left(a)
def right(a):
    turtle.right(a)
turtle.penup()
right(90)
forward(150)
right(90)
forward(50)
right(180)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.pendown()
for i in range(4):
    forward(100)
    right(90)
turtle.end_fill()

turtle.done()

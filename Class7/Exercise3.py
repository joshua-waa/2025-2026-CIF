import turtle
import random

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
turtle.color("orange")
turtle.pensize(10)
t1=turtle.clone()
t2=turtle.clone()
t3=turtle.clone()
t4=turtle.clone()
t5=turtle.clone()
t6=turtle.clone()
turtle.color("yellow")
for i in range(1, 5):
    turtle.shapesize(i)

t1.right(random.randint(1,360))
t2.right(random.randint(1,360))
t3.right(random.randint(1,360))
t4.right(random.randint(1,360))
t5.right(random.randint(1,360))
t6.right(random.randint(1,360))
t1.forward(100)
t2.forward(100)
t3.forward(100)
t4.forward(100)
t5.forward(100)
t6.forward(100)


turtle.done()

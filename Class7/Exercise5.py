import turtle

# Setup
turtle.bgcolor("black")
t = turtle.Turtle()
t.pencolor("white")
t.speed(0)
t.shape("circle")
t.shapesize(0.5)

for i in range(10101010100):
    t.forward(i/2)
    t.right(50)

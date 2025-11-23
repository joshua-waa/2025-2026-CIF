import turtle
t=turtle.Turtle()
c=t.clone()
c.shape("arrow")
t.shape("circle")
for i in range(4):
    t.forward(100)
    c.forward(100)
    t.right(90)
    c.left(90)
turtle.done()

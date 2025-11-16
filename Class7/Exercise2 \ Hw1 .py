import turtle
turtle.speed(0)
def forward(a):
    turtle.forward(a)
def left(a):
    turtle.left(a)
def right(a):
    turtle.right(a)
sides=int(input("How many sides?"))
for i in range(3):
    forward(100)
    right(180-((sides-2)*180/sides))
turtle.done()

import turtle
from turtle import *

t = Turtle()

t.pu()
t.goto(100,0)
t.pd()

for _ in range(2):
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(500)


t.pu()
t.goto(100,150)
t.pd()

t.left(180)
t.forward(500)
t.fillcolor("red")
t.begin_fill()
t.right(90)
t.forward(150)
t.right(90)
t.fd(500)
t.right(90)
t.fd(150)
t.end_fill()


mainloop()
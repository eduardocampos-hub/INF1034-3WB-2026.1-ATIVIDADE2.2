
import turtle
from turtle import *
from time import sleep
t = Turtle()


def retangulo_horizontal(cor):
    t.fillcolor(cor)
    t.begin_fill()
    t.right(90)
    t.fd(100)
    t.left(90)
    t.fd(500)
    t.lt(90)
    t.fd(100)
    t.left(90)
    t.fd(500)
    t.left(90)
    t.fd(100)
    t.lt(90)
    t.end_fill()

def bandeiraAlemanha():
    retangulo_horizontal("black")
    retangulo_horizontal("red")
    retangulo_horizontal("yellow")

bandeiraAlemanha()



def ret_hor():
    t.right(90)
    t.fd(100)
    t.left(90)
    t.fd(500)
    t.lt(90)
    t.fd(100)
    t.left(90)
    t.fd(500)
    t.left(180)



# for _ in range(2):
#     t.left(90)
#     t.forward(300)
#     t.left(90)
#     t.forward(500)

# t.fillcolor("red")
# t.begin_fill()
# t.left(90)
# t.fd(100)
# t.left(90)
# t.fd(500)
# t.left(90)
# t.fd(100)
# t.end_fill()
# t.rt(180)
# t.fd(100)
# def bandeirash(color1,color2,color3):
#     t.pu()
#     t.goto(0,0)
#     t.pd()

    
#     for _ in range(2):
#         t.left(90)
#         t.forward(300)
#         t.left(90)
#         t.forward(500)

#     t.fillcolor(color1)
#     t.begin_fill()
#     t.left(90)
#     t.fd(100)
#     t.left(90)
#     t.fd(500)
#     t.left(90)
#     t.fd(100)
#     t.end_fill()

#     t.left(90)
#     t.fd(500)
#     t.left(90)
#     t.fd(100)

#     t.fillcolor(color2)
#     t.begin_fill()
#     for _ in range(2):
#         t.fd(100)
#         t.left(90)
#         t.forward(500)
#         t.left(90)
#     t.end_fill()

#     t.fd(100)
#     t.fillcolor(color3)
#     t.begin_fill()
#     for _ in range(2):
#         t.fd(100)
#         t.left(90)
#         t.forward(500)
#         t.left(90)
#     t.end_fill()
#     t.right(90)
#     return

mainloop()
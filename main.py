import turtle
from turtle import *
from time import sleep
t = Turtle()
t.speed(20)
t.pu()
t.goto(100,0)
t.pd()

#bandeira 1

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

sleep(2)
t.clear()

t.pu()
t.goto(0,0)
t.pd()


def bandeiras(color1, color2, color3):
    t.pu()
    t.goto(-100,100)
    t.pd()

    t.right(90)
    t.fillcolor(color1)
    t.begin_fill()
    t.right(90)
    t.fd(300)
    t.right(90)
    t.fd(167)
    t.right(90)
    t.fd(300)
    t.end_fill()
    
    t.right(90)
    t.fillcolor(color2)
    t.begin_fill()
    t.right(90)
    t.fd(300)
    t.right(90)
    t.fd(167)   
    t.right(90)
    t.fd(300)
    t.end_fill()

    t.right(90)
    t.fillcolor(color3)
    t.begin_fill()
    t.right(90)
    t.fd(300)
    t.right(90)
    t.fd(167)
    t.right(90)
    t.fd(300)
    t.end_fill()
    return
#bandeira 2

bandeiras("green","white","green")

sleep(2)
t.clear()
#bandeira3

bandeiras("black","yellow","red")

sleep(2)
t.clear()
#bandeira 4

bandeiras("blue","white","red")

sleep(2)
t.clear()
#bandeira 5

bandeiras("green", "white","dark red")

sleep(2)
t.clear()
#bandeira 6 

bandeiras("green","white","orange")

sleep(2)
t.clear()

#bandeira 7

bandeiras("orange","white","green")

sleep(2)
t.clear()

#bandeira 8

bandeiras("green","yellow","red")

sleep(2)
t.clear()

#bandeira 9

bandeiras("dark blue","yellow","red")

sleep(2)
t.clear()

#bandeira 10

bandeiras("red","yellow","green")

sleep(2)
t.clear()

#bandeiras horizontais-------------------------------------------------------------------
def bandeirash(color1,color2,color3):
    t.pu()
    t.goto(0,0)
    t.pd()

    
    for _ in range(2):
        t.left(90)
        t.forward(300)
        t.left(90)
        t.forward(500)

    t.fillcolor(color1)
    t.begin_fill()
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(500)
    t.left(90)
    t.fd(100)
    t.end_fill()

    t.left(90)
    t.fd(500)
    t.left(90)
    t.fd(100)

    t.fillcolor(color2)
    t.begin_fill()
    for _ in range(2):
        t.fd(100)
        t.left(90)
        t.forward(500)
        t.left(90)
    t.end_fill()

    t.fd(100)
    t.fillcolor(color3)
    t.begin_fill()
    for _ in range(2):
        t.fd(100)
        t.left(90)
        t.forward(500)
        t.left(90)
    t.end_fill()
    t.right(90)
    return
#bandeira 11

t.left(90)
bandeirash("yellow","red","black")

sleep(2)
t.clear()

#bandeira 12

bandeirash("dark blue","white","red")

sleep(2)
t.clear()

#bandeira 13

bandeirash("red","green","white")

sleep(2)
t.clear()

#bandeira 14

bandeirash("red","dark blue","white")

sleep(2)
t.clear()

#bandeira 15

bandeirash("black","white","red")

sleep(2)
t.clear()

#bandeira 16

bandeirash("blue","yellow","green")

sleep(2)
t.clear()

#bandeira 17

bandeirash("white","black","blue")

sleep(2)
t.clear()

#bandeira 18

bandeirash("yellow","dark blue","red")

sleep(2)
t.clear()

#bandeira 19

bandeirash("yellow","green","red")

sleep(2)
t.clear()

#bandeira 20

bandeirash("red","white","green")

sleep(2)
t.clear()

mainloop()

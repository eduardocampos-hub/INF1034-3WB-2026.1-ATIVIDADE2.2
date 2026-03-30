import turtle
from turtle import *
from time import sleep
t = Turtle()

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



def desenha_retangulo(larg,alt,cor):
    t.right(90)
    t.fillcolor(cor)
    t.begin_fill()
    t.right(90)
    t.fd(larg)
    t.right(90)
    t.fd(alt)
    t.right(90)
    t.fd(300)
    t.end_fill()
    return



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
def bandeira_nigeria():   
    t.pu()
    t.goto(-100,100)
    t.pd()
    desenha_retangulo(300,167,"green")
    desenha_retangulo(300,167,"white")
    desenha_retangulo(300,167,"green")
    sleep(2)
    t.clear()
bandeira_nigeria()
#bandeira3
def bandeira_belgica():   
    t.pu()
    t.goto(-100,100)
    t.pd()
    desenha_retangulo(300,167,"black")
    desenha_retangulo(300,167,"yellow")
    desenha_retangulo(300,167,"red")
    sleep(2)
    t.clear()
bandeira_belgica()
#bandeira 4
def bandeira_franca():   
    t.pu()
    t.goto(-100,100)
    t.pd()
    desenha_retangulo(300,167,"blue")
    desenha_retangulo(300,167,"white")
    desenha_retangulo(300,167,"red")
    sleep(2)
    t.clear()
bandeira_franca()
#bandeira 5
def bandeira_italia():   
    t.pu()
    t.goto(-100,100)
    t.pd()
    desenha_retangulo(300,167,"green")
    desenha_retangulo(300,167,"white")
    desenha_retangulo(300,167,"dark red")
    sleep(2)
    t.clear()
bandeira_italia()
#bandeira 6 
def bandeira_irlanda():   
    t.pu()
    t.goto(-100,100)
    t.pd()
    desenha_retangulo(300,167,"green")
    desenha_retangulo(300,167,"white")
    desenha_retangulo(300,167,"orange")
    sleep(2)
    t.clear()
bandeira_irlanda()
#bandeira 7
def bandeira_costa_do_marfin():   
    t.pu()
    t.goto(-100,100)
    t.pd()
    desenha_retangulo(300,167,"orange")
    desenha_retangulo(300,167,"white")
    desenha_retangulo(300,167,"green")
    sleep(2)
    t.clear()
bandeira_costa_do_marfin()
#bandeira 8
def bandeira_mali():   
    t.pu()
    t.goto(-100,100)
    t.pd()
    desenha_retangulo(300,167,"green")
    desenha_retangulo(300,167,"yellow")
    desenha_retangulo(300,167,"red")
    sleep(2)
    t.clear()
bandeira_mali()
#bandeira 9
def bandeira_romania():   
    t.pu()
    t.goto(-100,100)
    t.pd()
    desenha_retangulo(300,167,"dark blue")
    desenha_retangulo(300,167,"yellow")
    desenha_retangulo(300,167,"red")
    sleep(2)
    t.clear()

bandeira_romania()
#bandeira 10
def bandeira_guine():   
    t.pu()
    t.goto(-100,100)
    t.pd()
    desenha_retangulo(300,167,"red")
    desenha_retangulo(300,167,"yellow")
    desenha_retangulo(300,167,"green")
    sleep(2)
    t.clear()

bandeira_guine()
#bandeiras horizontais-------------------------------------------------------------------

def retangulo_horizontal(cor):
    t.fillcolor(cor)
    t.begin_fill()
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(500)
    t.left(90)
    t.fd(100)
    t.end_fill()
    t.rt(180)
    t.fd(100)

def bandeira_alemanha():
    retangulo_horizontal("yellow")
    retangulo_horizontal("red")
    retangulo_horizontal("black")
    sleep(2)
    t.clear()

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

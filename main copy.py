import turtle
from turtle import *
from time import sleep
t = Turtle()
t.speed(10)
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
    t.pu()
    t.goto(0,0)
    t.pd()
    retangulo_horizontal("yellow")
    retangulo_horizontal("red")
    retangulo_horizontal("black")
    sleep(2)
    t.clear()
t.right(90)
bandeiraAlemanha()

def bandeiraHolanda():
    t.pu()
    t.goto(0,0)
    t.pd()
    retangulo_horizontal("dark blue")
    retangulo_horizontal("white")
    retangulo_horizontal("red")
    sleep(2)
    t.clear()
bandeiraHolanda()

def bandeiraHungria():
    t.pu()
    t.goto(0,0)
    t.pd()
    retangulo_horizontal("red")
    retangulo_horizontal("green")
    retangulo_horizontal("white")
    sleep(2)
    t.clear()

bandeiraHungria()

def bandeiraRussia():
    t.pu()
    t.goto(0,0)
    t.pd()
    retangulo_horizontal("red")
    retangulo_horizontal("dark blue")
    retangulo_horizontal("white")
    sleep(2)
    t.clear()

bandeiraRussia()

def bandeiraYemen():
    t.pu()
    t.goto(0,0)
    t.pd()
    retangulo_horizontal("black")
    retangulo_horizontal("white")
    retangulo_horizontal("red")
    sleep(2)
    t.clear()

bandeiraYemen()

def bandeiraGabao():
    t.pu()
    t.goto(0,0)
    t.pd()
    retangulo_horizontal("blue")
    retangulo_horizontal("yellow")
    retangulo_horizontal("green")
    sleep(2)
    t.clear()

bandeiraGabao()

def bandeiraEstonia():
    t.pu()
    t.goto(0,0)
    t.pd()
    retangulo_horizontal("white")
    retangulo_horizontal("black")
    retangulo_horizontal("blue")
    sleep(2)
    t.clear()

bandeiraEstonia()

def bandeiraArmenia():
    t.pu()
    t.goto(0,0)
    t.pd()
    retangulo_horizontal("yellow")
    retangulo_horizontal("dark blue")
    retangulo_horizontal("red")
    sleep(2)
    t.clear()

bandeiraArmenia()

def bandeiraLithuania():
    t.pu()
    t.goto(0,0)
    t.pd()
    retangulo_horizontal("red")
    retangulo_horizontal("green")
    retangulo_horizontal("yellow")
    sleep(2)
    t.clear()

bandeiraLithuania()

def bandeiraBulgaria():
    t.pu()
    t.goto(0,0)
    t.pd()
    retangulo_horizontal("red")
    retangulo_horizontal("white")
    retangulo_horizontal("green")
    sleep(2)
    t.clear()

bandeiraBulgaria()




mainloop()

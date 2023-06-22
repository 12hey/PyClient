import os
from time import sleep
import turtle as t

b = 0
def pyclient():
    t.ht()
    t.penup()
    t.setup(500,500)
    t.bgcolor('Black')
    t.pencolor('White')
    t.goto(-300,100)
    t.write('PyClient',font=('微软雅黑',100))
    t.goto(240, 120)
    t.write('V4', font=('微软雅黑', 30))
    t.pencolor('White')
    t.goto(-250,-100)
    t.pensize(15)
    for i in range(150):
        t.pendown()
        t.forward(3)
    t.penup()
    t.pencolor('Black')
    t.goto(-250, -100)
    t.pensize(13)
    for i in range(150):
        t.pendown()
        t.forward(3)
    t.penup()
    t.pencolor('White')
    t.goto(-250, -100)
    t.pensize(11)
    for i in range(900):
        t.pendown()
        t.forward(0.5)
    try:
        with open("bdl.txt", 'r') as file:
            b = file.read()
        with open("cps.txt", 'r') as file:
            b = file.read()
        with open("dl.txt", 'r') as file:
            b = file.read()
        with open("cs.txt", 'r') as file:
            b = file.read()
        with open("Maxms.txt", 'r') as file:
            b = file.read()
        with open("Minms.txt", 'r') as file:
            b = file.read()
    except:
        t.penup()
        t.goto(-250,-130)
        t.write("Error line 3 [OSError]",font=('微软雅黑',10))
        try:
            with open("strAC_4.08_settings.exe", 'r') as file:
                file.read()
        except:
            t.penup()
            t.goto(-200,-90)
            t.write("Error line 3 [OSError]:Found strAC_4.08_settings.exe", font=('微软雅黑', 10))
            sleep(10)
            exit()
        os.system("start strAC_4.08_settings.exe")
    t.down()
pyclient()
sleep(20)
exit()
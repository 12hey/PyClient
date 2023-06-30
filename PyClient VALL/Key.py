import pyautogui
import os
from time import sleep,time

t = 0.00
tt = 0.000
dlsq = 0
pag.PAUSE = 0.001
newcs = 0
js = 0
tooxh = 0
Max = 0.05
Min = 0.01

def key():
    try:
        with open("PyClient V4.py") as file:
           file.read()
    except:
        os.system("start PyClient V4.py")
    b = input('\n请输入您需要输入的字符：')
    t = time()
    with open("cs.txt",'r') as file:
        h = file.read()
    with open("bdl.txt",'r') as file:
        p = file.read()
    if p == 'y':
        js = 0

        with open("Maxms.txt",'r') as file:
            Max = file.read()
        with open("Minms.txt",'r') as file:
            Min = file.read()
        Max = float(Max)
        Min = float(Min)
        c = h
        c = int(c)
        print('请注意，您需要在5秒内切换到需要输入的窗口。')
        sleep(5)
        print('开始工作！')
        r = 0.01
        r = float(r)
        while True:
            pag.press(b)
            r = uniform(Min, Max)
            js = js + 1
            js = int(js)
            if js > c:
                break
            else:
                pag.press(b)
        tt = time()
        newtime = tt - t - 5
        newtime = str(newtime)
        print("完成，用时" + newtime + '秒')
    else:
        js = 0
        newcps = 0.1
        cps = 0.01
        with open("cps.txt",'r') as file:
            cps = file.read()
        cps = float(cps)
        newcps = float(newcps)
        newcps = 1 / cps
        c = h
        c = int(c)
        print('请注意，您需要在5秒内切换到需要输入的窗口。')
        sleep(5)
        print('开始工作！')
        e = time()
        while True:
            pag.press(b)
            sleep(newcps)
            if js > c:
                break
            else:
                pag.press(b)
        tt = time()
        newtime = tt - t - 5
        newtime = str(newtime)
        print("完成，用时" + newtime + '秒')
key()
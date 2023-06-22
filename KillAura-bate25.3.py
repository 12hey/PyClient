from random import randint,uniform
from time import sleep, time

import turtle as tur
import pyautogui
import pyautogui as pag
from tkinter import *
from tkinter import messagebox
import pynput.mouse as pm
import threading

t = 0.00
tt = 0.000
dlsq = 0
pag.PAUSE = 0.001
newcs = 0
js = 0
tooxh = 0
Max = 0.05
Min = 0.01
with open("bdl.txt",'w') as file:
    file.write("1")
with open("cps.txt",'w') as file:
    file.write("1")
with open("dl.txt",'w') as file:
    file.write("1")
with open("cs.txt",'w') as file:
    file.write("1")
with open("Maxms.txt",'w') as file:
    file.write("1")

with open("Minms.txt",'w') as file:
    file.write("1")
messagebox.showinfo("帮助PyClient","目前开发团队只有1个人，所以我由衷的请有Python开发经验的程序员加入我们.\n"
                    "我们收费吗？PyClient是完全免费的，代码开源。下载PyClient请认准github:https://github.com/12hey/PyClient.git(外国网点，连接稍慢)")
vb = pyautogui.prompt(text='请选择模式：\n模式1，键盘连点.\n模式2,鼠标连点(AC搭路已和该选项合并.\n模式4：杀戮光环\n模式5：'
                           '预设配置\n模式6：自动输入，防挂机踢出',title='strAC_Lunch_Run', default='')
vb = int(vb)

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
def notbeaac():
    messagebox.showinfo("提示",'AC连点如果你按住鼠标就开始连点，放开就停止')
    global out
    maxcs = pyautogui.prompt(text='设置最大点击次数',title='strAC_Lunch_Run', default='')
    mincs = pyautogui.prompt(text='设置最小点击次数', title='strAC_Lunch_Run', default='')
    while True:
        for i in range(1,999999999999999999999999999):
            out = 0.1
            def on_click(x, y, button, pressed):
                # 监听鼠标点击
                if pressed:
                    print(button)
                    if botton == Button.left:
                        zz = randint(mincs,maxcs)
                        out = 1 / zz
                        for i in range(1, zz):
                            pyautogui.Click()
                            sleep(out)
                    else:
                        if botton == Button.right:
                            zz = randint(mincs,maxcs)
                            out = 1 / zz
                            for i in range(1, zz):
                                pyautogui.rightClick()
                                sleep(out)
                        else:
                            print("停止操作")
                if not pressed:
                    return False

            def ls_k_thread():
                while (1):
                    with pm.Listener(on_click=on_click) as pmlistener:
                        pmlistener.join()

            def analyse_pic_thread():
                r = threading.Thread(target=ls_k_thread)
                r.start()

            analyse_pic_thread()


def dl():
    messagebox.showinfo("提示", 'AC搭路将在3秒后开始！')
    sleep(3)
    global out
    with open("cps.txt", 'r') as file:
        w = file.read()
    with open("cs.txt", 'r') as file:
        cs = file.read()
    pcl = 2
    mq = 0
    ctr = 0
    while True:
        out = 0.1
        out = uniform(10, 18)
        out = 1 / out
        out = out / 2 - 0.02
        print(out)
        pyautogui.rightClick()
        pyautogui.rightClick()
        sleep(out)
        mq = mq + 1
        pyautogui.rightClick()
        ctr = ctr + 1
        cs = int(cs)
def killaura():
    width,height = pyautogui.size()  # 屏幕的宽度和高度
    with open("cps.txt",'r') as file:
        client = file.read()
    gg = 0
    client = int(client)
    while gg < client:
        pro = randint(0, height)
        pyc = randint(width,0)
        pyautogui.dragTo(pro, prc)
        click()
        gg = gg+1
def pyclient():
    jg = pyautogui.prompt(text='请写出你要左(z)\n还是右(y)\n还是上(up)\n或下(down)\n输入exit退出',
                          title='strAC_Lunch_Run', default='')
    po = time()
    po = str(po)
    while True:
        if jg != "exit":
            with open(""+po,'w') as file:
                file.write(jg)
            jg = pyautogui.prompt(text='请写出你要左(z)\n还是右(y)\n还是上(up)\n或下(down)\n输入exit退出',
                                  title='strAC_Lunch_Run', default='')
            pc = pyautogui.prompt(text='请写出你要前进多少步',title='strAC_Lunch_Run', default='')
            with open(""+po+"#2", 'w') as file:
                file.write(pc)
            po = time()
            po = str(po)
        else:
            exit()
if vb == 1:
    ac = Tk()
    ac.title("strAC_Lunch_Run")
    label = Label(ac,text="strAC_Lunch_Run",font=("宋体",25),fg="red")
    entry = Entry(ac,font=("宋体",10),fg="red")
    entry.grid(row=0,column=1)
    label.grid()
    button = Button(ac,text="New AC",font=("微软雅黑",20),fg="blue",command=key)
    button.grid(row=1,column=1)
    # 窗口大小
    ac.geometry("600x450")
    # 显示窗口
    ac.mainloop()
else:
    if vb == 2:
        ac = Tk()
        ac.title("strAC_Lunch_Run")
        label = Label(ac, text="strAC_Lunch_Run", font=("宋体", 25), fg="red")
        entry = Entry(ac, font=("宋体", 10), fg="red")
        entry.grid(row=0, column=1)
        label.grid()
        button = Button(ac, text="New AC", font=("微软雅黑", 20), fg="blue", command=notbeaac)
        button.grid(row=1, column=1)
        # 窗口大小
        ac.geometry("600x450")
        # 显示窗口
        ac.mainloop()
    else:
        if vb == 4:
            ac = Tk()
            ac.title("strAC_Lunch_Run")
            label = Label(ac, text="strAC_Lunch_Run", font=("宋体", 25), fg="red")
            entry = Entry(ac, font=("宋体", 10), fg="red")
            entry.grid(row=0, column=1)
            label.grid()
            button = Button(ac, text="New AC", font=("微软雅黑", 20), fg="blue", command=killaura)
            button.grid(row=1, column=1)
            # 窗口大小
            ac.geometry("600x450")
            # 显示窗口
            ac.mainloop()
        else:
            if vb == 5:
                ac = Tk()
                ac.title("strAC_Lunch_Run")
                label = Label(ac, text="strAC_Lunch_Run", font=("宋体", 25), fg="red")
                entry = Entry(ac, font=("宋体", 10), fg="red")
                entry.grid(row=0, column=1)
                label.grid()
                button = Button(ac, text="New AC", font=("微软雅黑", 20), fg="blue", command=pyclient)
                button.grid(row=1, column=1)
                # 窗口大小
                ac.geometry("600x450")
                # 显示窗口
                ac.mainloop()
            else:
                messagebox.showinfo("帮助PyClient","目前开发团队只有1个人，所以我由衷的请有Python开发经验的程序员加入我们.\n"
                "我们收费吗？PyClient是完全免费的，代码开源。遇到要收费的PyClient,你大概是遇到了拿我们公开的源代码收费的人\n"
                "所以，下载PyClient请认准github(外国网点，连接稍慢)")
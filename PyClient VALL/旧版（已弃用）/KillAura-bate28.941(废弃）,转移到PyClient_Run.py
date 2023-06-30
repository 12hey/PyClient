import os
from tkinter import *
from tkinter import messagebox


messagebox.showinfo("帮助PyClient","目前开发团队只有1个人，所以我由衷的请有Python开发经验的程序员加入我们.\n"
                    "我们收费吗？PyClient是完全免费的，代码开源。下载PyClient请认准github:https://github.com/12hey/PyClient.git(外国网点，连接稍慢)")
'''vb = pyautogui.prompt(text='请选择模式：\n模式1，键盘连点.\n模式2,鼠标连点(AC搭路已和该选项合并.\n模式4：杀戮光环\n模式5：'
                           '预设配置\n模式6：自动输入，防挂机踢出.\n模式7：瞬移',title='strAC_Lunch_Run', default='')
vb = int(vb)'''


import tkinter as tk

def button1_clicked():
    os.system("start KillAura.py")

def button2_clicked():
    os.system("start AimBot.py")

def button3_clicked():
    os.system("start openproject.py")

def button4_clicked():
    os.system("start Tp+.py")

def keyclick():
    os.system("start key.py")

def run():
    os.system("start PyClient_V4.py")
window = tk.Tk()
window.title("Black Background Window")
window.geometry("400x200")
window.configure(bg="black")

button_frame = tk.Frame(window, bg="black")
button_frame.pack(pady=30)

button1 = tk.Button(button_frame, text="杀\n戮\n光\n环", command=button1_clicked, bg="white", fg="black", bd=2, relief="solid", width=5, height=4)
button1.grid(row=0, column=0, padx=10)

button2 = tk.Button(button_frame, text="自\n动\n瞄\n准", command=button2_clicked, bg="white", fg="black", bd=2, relief="solid", width=5, height=4)
button2.grid(row=0, column=1, padx=10)

button3 = tk.Button(button_frame, text="自\n动\n连\n点", command=button3_clicked, bg="white", fg="black", bd=2, relief="solid", width=5, height=4)
button3.grid(row=0, column=2, padx=10)

button4 = tk.Button(button_frame, text="瞬\n移", command=button3_clicked, bg="white", fg="black", bd=2, relief="solid", width=5, height=4)
button4.grid(row=0, column=3, padx=10)

run = tk.Button(button_frame, text="运\n行\n检\n查", command=run, bg="white", fg="black", bd=2, relief="solid", width=5, height=4)
run.grid(row=0, column=4, padx=10)

run = tk.Button(button_frame, text="键\n盘\n连\n点", command=keyclick, bg="white", fg="black", bd=2, relief="solid", width=5, height=4)
run.grid(row=0, column=5, padx=10)



window.mainloop()
from pynput.mouse import Listener, Button
from time import sleep, time
import pyautogui

t = 0.00
tt = 0.000
dlsq = 0
pag.PAUSE = 0.001
newcs = 0
js = 0
tooxh = 0
Max = 0.05
Min = 0.01

def openproject():
    # 鼠标点击事件处理函数
    cin = pyautogui.prompt(text="请说出你连点的停顿：",title="Settings Time Out",default='')
    cin = int(cin)
    continuous_clicking = False
    def on_click(x, y, button, pressed):
        if button == Button.left:
            if pressed:
                pyautogui.click()
                sleep(cin)
            else:
                print("stop Click")
        elif button == Button.right:
            if pressed:
                for i in range(1, 20):
                    pyautogui.rightClick()
                    sleep(ce)
            else:
                print("stop Right Click")

    # 创建监听器
    listener = Listener(on_click=on_click)

    # 启动监听器
    listener.start()

    # 运行主循环
    while True:
        pass
while True:
    openproject()
import os
import pyautogui


NO1 = pyautogui.prompt(text='请输入要点击的次数：', title='strAC_4.07_Setting', default='')

with open(r'cs.txt','w') as file:
    file.write(NO1)
    NO2 = pyautogui.prompt(text='是否开启不等量延迟？(y/n)', title='strAC_4.07_Setting', default='')
if NO2 == 'y':
    with open(r"bdl.txt", 'w') as file:
        file.write(NO2)
    NO3 = pyautogui.prompt(text='请输入最大延迟：', title='strAC_4.07_Setting', default='')
    with open(r"Maxms.txt",'w') as file:
        file.write(NO3)
    NO4 = pyautogui.prompt(text='请输入最小延迟：', title='strAC_4.07_Setting', default='')
    with open(r"Minms.txt",'w') as file:
        file.write(NO4)
else:
    with open(r"bdl.txt",'w') as file:
        file.write(NO2)
    NO5 = pyautogui.prompt(text='请输入你要的cps数/s:', title='strAC_4.07_Setting', default='')
    with open(r"cps.txt",'w') as file:
        file.write(NO5)
NO6 = pyautogui.prompt(text='请输入你搭路的方块数:', title='strAC_4.07_Setting', default='')
with open("dl.txt",'w') as file:
    file.write(NO6)
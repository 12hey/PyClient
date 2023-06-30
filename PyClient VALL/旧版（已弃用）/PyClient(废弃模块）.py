import os

def pyclient():
    jg = pyautogui.prompt(text='请写出你要左(z)\n还是右(y)\n还是上(up)\n或下(down)\n输入exit退出',
                          title='strAC_Lunch_Run', default='')
    po = time()
    po = str(po)
    while True:
        if jg != "exit":
            with open(""+po+".txt",'w') as file:
                file.write(jg)
            jg = pyautogui.prompt(text='请写出你要左(z)\n还是右(y)\n还是上(up)\n或下(down)\n输入exit退出',
                                  title='strAC_Lunch_Run', default='')
            pc = pyautogui.prompt(text='请写出你要前进多少步',title='strAC_Lunch_Run', default='')
            with open(""+po+"#2"+".txt", 'w') as file:
                file.write(pc)
            po = time()
            po = str(po)
        else:
            exit()
while True:
    pyclient()
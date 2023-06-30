from mcpi.minecraft import Minecraft
import time

try:
    mc = Minecraft.create()
except ConnectionRefusedError:
    print("网络防火墙拒绝了Python TP+ 模块的更改(ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。)")
    time.sleep(5)
    exit()
while True:
    # 获取玩家当前位置
    player_pos = mc.player.getTilePos()

    sayy = pyautogui.prompt(text='输入将要瞬移到的y坐标：',title='strAC_Lunch_Run_TP+', default='')
    sayx = pyautogui.prompt(text='输入将要瞬移到的x坐标：', title='strAC_Lunch_Run_TP+', default='')
    sayz = pyautogui.prompt(text='输入将要瞬移到的z坐标：', title='strAC_Lunch_Run_TP+', default='')
    try:
        mc.player.setTilePos(sayx, sayy, sayz)
    except ConnectionRefusedError:
        print("网络防火墙拒绝了Python TP+ 模块的更改")
        input()

import os
import pyautogui
import time
from mss import mss

pyautogui.FAILSAFE = False
def killaura():
    open = 0.1
    open = float(open)
    open = pyautogui.prompt(text="请说出你要的间隔时间:",title="Settings Time Out",default='')
    def get_screen():
        with mss() as sct:
            monitor = sct.monitors[0]  # 如果你的Minecraft在第二个显示器上，可以使用monitors[1]，否则使用monitors[0]
            screenshot = sct.grab(monitor)
            return screenshot

    def find_player():
        screenshot = get_screen()

        player_x = 100
        player_y = 200
        return player_x, player_y

    def aim_at_player(player_x, player_y):
        # 获取屏幕尺寸
        screen_width, screen_height = pyautogui.size()

        # 计算玩家的相对坐标
        relative_x = player_x - screen_width / 2
        relative_y = player_y - screen_height / 2

        # 将鼠标移动到玩家的位置
        pyautogui.moveTo(relative_x, relative_y, duration=0.1)
        pyautogui.click()
        pyautogui.click()
        pyautogui.rightClick()

    # 主循环
    while True:
        player_x, player_y = find_player()
        aim_at_player(player_x, player_y)
        open = float(open)
        time.sleep(open)
for i in range(1,100):
    killaura()

import time

import win32api
import win32con

while True:
    print("Was CAPS lock pressed?", win32api.GetAsyncKeyState(win32con.VK_CAPITAL))
    print("Was space pressed?", win32api.GetAsyncKeyState(ord(" ")))
    time.sleep(1)

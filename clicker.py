from operator import truediv

import pyautogui
import time
import keyboard
import threading

clicking = True

def stop_clicking():
    global clicking
    while True:
        if keyboard.is_pressed('esc'):
            clicking = False
            print('Stopped clicking')
            break

def clicker_position():
    x, y = 2100, 500

    while clicking:
        pyautogui.click(x, y)
        time.sleep(0.1)

stop_thread = threading.Thread(target=stop_clicking)
stop_thread.start()

clicker_position()

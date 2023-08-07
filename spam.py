import time
import pyautogui

time.sleep(10)
f = open('span.txt')

for line in f:
    pyautogui.typewrite(line)
    pyautogui.press('enter')

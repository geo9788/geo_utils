import time
import pyautogui as pag
count = 0
sleep = 2
while True:
    count += 1
    if count == 1:
        sleep = 10
    pag.moveTo(33, 222, duration=2)
    pag.click()
    time.sleep(sleep)
    pag.moveTo(33, 333, duration=2)
    pag.click()
    time.sleep(sleep)

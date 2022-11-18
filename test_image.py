import pyautogui as pt
from time import sleep

sleep(0.2)

pt.FAILSAFE = True

screenshot_remind = pt.screenshot("imgs/screenshot_remind.png", region=(1012,655,188,28))
remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(1012,655,188,28), confidence=0.8)

while 1:
    sleep(1)
    
    remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(932,673,60,25), confidence=0.8)
    if remind is not None:
        print("i see")
    reminnd= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(932,673,60,25), confidence=0.8)
    if remind is None:
        print("i not see")  
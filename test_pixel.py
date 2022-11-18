import pyautogui as pt
import win32gui,win32con
import keyboard
from time import sleep
from pynput. keyboard import Key, Controller

sleep(0.2)

pt.FAILSAFE = True 

#hwnd = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

sleep(0.5)


 # search cargo
screenshot_region_cargo=pt.screenshot("imgs/screenshot_region_cargo.png", region=(721,777,719,51))
print("screenshot from region cargo")

while 1:
    
    sleep(0.5)
    
    while 1:
    
        # screenshot region gols
        screenshot_region1_gold=pt.screenshot("imgs/screenshot_region1_gold.png", region=(727,783,42,38))

        # search for gold
        gold= pt.locateOnScreen("imgs/gold.png", grayscale=False, region=(727,783,42,38), confidence=0.83)
        
        ############################################
        if pt.pixel(833,803)[0] == 84:
            sleep(0.1)
            if gold is None:
                print("ok region 1")
                
        if pt.pixel(833,803)[0] == 84:
            sleep(0.1)
            if gold is not None:
                print("not ok with gold region 1")

        if pt.pixel(833,803)[0] != 84:
            sleep(0.1)
            print("not ok region 1")
            
        ############################################
        if pt.pixel(1024,801)[0] == 84: 
            sleep(0.1)
            if gold is None:
                print("ok region 2")
                
        if pt.pixel(1024,801)[0] == 84: 
            sleep(0.1)
            if gold is not None:
                print("not ok with gold region 2")

        if pt.pixel(1024,801)[0] != 84:
            sleep(0.1)
            print("not ok region 2")
        ############################################
        if pt.pixel(1222,801)[0] == 84: 
            sleep(0.1)
            if gold is None:
                print("ok region 3")
                
        if pt.pixel(1222,801)[0] == 84: 
            sleep(0.1)
            if gold is not None:
                print("not ok with gold region 3")

        if pt.pixel(1222,801)[0] != 84:
            sleep(0.1)
            print("not ok region 3")
        ############################################
        if pt.pixel(1414,800)[0] == 84: 
            sleep(0.1)
            if gold is None:
                print("ok region 4")
                
        if pt.pixel(1414,800)[0] == 84:
            sleep(0.1)
            if gold is not None:
                print("not ok with gold region 4")

        if pt.pixel(1414,800)[0] != 84:
            sleep(0.1)
            print("not ok region 4")
        
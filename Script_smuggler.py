import pyautogui as pt
import win32gui,win32con
from time import sleep

sleep(0.5)

pt.FAILSAFE = True 

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

sleep(0.5)

# loop smuggler
print("START SMUGGLER")
while 1:
    
    sleep(1)
    
    # click on smuggler
    pt.moveTo(331,417)
    sleep(0.2)
    pt.click()
    print("clickt on smuggler")
    
    # new screen
    sleep(1)
        
    # loop for exchange
    print("loop exchange")
    while 1:
        
        sleep(1)
        
        while 1:
            print("search for exchange")
            ############################################
            
            # loop region 1 gold
            print("start region 1")
            sleep(0.5)
                
            pt.FAILSAFE = True
            gold= pt.locateOnScreen("imgs/gold.png", grayscale=False, region=(727,783,42,38), confidence=0.8)
    
            if pt.pixel(833,803)[0] == 84 and gold is None:
                print("ok region 1")
                pt.moveTo(796,802)
                sleep(0.2)
                pt.click()
                sleep(0.2)
                
                while 1:
                    
                    # search for remind
                    remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(1012,655,188,28), confidence=0.8)
                    if remind is not None:
                        print("i see remind")
                        
                        # click on remind
                        pt.moveTo(988,668)
                        sleep(0.2)
                        pt.click()
                        print("clickt on remind")
                        
                        
                        # exit screen remind
                        pt.moveTo(1378,447)
                        sleep(0.2)
                        pt.click()
                        print("exit screen remind")
                        break
                        
                    remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(1012,655,188,28), confidence=0.8)
                    if remind is None:
                        print("i not see remind")
                        break
                    
            if pt.pixel(833,803)[0] == 84 and gold is not None:
                sleep(0.2)
                print("not ok with gold region 1")
                break
            
    
            if pt.pixel(833,803)[0] != 84:
                sleep(0.1)
                print("not ok with pixel region 1")
                break
            
        ############################################
        while 1:
            # loop region 2 gold
            print("start region 2")
            sleep(0.5)
            
            pt.FAILSAFE = True
            gold= pt.locateOnScreen("imgs/gold.png", grayscale=False, region=(921,785,42,38), confidence=0.8)
    
            if pt.pixel(1024,801)[0] == 84 and gold is None:
                print("ok region 2")
                pt.moveTo(983,802)
                sleep(0.2)
                pt.click()
                sleep(0.2)
                
                # search for remind
                remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(1012,655,188,28), confidence=0.8)
                if remind is not None:
                    print("i see remind")
                    
                    # click on remind
                    pt.moveTo(988,668)
                    sleep(0.2)
                    pt.click()
                    print("clickt on remind")
                    
                    
                    # exit screen remind
                    pt.moveTo(1378,447)
                    sleep(0.2)
                    pt.click()
                    print("exit screen remind")
                    break
                    
                remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(1012,655,188,28), confidence=0.8)
                if remind is None:
                    print("i not see remind")
                    break
                    
            if pt.pixel(1024,801)[0] == 84 and gold is not None:
                sleep(0.2)
                print("not ok with gold region 2")
                break
                
    
            if pt.pixel(1024,801)[0] != 84:
                sleep(0.1)
                print("not ok with pixel region 2")
                break
            
        ############################################
        while 1:
            # loop region 3 gold
            print("start region 3")
            sleep(0.5)
            
            pt.FAILSAFE = True
            gold= pt.locateOnScreen("imgs/gold.png", grayscale=False, region=(1114,785,42,38), confidence=0.8)
            if pt.pixel(1222,801)[0] == 84 and gold is None:
                print("ok region 3")
                pt.moveTo(1178,799)
                sleep(0.2)
                pt.click()
                sleep(0.2)
                
                # search for remind
                remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(1012,655,188,28), confidence=0.8)
                if remind is not None:
                    print("i see remind")
                    
                    # click on remind
                    pt.moveTo(988,668)
                    sleep(0.2)
                    pt.click()
                    print("clickt on remind")
                    
                    
                    # exit screen remind
                    pt.moveTo(1378,447)
                    sleep(0.2)
                    pt.click()
                    print("exit screen remind")
                    break
                    
                remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(1012,655,188,28), confidence=0.8)
                if remind is None:
                    print("i not see remind")
                    break
                    
            if pt.pixel(1222,801)[0] == 84 and gold is not None:
                print("not ok with gold region 3")
                break
            
            if pt.pixel(1222,801)[0] != 84:
                sleep(0.1)
                print("not ok with pixel region 3")
                break
            
        ############################################
        while 1:
            # loop region 4 gold
            print("start region 4")
            sleep(0.5)
            
            pt.FAILSAFE = True
            gold= pt.locateOnScreen("imgs/gold.png", grayscale=False, region=(1307,784,42,38), confidence=0.8)
    
            if pt.pixel(1414,800)[0] == 84 and gold is None:
                print("ok region 4")
                pt.moveTo(1371,801)
                sleep(0.2)
                pt.click()
                sleep(0.2)
                
                # search for remind
                remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(1012,655,188,28), confidence=0.8)
                if remind is not None:
                    print("i see remind")
                    
                    # click on remind
                    pt.moveTo(988,668)
                    sleep(0.2)
                    pt.click()
                    print("clickt on remind")
                    
                    
                    # exit screen remind
                    pt.moveTo(1378,447)
                    sleep(0.2)
                    pt.click()
                    print("exit screen remind")
                    break
                    
                remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(1012,655,188,28), confidence=0.8)
                if remind is None:
                    print("i not see remind")
                    break
                    
            if pt.pixel(1414,800)[0] == 84 and gold is not None:
                print("not ok with gold region 4")
                break
            
            if pt.pixel(1414,800)[0] != 84:
                sleep(0.1)
                print("not ok with pixel region 4")
                break
            
        screenshot_region_40=pt.screenshot("imgs/screenshot_region_40.png", region=(721,777,719,51))
        x= pt.locateOnScreen("imgs/40.png", grayscale=False, region=(984,471,25,19), confidence=0.92)
        if x is None:
            print("i not see 40 gold attemp")  
                      
            # click on free attemps
            pt.moveTo(983,471)
            sleep(1)
            pt.click()
            pt.moveTo(1086,868)
            print("click on free attemps")
            sleep(0.5) 
    
        x= pt.locateOnScreen("imgs/40.png", grayscale=False, region=(984,471,25,19), confidence=0.92)
        if x is not None:
            print("i see 40 gold attemp")
        
            # exit smuggler screen
            sleep(0.5)
            pt.moveTo(1483,271)
            sleep(0.2)
            pt.click()
            print("exit smuggler screen")
            print("END SCRIPT SMUGGLER")
            break 
    break                
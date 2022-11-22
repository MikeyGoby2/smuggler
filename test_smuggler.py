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
        
        screenshot_region_exchange=pt.screenshot("imgs/screenshot_region_exchange.png", region=(725,780,714,47))
        
        cargo= pt.locateOnScreen("imgs/cargo.png", grayscale=False, region=(725,780,714,47), confidence=0.8)
        if cargo is not None:
            print("cargo")
            pt.moveTo(cargo)
            sleep(0.2)
            pt.click()
            sleep(0.5)
            
            cargo= pt.locateOnScreen("imgs/cargo.png", grayscale=False, region=(725,780,714,47), confidence=0.8)
            money= pt.locateOnScreen("imgs/money.png", grayscale=False, region=(725,780,714,47), confidence=0.8)


            if cargo and money is None:
                print("i not see cargo and money")  
                          
                # click on free attemps
                pt.moveTo(983,471)
                sleep(1)
                pt.click()
                pt.moveTo(1086,868)
                print("click on free attemps")
                sleep(0.5)
            
            
            
        money= pt.locateOnScreen("imgs/money.png", grayscale=False, region=(725,780,714,47), confidence=0.8)
        if money is not None:
            print("money")
            pt.moveTo(money)
            sleep(0.2)
            pt.click()
            sleep(0.5)
            
            cargo= pt.locateOnScreen("imgs/cargo.png", grayscale=False, region=(725,780,714,47), confidence=0.8)
            money= pt.locateOnScreen("imgs/money.png", grayscale=False, region=(725,780,714,47), confidence=0.8)
            
            if cargo and money is None:
                print("i not see cargo and money")  
                          
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
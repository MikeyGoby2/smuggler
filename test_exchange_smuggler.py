import pyautogui as pt
import win32gui,win32con
from time import sleep

sleep(0.5)

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

sleep(0.5)

print("START EXCHANGE SMUGGLER")

# loop search 40 gold
print("start search 40 gold")
pt.FAILSAFE = True 
while 1:
    
    sleep(0.5)
    
    # check for search 40 gold
    search_gold= pt.locateOnScreen("imgs/40.png", grayscale=False, region=(984,471,25,19), confidence=0.92)
    if search_gold is not None:
        print("i see search 40 gold")
    
        # exit smuggler screen
        sleep(0.5)
        pt.moveTo(1483,271)
        sleep(0.2)
        pt.click()
        print("exit smuggler screen")
        print("END EXCHANGE SMUGGLER")
        break   
    
    search_gold= pt.locateOnScreen("imgs/40.png", grayscale=False, region=(984,471,25,19), confidence=0.92)
    if search_gold is None:
        print("i not see 40 gold attemp")
    
    
    # loop exchange
    print("start exchange")
    pt.FAILSAFE = True 
    while 1:    
        
        # search for exchange
        print("search exchange")
        
        sleep(0.2)
        
        # search cargo
        cargo= pt.locateOnScreen("imgs/cargo.png", grayscale=False, region=(725,780,714,47), confidence=0.78)
        if cargo is not None:
            print("i see cargo")
            
            # click on cargo
            pt.moveTo(cargo)
            sleep(0.2)
            pt.click()
            print("clickt cargo")
            
            sleep(0.2)
            
            # return to point
            pt.moveTo(1083,863)
            sleep(0.2)
            pt.click()
            print("return")
        
            sleep(0.2)
            
        sleep(0.2)
        
        # search money
        money= pt.locateOnScreen("imgs/money.png", grayscale=False, region=(725,780,714,47), confidence=0.8)
        if money is not None:
            print("i see money")
            
            # click on cargo
            pt.moveTo(money)
            sleep(0.2)
            pt.click()
            print("clickt money")
            
            sleep(0.2)
            
            # return to point
            pt.moveTo(1083,863)
            sleep(0.2)
            pt.click()
            print("return")
            
            sleep(0.2)
        
        sleep(0.1)   
        
        if cargo is None:
            print("none cargo left")
            
            if money is None:
                print("none money left")
        
                # click on search
                pt.moveTo(984,472)
                sleep(0.2)
                pt.click()
                print("clickt search")
                break
        
        if money is None:
            print("none money left")
            
            if cargo is None:
                print("none cargo left")
        
                # click on search
                pt.moveTo(984,472)
                sleep(0.2)
                pt.click()
                print("clickt search")
                
                # return to point
                pt.moveTo(1083,863)
                sleep(0.2)
                pt.click()
                print("return")
                
                break
    
import pyautogui as pt
import win32gui,win32con
from time import sleep

sleep(0.5) 

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

sleep(0.5)

# start smuggler
print("START SMUGGLER")

# loop setting
print("start setting smuggler")
pt.FAILSAFE = True
while 1:
    
    sleep(1)
    
    # click on smuggler
    pt.moveTo(331,417)
    sleep(0.2)
    pt.click()
    print("clickt on smuggler")
    
    # new screen
    sleep(1)
    
    # check screen smuggler
    if pt.pixel(615,266)[0] == 123:
        print("check screen smuggler ok")
    
    if pt.pixel(615,266)[0] != 123:
        print("check screen smuggler----- NOT OK -----")
        
        # click on city map
        pt.moveTo(960,992)
        sleep(0.2)
        pt.click()
        print("clickt city map")
        
        # new sreen
        sleep(2)
        
        # click on back
        pt.moveTo(960,992)
        sleep(0.2)
        pt.click()
        print("clickt back")
        
        # new screen
        sleep(2)
        
        # click on smuggler
        pt.moveTo(331,417)
        sleep(0.2)
        pt.click()
        print("clickt on smuggler")
        
        # new screen
        sleep(1) 
    
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
        print("END SCRIPT SMUGGLER")
        break   
    
    search_gold= pt.locateOnScreen("imgs/40.png", grayscale=False, region=(984,471,25,19), confidence=0.92)
    if search_gold is None:
        print("i not see 40 gold attemp")
    
    sleep(1)
    
    # search for exchange
    print("search exchange")
    
    screenshot_region_exchange=pt.screenshot("imgs/screenshot_region_exchange.png", region=(725,780,714,47))  
    print("screenshot region exchange")
    
    # search cargo
    cargo= pt.locateOnScreen("imgs/cargo.png", grayscale=False, region=(725,780,714,47), confidence=0.8)
    if cargo is not None:
        print("cargo")
        pt.moveTo(cargo)
        sleep(0.2)
        pt.click()
        sleep(0.5)
            
        screenshot_region_remind=pt.screenshot("imgs/screenshot_region_remind.png", region=(1013,655,181,24))  
        print("screenshot region exchange")
            
        # check remind
        print("check remind")
        
        remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(1013,655,181,24), confidence=0.8)
        if remind is not None:
            print("i see remind")
            
            # click on remind
            pt.moveTo(988,670)
            sleep(0.2)
            pt.click()
            print("clickt remind")
            
            # exit remind
            pt.moveTo(1378,448)
            sleep(0.2)
            pt.click()
            print("exit remind")
            
            # exit smuggler
            pt.moveTo(1482,270)
            sleep(0.2)
            pt.click()
            print("clickt exit smuggler")
            
            print("END SELLECT SMUGGLER")
            break
        
        else:
            print("i not see remind")
            print("END SELLECT SMUGGLER")
            break
           
    sleep(0.5)
        
    money= pt.locateOnScreen("imgs/money.png", grayscale=False, region=(725,780,714,47), confidence=0.8)
    if money is not None:
        print("money")
        pt.moveTo(money)
        sleep(0.2)
        pt.click()
        
        # new sreen
        sleep(1)
        
        
        screenshot_region_remind=pt.screenshot("imgs/screenshot_region_remind.png", region=(1013,655,181,24))  
        print("screenshot region exchange")
            
        # check remind
        print("check remind")
        
        remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(1013,655,181,24), confidence=0.8)
        if remind is not None:
            print("i see remind")
            
            # click on remind
            pt.moveTo(988,670)
            sleep(0.2)
            pt.click()
            print("clickt remind")
            
            # exit remind
            pt.moveTo(1378,448)
            sleep(0.2)
            pt.click()
            print("exit remind")
            
            # exit smuggler
            pt.moveTo(1482,270)
            sleep(0.2)
            pt.click()
            print("clickt exit smuggler")
            
            print("END SELLECT SMUGGLER")
            break
         
        else:
            print("i not see remind")
            print("END SELLECT SMUGGLER")
            break
    
    # click on search
    else:
        pt.moveTo(984,472)
        sleep(0.2)
        pt.click()
        print("clickt search (all gold)")
        
        screenshot_region_exchange=pt.screenshot("imgs/screenshot_region_exchange.png", region=(725,780,714,47))  
        print("screenshot region exchange")
        
        # search cargo
        cargo= pt.locateOnScreen("imgs/cargo.png", grayscale=False, region=(725,780,714,47), confidence=0.8)
        if cargo is not None:
            print("cargo")
            pt.moveTo(cargo)
            sleep(0.2)
            pt.click()
            sleep(0.5)
                
            screenshot_region_remind=pt.screenshot("imgs/screenshot_region_remind.png", region=(1013,655,181,24))  
            print("screenshot region exchange")
                
            # check remind
            print("check remind")
            
            remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(1013,655,181,24), confidence=0.8)
            if remind is not None:
                print("i see remind")
                
                # click on remind
                pt.moveTo(988,670)
                sleep(0.2)
                pt.click()
                print("clickt remind")
                
                # exit remind
                pt.moveTo(1378,448)
                sleep(0.2)
                pt.click()
                print("exit remind")
                
                # exit smuggler
                pt.moveTo(1482,270)
                sleep(0.2)
                pt.click()
                print("clickt exit smuggler")
                
                print("END SELLECT SMUGGLER")
                break
            
            else:
                print("i not see remind")
                print("END SELLECT SMUGGLER")
                break
               
        sleep(0.5)
            
        money= pt.locateOnScreen("imgs/money.png", grayscale=False, region=(725,780,714,47), confidence=0.8)
        if money is not None:
            print("money")
            pt.moveTo(money)
            sleep(0.2)
            pt.click()
            
            # new sreen
            sleep(1)
            
            
            screenshot_region_remind=pt.screenshot("imgs/screenshot_region_remind.png", region=(1013,655,181,24))  
            print("screenshot region exchange")
                
            # check remind
            print("check remind")
            
            remind= pt.locateOnScreen("imgs/remind.png", grayscale=False, region=(1013,655,181,24), confidence=0.8)
            if remind is not None:
                print("i see remind")
                
                # click on remind
                pt.moveTo(988,670)
                sleep(0.2)
                pt.click()
                print("clickt remind")
                
                # exit remind
                pt.moveTo(1378,448)
                sleep(0.2)
                pt.click()
                print("exit remind")
                
                # exit smuggler
                pt.moveTo(1482,270)
                sleep(0.2)
                pt.click()
                print("clickt exit smuggler")
                
                print("END SELLECT SMUGGLER")
                break
             
            else:
                print("i not see remind")
                print("END SELLECT SMUGGLER")
                break
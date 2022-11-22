import pyautogui as pt
from time import sleep

sleep(0.2)

pt.FAILSAFE = True



while 1:
    sleep(1)
    
    # search cargo
    cargo= pt.locateOnScreen("imgs/cargo.png", grayscale=False, region=(725,780,714,47), confidence=0.78)
    if cargo is not None:
        print("i see cargo")
        
    if cargo is None:
        print("i not see cargo")
    
    money= pt.locateOnScreen("imgs/money.png", grayscale=False, region=(725,780,714,47), confidence=0.8)
    if money is not None:
        print("i see money")
        
    if money is None:
        print("i not see money")
#ScreenCap
#A tool which records screenshots in stealth mode.
#Author - WireBits

import os
import time
import pyautogui

def capture_screenshots(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    i = 1
    while True:
        screenshot = pyautogui.screenshot()
        timestamp = time.strftime("%Y%m%d%H%M%S")
        file_path = os.path.join(folder_path, f"screenshot_{timestamp}_{i}.png")
        screenshot.save(file_path)
        time.sleep(1)
        i += 1

folder_path = ".screenshots"
capture_screenshots(folder_path)
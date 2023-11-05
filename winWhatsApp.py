import os
import pyautogui 
import time
from time import strftime

#Start WhatsApp Desktop App on Windows
os.system('start WhatsApp:')

#Bring the Window to the top
pyautogui.hotkey('win', 'up')
time.sleep(3)

#Move to the Search Users Field. To get the Coordinates on your screen you can use my little Script @ https://github.com/bsailer2510/mouseposition_window
pyautogui.moveTo(156, 179)
pyautogui.click (button = 'left')
#time.sleep(1)

#Search for the User
pyautogui.write("Enter User here")
time.sleep(1)

#CLick on the found User (First Result)
pyautogui.moveTo(394, 284)
pyautogui.click (button = 'left')
time.sleep(1)

#Send them messages
for i in range (1000):
    time1 = (strftime("%Y-%m-%d %H:%M:%S"))

    pyautogui.write("Funny, if you receive 1000x Messages during the night with acoustic notification - " + (time1))
    pyautogui.press('enter')
    time.sleep(1)

# Close WhatsApp
os.system('TASKKILL /F /IM WhatsApp.exe')

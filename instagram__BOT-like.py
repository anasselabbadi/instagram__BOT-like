import pyautogui
import sys
from time import sleep
import pyperclip
o="No"
while o=="No":
    nb = pyautogui.prompt(text='ENTER HOW MUCH TIME (1,2.......!)', title='SPAM ' , default='')
    o=pyautogui.confirm('Have you clicked inside text box where you want to write ?' ,buttons=['yes','no'])
    if o =='yes':
        sleep(5)
        pyperclip.copy('var n = document.getElementsByClassName("_aagw");n[0].click();')
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
        sleep(3)
        pyperclip.copy('var slides = document.getElementsByClassName("_abl-");slides[5].click();')
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
        sleep(3)
        pyperclip.copy('var slides = document.getElementsByClassName("_abl-");slides[3].click();')
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
        sleep(3)     
        for i in range (1,int(nb)):
                pyperclip.copy('var slides = document.getElementsByClassName("_abl-");slides[4].click();')
                pyautogui.hotkey("ctrl", "v")
                pyautogui.press('enter')
                sleep(3)
                pyperclip.copy('var slides = document.getElementsByClassName("_abl-");slides[6].click();')
                pyautogui.hotkey("ctrl", "v")
                pyautogui.press('enter')
                sleep(3)

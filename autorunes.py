import pyautogui
import keyboard

CONFIDENCE = 0.8

def editPage():
    while keyboard.is_pressed('alt') != True:
        locale = pyautogui.locateOnScreen('./images/edit.png', CONFIDENCE)
        if locale != None:
            print(locale)
            pyautogui.click(locale.x, locale.y)


def savePage():
    pyautogui.click(pyautogui.locateOnScreen('./images/save.png', CONFIDENCE))


def selectRuna():
     while keyboard.is_pressed('alt') != True:
        if pyautogui.locateOnScreen('./images/edit.PNG', confidence = CONFIDENCE) != None:
            print("ACHOU!")
            pyautogui.click(679, 558)




def main():
    # editPage()
    selectRuna()
    
    
    
main()
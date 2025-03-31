import pyautogui
import keyboard

while keyboard.is_pressed('q') == False:
    get1 = input('\nGet Cords Press Enter! \n')
    pos1 = pyautogui.position()
    print(str(pos1[0]) + ',' + str(pos1[1]))

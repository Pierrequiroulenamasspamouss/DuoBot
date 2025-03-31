import pyautogui as pya
import time
import screen
from ppadb.client import Client
import random
from config import *

#___________________________________________________________________________________________________________________________________________________#
# Initiate Pyautogui

pya.useImageNotFoundException()

    # ADB shenanigans
adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()
device = devices[0]




#___________________________________________________________________________________________________________________________________________________#
# Functions


def computerResToPhoneRes(coordinates):
    # Décalage dû aux bordures noires ajoutées par scrcpy
    offset_x = (computer_resolution[0] - scrcpy_dimensions[0]) / 2
    offset_y = (computer_resolution[1] - scrcpy_dimensions[1]) / 2

    # Coordonnées normalisées dans la zone affichée par scrcpy
    norm_x = (coordinates[0] - offset_x) / scrcpy_dimensions[0]
    norm_y = (coordinates[1] - offset_y) / scrcpy_dimensions[1]

    # Conversion vers la résolution du téléphone
    x = round(norm_x * Phoneresolution[0], 0)
    y = round(norm_y * Phoneresolution[1], 0)

    return (int(x), int(y))


def swipeOnPhone(phoneCoordinates, dur):
    #TODO : changer ceci en computerCoordinates
    Xini, Yini, Xfin, Yfin = phoneCoordinates
    '''This function's role is to swipe from a position to another, for a certain duration. '''
    device.shell(f'input touchscreen swipe {Xini} {Yini} {Xfin} {Yfin} {dur}')


def clickOnPhone(computerPos):
    '''This function works like a converter from computer found positions translated into phone's position : 
    the phone has a different resolution than the computer, so the position of the found image on the computer's screen has to be translated back into the phone's matching coordinates '''

    phonex,phoney = computerResToPhoneRes(computerPos)
    device.shell(f'input tap {phonex} {phoney}')


def pressOnPhone(computerPos):
    temp = computerResToPhoneRes(computerPos)
    
    swipeOnPhone((temp[0],temp[1],temp[0],temp[1]), swipe_speed)


def confirm():
    for _ in range(2):
        clickOnPhone(Confirm_POS)
        time.sleep(0.1)
    return 0


def Whereis(Searched_item, confidence, region) :
    global generalPurposeCounter
    imagePos = None
    while imagePos == None and generalPurposeCounter < maxIterations:
        try:
            imagePos = pya.locateCenterOnScreen(Searched_item,confidence= confidence, region = region)
            time.sleep(0.05)
        except:
            generalPurposeCounter +=1
    generalPurposeCounter = 0 # Reset the counter for next use
    return imagePos


def assemble(listnumber):
    '''This function searches the matching region and returns a list of positions to click to match the answers'''
    positionsList = []
    answercounter = 0  # Remplace generalPurposeCounter

    while len(positionsList) < 6:  # ou numberOfPropositions*2 selon ton besoin
        NewPosition = Whereis(ANSWERSLIST[answercounter + listnumber], 0.90, MatchingAnswersRegion)

        if NewPosition is not None:  # Évite d'ajouter None à la liste
            positionsList.append(NewPosition)
            answercounter += 1
        else:
            callMe(f"Incapacité de retrouver l'asset {answercounter + listnumber}")

    return positionsList

def callMe(message):
    # TODO: should send a webhook to a discord server to notify the program is stuck...
    while True:
        print(f"issue here: {message}")
        time.sleep(1)



#___________________________________________________________________________________________________________________________________________________#
# Standard exercise
def makeLessons(maxLessons = 999):
    """ maxLessons = -1 means there is no stop"""
    while numberOfLessons < maxLessons or maxLessons == -1:
        print("The session started")
        CourseIsOn = True
        screen.launchscrcpy(3)
        while CourseIsOn == True:
            
            #waiting for duo to load the first exercise:
            while Whereis(DRAWONE,globalConfidence,screenRegion) == None: pass

            swipeOnPhone(strokes["Stroke_1_1"],swipe_speed)  #first stroke
            confirm()
            time.sleep(0.5*phone_slowness)

            swipeOnPhone(strokes["Stroke_2_1"],swipe_speed)  #first stroke
            swipeOnPhone(strokes["Stroke_2_2"],swipe_speed)  #second stroke
            confirm()
            time.sleep(0.5*phone_slowness)

            swipeOnPhone(strokes["Stroke_3_1"],swipe_speed)  #first stroke
            swipeOnPhone(strokes["Stroke_3_2"],swipe_speed)  #second stroke
            swipeOnPhone(strokes["Stroke_3_3"],swipe_speed)  #third stroke
            confirm()
            time.sleep(0.2*phone_slowness)


            Offset_Counter,answerPosition = 0,0
            if debug: print("Now searching for matching questions")
            for i in range (3): # Number of times there are a matching exercise
                positionsList = assemble(Offset_list[Offset_Counter])
                
                for j in range(numberOfPropositions*2):
                    s= time.time()
                    clickOnPhone(positionsList[answerPosition])
                    answerPosition +=1
                    time.sleep(random.randint(1,10)/5000)
                    e= time.time()
                    if debug: print(f'time to click on all answers: {e-s} seconds')
                confirm()
                answerPosition,Offset_Counter,PracticePos,CourseIsOn = 0, Offset_Counter +1, None, False
                
            while PracticePos == None :
                try: 
                    PracticePos = pya.locateCenterOnScreen(PRACTICEBUTTON , confidence = globalConfidence, region = screenRegion)   #check if the practice button is visible, and if not, clickOnPhone the "continue button"'s position
                    clickOnPhone (Confirm_POS)
                except:
                    confirm()
                    generalPurposeCounter +=1
                if generalPurposeCounter >maxIterations: 
                    callMe("échec du lancement d'un nouvel exercice")
                    generalPurposeCounter = 0
                
        
            Offset_Counter,generalPurposeCounter = 0,0

        # Launch another exercise
        pressOnPhone(PracticePos)
        time.sleep(0.1)
        numberOfLessons +=1
        if debug: print(numberOfLessons)
        CourseIsOn = True

if __name__ == '__main__':
    makeLessons(-1)
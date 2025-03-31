    # If you change one of those resolutions, you have to remake the assets library. 
Phoneresolution = (1080, 2400)
computer_resolution = (1920,1080) # 1080p horizontal
scrcpy_dimensions = [420,1080]    #1080p vertical

    # Whether there are print statements everywhere or not. 
debug = False

    # Position of the confirm button on computer, could add a setup to auto find it...
Confirm_POS = (845,972) 

    # Where to search on screen for matching exercises. 
MatchingAnswersRegion = (715,380,1200,750) 

    # Offsets required for matching, which asset matches which 
screenRegion = (710,110, 1200, 1000)
Offset_list = [0,6,6]

    # Path for the assets
Default_path = r"\Assets" 



    # If you want for you computer to search more times the image on screen
maxIterations = 30

    # Image confidence
globalConfidence =0.90

    # Number of propositions on Assemnble. Can range from 3 to 5
numberOfPropositions = 3

    # Speed at which the program makes the strokes and/or presses (milliseconds)
swipe_speed = 110 

    # Delay between strokes multiplier (in %)
phone_slowness = 0.9 


generalPurposeCounter = 0 
numberOfLessons = 0 # number of lessons the program has completed

strokes = {
    #Those strokes positions are found on the phone screen. These are not the positions on the computer screen
    #TODO : change this to computer screen positions. 
    "Stroke_1_1": (222,1300 ,850, 1280),
    "Stroke_2_1": (300,1100 ,750, 1110),
    "Stroke_2_2": (200,1500 ,850, 1450),
    "Stroke_3_1": (300,1100 ,730, 1050),
    "Stroke_3_2": (320,1300 ,730, 1250),
    "Stroke_3_3": (200,1500 ,850, 1500)
}

scrcpy_path = r"C:\Program Files\scrcpy-win64-v2.7\scrcpy.exe"

#___________________________________________________________________________________________________________________________________________________#
# Importing assets to search for

    # Buttons
PRACTICEBUTTON = Default_path + r"\PRACTICE.png"
    # Statements
DRAWONE = Default_path + r"\DRAWONE.png"
    # Exercise answers 
K1 = Default_path + r"\MATCHING_ONE_JP.png"
K2 = Default_path + r"\MATCHING_TWO_JP.png"
K3 = Default_path + r"\MATCHING_THREE_JP.png"
H1 = Default_path + r"\MATCHING_ONE_HIRAGANA.png"
H2 = Default_path + r"\MATCHING_TWO_HIRAGANA.png"
H3 = Default_path + r"\MATCHING_THREE_HIRAGANA.png"
E1 = Default_path + r"\MATCHING_ONE_EN.png"
E2 = Default_path + r"\MATCHING_TWO_EN.png"
E3 = Default_path + r"\MATCHING_THREE_EN.png"


ANSWERSLIST = [K1,E1,K2,E2,K3,E3,    K1,H1,K2,H2,K3,H3 ] # each setup with it's matching answers in the right order.

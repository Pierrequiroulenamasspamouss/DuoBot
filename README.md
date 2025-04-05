# DuoBot
Automatic XP farmer with easy japanese lessons

# REQUIREMENTS: 
- Win11 (Maybe works on linux, but adaptations are required for the detection with pyautogui)
- Duolingo version 6.23.2 or later
- A computer and a phone
- An USB cable
- Some patience for the setup.
- Python 3.12.9

# SETUP 
0) Install Android Debug Bridge [directly from Android](https://developer.android.com/tools/adb?hl=en)  and also scrcpy (SCReenCoPY) in your folder "C:\Program Files\scrcpy-win64-v2.7\scrcpy.exe" ([directly from scrcpy.org](https://scrcpy.org/)) (Optional if already installed)

1) Install the required libraries:
   - Pure-python ADB 0.3.0 ([official link](https://pypi.org/project/pure-python-adb/))
   - Pyautogui  ([official link](https://pyautogui.readthedocs.io/en/latest/))
   - dotenv(required to use private discord webhooks token) ( [official link](https://pypi.org/project/python-dotenv/) )

3) Go to config.py and change the settings if you have a different phone than a REDMI Note 12 pro 5G
(e.g. : computer screen resolution, phone screen resolution,...)

4) Go on Duolingo and disable everything related to animations, motivational messages, sound effects, listening exercises, then put the lesson to Japanese, and go to the section "let's prectice Kanji" at the top and be sure there is only one blue "practice" button available. Be sure to be in dark mode for Duolingo, or else you'll have to redo the assets library
   
5) Plug your phone into your computer, and allow your phone to communicate with your computer by running adb devices() in a shell terminal. One device should pop up and/or a message on your unlocked phone to trust this device. It's your computer, you should be safe to allow it.

6) launch the python program by running
```shell
cd <PATH TO THE FOLDER> & python DuoBot.py
```
You can also import the program into your own python program by doing so:
```python
import DuoBot
(...)
DuoBot.makeLessons(<NUMBER OF LESSONS YOU WANT TO DO>)
#a number equal to -1 means there is no maximal number of lessons to do
```
# HOW TO REDO AN ASSET LIBRARY
1) Be ready to use your screencapture tool a lot, and start by launching SCRCPY:
```shell
cd C:\Program Files\scrcpy-win64-v2.7\ & .\scrcpy -m 1080 -f
```
2) Go though your lesson and screenshot with your computer every asset that is present in "\Assets". Crop them like they are currently. The smaller the image is, the faster the program goes.

# HOW TO KNOW THE POSITION OF SOMETHING ON YOUR SCREEN AT PIXEL PRECISION
1) Launch Mousepos.py in a terminal, be ready to enter textin it, and launch scrcpy.exe in another shell terminal.
2) Go to scrcpy and move your mouse cursor to the position of the searched item. 
3) Use ALT+TAB to switch onto the terminal with Mousepos.py running, and press enter. You should get the exact coordinates that you can plug back into config.py for whatever you'd need. 

# Help
- If the program is stuck at the matching exercise, try either lowering the confidence, or redoing the assets library.
- If there is no device detected, please refer to a tutorial on how to use scrcpy or Android Debug Bridge (ADB)
- If you want more infos, contact me via Discord: UID : 688759026564989072

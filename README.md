# DuoBot
Automatic XP farmer with easy japanese lessons

REQUIREMENTS: 
Win11 (Maybe works on linux, but adaptations are required for the detection with pyautogui)
Duolingo version 6.23.2 or later
A computer and a phone
An USB cable
Some patience for the setup.

# SETUP 
0) Install Android Debug Bridge [directly from Android]([https://www.google.com](https://developer.android.com/tools/adb?hl=en))(Optional if already installed) and also scrcpy in your folder "C:\Program Files\scrcpy-win64-v2.7\scrcpy.exe" ([link](https://scrcpy.org/))

1) Install the required libraries:
   -Pure-python ADB 0.3.0 ([official link](https://pypi.org/project/pure-python-adb/))
   -Pyautogui  ([official link](https://pyautogui.readthedocs.io/en/latest/))

3) Go to config.py and change the settings if you have a different phone than a REDMI Note 12 pro 5G
(e.g. : computer screen resolution, phone screen resolution,...)

4) Go on Duolingo and disable everything related to animations, motivational messages, sound effects, listening exercises, then put the lesson to Japanese, and go to the section "let's prectice Kanji" at the top and be sure there is only one blue "practice" button available. be sure to be in dark mode for Duolingo, or else you'll have to redo the assets library
   
5) Plug your phone into your computer, and allow your phone to communicate with your computer by running adb devices() in a shell terminal. One device should pop up and/or a message on your unlocked phone to trust this device. It's your computer, you should be safe to allow it.

6) launch the python program by running
```shell
cd <PATH TO THE FOLDER> | python DuoBot.py
```
You can also import the program into your own python program by doing so:
```python
import DuoBot
(...)
DuoBot.makeLessons(<NUMBER OF LESSONS YOU WANT TO DO>)
#a number equal to -1 means there is no maximal number of lessons to do
```

import keyboard
from pyautogui import *
import pyautogui
import time
import numpy as np
import random
import win32api
import win32con
import os

while 1:
    if pyautogui.locateOnScreen('lookOne.png') != None:
        print("Ayooo")
        time.sleep(0.2)
    else:
        print("where?")
        time.sleep(0.1)

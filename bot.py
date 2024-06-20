import keyboard
from pyautogui import *
import pyautogui
import time
import numpy as np
import random
import win32api
import win32con
import os


forward = 0
back = 0
time.sleep(5)

def void_this():
    path1 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'jpg.jpg')
    path2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lookTwo.png')
    # noinspection PyArgumentList
    if pyautogui.locateOnScreen('newPngBGD.png', grayscale=False, confidence=0.1) is not None:
        pass
    else:
        time.sleep(0.2)
        keyboard.press_and_release('1')
        for hitOnOne in range(6):
            time.sleep(0.2)
            keyboard.press_and_release('g')

    # noinspection PyArgumentList
    if pyautogui.locateOnScreen('lookTwo.png', grayscale=False, confidence=0.1) is None:
        pass
    else:
        time.sleep(0.2)
        keyboard.press_and_release('1')
        for hitOnOne in range(6):
            time.sleep(0.2)
            keyboard.press_and_release('g')
##


while keyboard.is_pressed('q') == False:
    time.sleep(0.3)
    print("keyPressed2_1stLine")
    keyboard.press_and_release('2')
    for forward in range(35):
        print("diggingForward")
        time.sleep(0.1)
        keyboard.press_and_release('a')
        time.sleep(0.1)
        keyboard.press_and_release('f')

    time.sleep(0.5)
    keyboard.press_and_release('1')
    for hitOnOne in range(30):
        print("Attack!")
        time.sleep(0.1)
        keyboard.press_and_release('g')

    time.sleep(0.1)
    print("keyPressed2_2ndLine")
    keyboard.press_and_release('2')
    for back in range(35):
        print("diggingBackward")
        time.sleep(0.1)
        keyboard.press_and_release('d')
        time.sleep(0.1)
        keyboard.press_and_release('f')

    time.sleep(0.5)
    keyboard.press_and_release('1')
    for hitOnOne in range(30):
        print("Attack!")
        time.sleep(0.1)
        keyboard.press_and_release('f')


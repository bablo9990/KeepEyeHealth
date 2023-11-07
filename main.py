import os
from time import sleep

import pyautogui
import schedule
import datetime


def is_mouse_position_stable():
    current_position = pyautogui.position()
    sleep(15)
    new_position = pyautogui.position()
    return current_position == new_position

# Set file paths
file = os.path.join(os.getcwd(), 'Exercises', 'main.py')
file_water = os.path.join(os.getcwd(), 'WaterMessage', 'main.py')
file_glasses = os.path.join(os.getcwd(), 'Glasses', 'main.py')

def run_eye():
    if not is_mouse_position_stable():
        os.system(f'python "{file}"')

def run_water():
    if not is_mouse_position_stable():
        os.system(f'python "{file_water}"')

def run_glasses():
    if not is_mouse_position_stable():
        os.system(f'python "{file_glasses}"')

# Schedule tasks
schedule.every(25).minutes.do(run_eye)
schedule.every(60).minutes.do(run_glasses)
schedule.every(15).minutes.do(run_water)

# Run scheduled tasks indefinitely
while True:
    schedule.run_pending()
    if datetime.datetime.now().hour == 24:
        break
    if datetime.datetime.now().strftime("%H") == "20" or datetime.datetime.now().strftime("%H") == "10":
        pyautogui.hotkey('win', 'ctrl', 'c')
    sleep(180)

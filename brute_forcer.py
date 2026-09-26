# Made by Justin Smeya

# This python tool automates the code guessing process for door bases in minecraft rust.
# Server name will be excluded, for now.

'''
DOOR CODE INFO:
- 1 minimum slot.
- 14 maximum slots.
- Standard 0-9 digits.
- Digits can repeat.

ADDITIONAL INFO:
- Digits are mapped to pixel coordinates on a 1920x1080 monitor for a fullscreen minecraft application.
- Inputs are based on those coordinates paired with a click (which is the actual automation part).
- Once a desired code is inputted, the program will map to the "ok" button and click to enter the code.

EFFICIENCY:
- Ctypes is used to call the windows API directly.
- No library overhead.
'''


# TODO:
# 1. Add (optional) arguments. Make sure they don't interfere with eachother though. E.g., digit count specification, file reading, interval speed
# 2. Add a killswitch hotkey.
# 3. Maybe add logging correct codes (pair with chat logs using timestamps).


# Imports
from itertools import product
import ctypes
import time

user32 = ctypes.windll.user32

# Bitmasks (hexadecimal)
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

# Digits mapped to coordinates on screen
# Supports a 1920x1080 fullscreen-ed minecraft
digits = {
    '0': (965, 505),
    '1': (905, 335),
    '2': (965, 335),
    '3': (1015, 335),
    '4': (905, 395),
    '5': (965, 395),
    '6': (1015, 395),
    '7': (905, 445),
    '8': (965, 445),
    '9': (1015, 445),
}
enter_button = (905, 505) # Coordinates of the enter button

# Digit clamping
min_digits = 1
max_digits = 14

# Absolute is faster
def move_to(x, y):
    user32.SetCursorPos(x, y)

# Simulate a full mouse click
def click():
    user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def click_slot(x, y):
    move_to(x, y)
    time.sleep(0.05)
    click()

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

def main():
    digit_count = int(input("Digit count: "))
    delay_time = float(input("Enter a delay time in s: "))

    time.sleep(3) # Wait time for transition
    
    for combo in product(digits, repeat=digit_count):
        click() # Click the door to open the code GUI
        time.sleep(delay_time)
        for num in combo:
            click_slot(*digits[num])
            time.sleep(delay_time)
        click_slot(*enter_button)
        time.sleep(delay_time)

if __name__ == "__main__":
    main()
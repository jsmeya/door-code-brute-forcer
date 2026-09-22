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

# TODO: Add the ability to log successful attempts by utilizing timestamps and chat logs.
# ^^ this will need the program to log all attempts and timestamps to a file.


# Imports
import ctypes
import time

user32 = ctypes.windll.user32
SCREEN_W = user32.GetSystemMetrics(0)
SCREEN_H = user32.GetSystemMetrics(1)

# Bitmasks (hexadecimal)
MOUSEEVENTF_MOVE = 0x0001 # Movement occured
MOUSEEVENTF_ABSOLUTE = 0x0008
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
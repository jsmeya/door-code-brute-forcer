# door-code-brute-forcer

A mouse-automation macro for guessing base door codes on a Rust-inspired Minecraft server.
<br>
<br>
The server in specific is intentionally omitted.
<br>
<br>
Base door codes are accessed through an on-screen gui / keypad. Clicking any given slot will input a code, with options to enter or reset the code.
This program maps that gui to pixel coordinates on a 1920x1080 fullscreen Minecraft window and inputs a given code.

## DISCLAIMER

This is a personal project to automate a simple task on a server I used to play a lot. My goals for this project were to better understand how to automate input in Python.
<br>
<br>
DO NOT use this code for any malicious purposes, or in any way that violates any server's rules or terms of service. Only run it against systems you have permission to test.

## Requirements

- Windows (uses the Win32 `user32` API via `ctypes`)
- Python 3.8+
- Minecraft running **fullscreen at 1920x1080**

Plan to implement automatic coordinate mapping to support all screen resolutions.

## Usage

```
python3 brute_forcer.py
```

The program prompts you for the following:

1. **A digit count (1-14) or a filename.**
   - A number generates and tries every `0-9` combination of that length.
   - A filename tries each code listed in that file, one per line.
2. **A delay time in seconds** between clicks (tune to your server's tick rate
   and input handling).

<br>

**Example:**
`Enter a digit count (1-14) or a filename: 4`
`Enter a delay time in s: 0.25`

<br>

After you confirm, you have 3 seconds to switch into fullscreen Minecraft before
the macro starts clicking. No killswitch yet, but you can alt+tab back into the terminal window and spam `Ctrl+C`.

## Door code specific rules

- 1 to 14 slots per code
- Digits `0-9`, repeats allowed

## Notes / roadmap

- Killswitch hotkey
- Logging of successful codes (no direct communication w/ Minecraft, so this will need to read the chat message on screen that displays a successful code)
- Support for all screen sizes

## Known Issues

- Latency from client-server communication doesn't cause total failure, but it definitely skips over some codes. If a player lags for pretty much any given amount of time, at least one code will be skipped. The impact itself is dependent on the "amount" of lag paired with the code digit length. My only guess to fix it would be adding a latency reader of some sort and checking that while inputting codes, but that may significantly slow down the process. In this case, the need for efficiency would outweigh the probability that any missed code(s) during a "lag window" are correct.
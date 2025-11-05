# Keylogger

A simple Python keylogger implemented in [`keylogger.py`](./keylogger.py).

## Overview

A keylogger is a program that records keyboard inputs made by a user. This implementation uses the `pynput` library to monitor and log keystrokes in real-time. The captured keystrokes are written to a log file for later review.

## How It Works

- The script listens for keyboard events using `pynput.keyboard.Listener`.
- Each key press is recorded and appended to a log file.
- The logger runs silently in the background, without displaying any windows or notifications.
- The log file location and format can be customized in the script.

## Features

- Logs all keystrokes to a file
- Runs silently in the background
- Cross-platform support (Windows, Linux, macOS)
- Easy to configure and extend

## Dependencies

- Python 3.x
- [`pynput`](https://pypi.org/project/pynput/) library for keyboard event handling

## Installation

1. **Install Python**  
    Ensure you have Python 3.x installed on your system.

2. **Install required libraries**  
    Open a terminal and run:
    ```bash
    pip install pynput
    ```

## Usage

1. **Run the keylogger**  
    ```bash
    python keylogger.py
    ```

2. **Check the log file**  
    The keystrokes will be saved to a log file as specified in the script (e.g., `keylog.txt`).

## Disclaimer

This project is for educational purposes only. Do not use it for malicious activities.

## License

MIT License

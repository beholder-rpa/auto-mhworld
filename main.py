from win32gui import GetWindowText, GetForegroundWindow
import simpleaudio as sa
import numpy as np
import os
from time import sleep
import random
import argparse
import keyboard as global_keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from colorama import Style, Fore, init as colorama_init
import time

colorama_init()
MHW_WINDOW_NAME = "Monster Hunter: World"

fanfare = sa.WaveObject.from_wave_file(
    os.path.dirname(__file__) + "\\sounds\\fanfare.wav"
)
bell = sa.WaveObject.from_wave_file(
    os.path.dirname(__file__) + "\\sounds\\bell.wav"
)
start = sa.WaveObject.from_wave_file(
    os.path.dirname(__file__) + "\\sounds\\start.wav"
)
stop = sa.WaveObject.from_wave_file(
    os.path.dirname(__file__) + "\\sounds\\stop.wav"
)
error = sa.WaveObject.from_wave_file(
    os.path.dirname(__file__) + "\\sounds\\error.wav"
)
keyboard = KeyboardController()
mouse = MouseController()

# Bank the Phials, aka Charge Phials
def bank_it(solo=False):
    if solo:
        start.play()
    # R+B
    mouse.press(Button.x2)
    mouse.press(Button.right)
    sleep(0.25)
    mouse.release(Button.right)
    mouse.release(Button.x2)
    if solo:
        stop.play()

def fill_phials(solo=False):
    if solo:
        start.play()

    # Y+B
    mouse.press(Button.x1)
    sleep(0.25)
    mouse.release(Button.x1)
    sleep(0.5) # Since we're lunging, we're slightly slower to the charge.

    # Hold B
    mouse.press(Button.right)
    sleep(1)
    mouse.release(Button.right)
    sleep(0.25)

    # Y
    mouse.press(Button.left)
    sleep(0.25)
    mouse.release(Button.left)
    sleep(0.5)

    # R+B
    bank_it()

    if solo:
        stop.play()

def fill_phials_2(solo=False):
    if solo:
        start.play()
    # Y + Hold B (release) + Y + (Hold RT + B)
    
    # Y + Hold B (release)
    mouse.press(Button.left)
    sleep(0.25)
    mouse.release(Button.left)
    sleep(0.25)

    # Hold B
    mouse.press(Button.right)
    sleep(1)
    mouse.release(Button.right)
    sleep(0.25)

    # Y
    mouse.press(Button.left)
    sleep(0.25)
    mouse.release(Button.left)
    sleep(0.5)

    # R+B
    bank_it()

    if solo:
        stop.play()

def charge_shield(solo=False):
    if solo:
        start.play()
        mouse.press(Button.x1)
        sleep(0.25)
        mouse.release(Button.x1)
        sleep(1)

    # Y+B
    mouse.press(Button.x1)
    sleep(0.25)
    mouse.release(Button.x1)
    sleep(1)

    # Y+B
    mouse.press(Button.x1)
    sleep(0.25)
    mouse.release(Button.x1)
    sleep(0.5)

    # R2
    mouse.press(Button.x2)
    sleep(0.25)
    mouse.release(Button.x2)
    if solo:
        stop.play()

def charge_sword(solo=False):
    if solo:
        start.play()
    # R+B
    mouse.press(Button.x2)
    mouse.press(Button.right)
    sleep(0.25)
    mouse.release(Button.right)
    mouse.release(Button.x2)
    sleep(0.5)

    # Hold Y
    mouse.press(Button.left)
    sleep(2)
    mouse.release(Button.left)
    if solo:
        stop.play()

def charge_blade_sword_combo(solo=False):
    if solo:
        start.play()
    # Y+B, hold B, Y, R+B, Y+B, Y+B, Y+B, R2, R+B, hold Y
    # Left+Right, Hold Right, Left, Ctrl+Right, Left+Right, Left+Right, Ctrl, Ctrl+Left, Hold Left then release

    fill_phials()
    sleep(0.25)

    # Charge Shield
    # Y+B
    mouse.press(Button.x1)
    sleep(0.25)
    mouse.release(Button.x1)
    sleep(1) # If we don't wait long enough, it does an elemental discharge

    # Y+B
    mouse.press(Button.x1)
    sleep(0.25)
    mouse.release(Button.x1)
    sleep(0.5) # If we don't wait long enough, it completes the SAED

    # This cancels the SAED, charging the shield
    mouse.press(Button.x2)
    sleep(1.25) # If we don't wait long enough, we go into a morph slash
    # Then we charge the sword
    mouse.press(Button.right)
    sleep(0.25)
    mouse.release(Button.right)
    mouse.press(Button.left)
    sleep(2.5) # The charge ls lengthy, if we don't wait long enough, it's just a return slash
    mouse.release(Button.left)
    mouse.release(Button.x2)

    if solo:
        stop.play()

def charge_blade_sword_combo_2(solo=False):
    if solo:
        start.play()
    # Y + Hold B (release) + Y + (Hold RT + B) + Y + Hold B (Release) + (Y+B) + (Y+B) + (Hold RT + B + Hold Y + Release)
    
    fill_phials_2()
    sleep(0.25)

    # Y + Hold B (release)
    mouse.press(Button.left)
    sleep(0.25)
    mouse.release(Button.left)
    sleep(1.25)

    mouse.press(Button.right)
    sleep(0.5)
    mouse.release(Button.right)
    sleep(1)

    # Charge Shield
    # Y+B
    mouse.press(Button.x1)
    sleep(0.25)
    mouse.release(Button.x1)
    sleep(0.5)

    # Y+B
    mouse.press(Button.x1)
    sleep(0.25)
    mouse.release(Button.x1)
    sleep(0.5)

    # This cancels the SAED, charging the shield
    mouse.press(Button.x2)
    sleep(1)
    # Then we charge the sword
    mouse.press(Button.right)
    sleep(0.25)
    mouse.release(Button.right)
    sleep(0.5)
    mouse.press(Button.left)
    sleep(2) # The charge ls lengthy
    mouse.release(Button.left)
    mouse.release(Button.x2)

    if solo:
        stop.play()

def saed_combo(solo=False):
    if solo:
        start.play()

    # Morph to Axe
    # R+Y
    mouse.press(Button.x2)
    mouse.press(Button.left)
    sleep(0.25)
    mouse.release(Button.left)
    mouse.release(Button.x2)
    sleep(1.5)

    # Y+B
    mouse.press(Button.left)
    mouse.press(Button.right)
    sleep(0.25)
    mouse.release(Button.left)
    mouse.release(Button.right)
    if solo:
        stop.play()

def saed_combo_2(solo: bool = False):
    if solo:
        start.play()
    
    # Morph to Axe
    # R+Y
    mouse.press(Button.x2)
    mouse.press(Button.left)
    sleep(0.25)
    mouse.release(Button.left)
    mouse.release(Button.x2)
    sleep(2)

    # B
    mouse.press(Button.right)
    sleep(0.25)
    mouse.release(Button.right)
    sleep(1)

    # B
    mouse.press(Button.right)
    sleep(0.25)
    mouse.release(Button.right)
    if solo:
        stop.play()

def savage_axe_combo(solo: bool = False):
    if solo:
        start.play()
    # Morph to Axe
    # R+Y
    mouse.press(Button.x2)
    mouse.press(Button.left)
    sleep(0.25)
    mouse.release(Button.left)
    mouse.release(Button.x2)
    sleep(2)

    # Y+B
    mouse.press(Button.x1)
    sleep(0.25)
    mouse.release(Button.x1)
    sleep(1)

    # C
    keyboard.press('c')
    sleep(0.25)
    keyboard.release('c')
    sleep(3.0)

    # Controversial, morph back to sword
    mouse.press(Button.x2)
    sleep(0.25)
    mouse.release(Button.x2)

    if solo:
        stop.play()

def savage_axe_finisher(solo: bool = False):
    if solo:
        start.play()
    # Morph to Axe
    # R+Y
    mouse.press(Button.x2)
    mouse.press(Button.left)
    sleep(0.25)
    mouse.release(Button.left)
    mouse.release(Button.x2)
    sleep(2)

    # Y+B
    mouse.press(Button.x1)
    sleep(0.25)
    mouse.release(Button.x1)
    sleep(1)

    # C
    keyboard.press('c')
    sleep(0.25)
    keyboard.release('c')
    sleep(3.25)

    # now we do the finisher
    mouse.press(Button.left)
    mouse.press(Button.right)
    sleep(0.25)
    mouse.release(Button.left)
    mouse.release(Button.right)
    
    if solo:
        stop.play()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()


    global debug
    debug = args.debug
    print(f"Debug: {debug}")

    print(f"{Fore.LIGHTMAGENTA_EX}Starting Auto MH:World ...{Style.RESET_ALL}")


    if args.debug:
        print(f"\t{Fore.LIGHTGREEN_EX}Debugging mode enabled{Style.RESET_ALL}")
    
    # Register Global Hotkeys
    global_keyboard.add_hotkey("0", charge_blade_sword_combo, args=[True])
    global_keyboard.add_hotkey("1", fill_phials, args=[True])
    global_keyboard.add_hotkey("4", charge_shield, args=[True])
    global_keyboard.add_hotkey("7", charge_sword, args=[True])
    global_keyboard.add_hotkey(".", charge_blade_sword_combo_2, args=[True])

    global_keyboard.add_hotkey("2", fill_phials_2, args=[True])

    global_keyboard.add_hotkey("+", savage_axe_finisher, args=[True])
    global_keyboard.add_hotkey("-", savage_axe_combo, args=[True])
    global_keyboard.add_hotkey("*", bank_it, args=[True])

    global_keyboard.add_hotkey("3", saed_combo, args=[True])
    global_keyboard.add_hotkey("6", saed_combo_2, args=[True])
    print(f"Press Ctrl+C to exit...")

    while True:
        try:
            time.sleep(100)
        except KeyboardInterrupt:
            print("Exiting...")
            exit()
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    main()
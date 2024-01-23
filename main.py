from win32gui import GetWindowText, GetForegroundWindow
import simpleaudio as sa
import numpy as np
import os
from time import sleep
import argparse
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from colorama import Style, Fore, init as colorama_init
import time
from StreamDeck.DeviceManager import DeviceManager

from modules.deckard import update_key_image

colorama_init()
MHW_WINDOW_NAME = "Monster Hunter: World"

fanfare = sa.WaveObject.from_wave_file(
    os.path.dirname(__file__) + "\\assets\\sounds\\fanfare.wav"
)
bell = sa.WaveObject.from_wave_file(
    os.path.dirname(__file__) + "\\assets\\sounds\\bell.wav"
)
start = sa.WaveObject.from_wave_file(
    os.path.dirname(__file__) + "\\assets\\sounds\\start.wav"
)
stop = sa.WaveObject.from_wave_file(
    os.path.dirname(__file__) + "\\assets\\sounds\\stop.wav"
)
error = sa.WaveObject.from_wave_file(
    os.path.dirname(__file__) + "\\assets\\sounds\\error.wav"
)
keyboard = KeyboardController()
mouse = MouseController()
currentDeck = None

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


actions = [
  {
    "index": 0,
    "icon": "charge_sword.png",
    "label": "Charge Sword",
    "action": charge_sword,
  },
  {
    "index": 1,
    "icon": "charge_shield.png",
    "label": "Charge Shield",
    "action": charge_shield,
  },
  {
    "index": 4,
    "icon": "charge_phials.png",
    "label": "Bank It",
    "action": bank_it,
  },
  {
    "index": 5,
    "icon": "Fill_Phials_1.png",
    "label": "Fill Phials Far",
    "action": fill_phials,
  },
  {
    "index": 6,
    "icon": "Fill_Phials_2.png",
    "label": "Fill Phials Near",
    "action": fill_phials_2,
  },
  {
    "index": 8,
    "icon": "SAED_2.png",
    "label": "SAED 2",
    "action": saed_combo_2,
  },
  {
    "index": 9,
    "icon": "Savage_Axe_Finisher_2.png",
    "label": "S. Axe Combo",
    "action": savage_axe_combo,
  },
  {
    "index": 10,
    "icon": "Combo_1.png",
    "label": "Full Combo Far",
    "action": charge_blade_sword_combo,
  },
  {
    "index": 11,
    "icon": "Combo_2.png",
    "label": "Full Combo Near",
    "action": charge_blade_sword_combo_2,
  },
  {
    "index": 13,
    "icon": "SAED_1.png",
    "label": "SAED",
    "action": saed_combo,
  },
  {
    "index": 14,
    "icon": "Savage_Axe_Finisher_1.png",
    "label": "S. Axe Finisher",
    "action": savage_axe_finisher,
  },
]

# Prints key state change information, updates rhe key image and performs any
# associated actions when a key is pressed.
def key_change_callback(deck, key, state):
    # Print new key state
    if debug:
        print("Deck {} Key {} = {}".format(deck.id(), key, state), flush=True)
    
    # only do stuff if the key is pressed
    if state == False:
        return
 
    keyAction = None
    for action in actions:
        if action["index"] == key:
            keyAction = action
            break
    
    if keyAction is None:
        return
    
    # Update the key image based on the new key state.
    update_key_image(deck, key, "Running.png", "Running...")
    # Perform the action
    keyAction["action"](solo=True)
    # Update the key image based on the new key state.
    update_key_image(deck, key, keyAction["icon"], keyAction["label"])

def main():
    streamdecks = DeviceManager().enumerate()
    print(f"Found {len(streamdecks)} Stream Deck(s). Usint the first visual Stream Deck.")

    # Get the first streamdeck where is_visual is True
    for deck in streamdecks:
        if deck.is_visual():
            print(f"Using {deck.deck_type()} as the Stream Deck.")
            currentDeck = deck
            break
    if currentDeck is None:
        print("No visual Stream Deck found. Exiting...")
        exit()

    currentDeck.open()
    currentDeck.reset()

    print("Opened '{}' device (serial number: '{}', fw: '{}')".format(
            deck.deck_type(), deck.get_serial_number(), deck.get_firmware_version()
        ))
    
    currentDeck.set_brightness(100)

    # Set initial key images.
    for key in range(deck.key_count()):
        # Find the action for the key
        keyAction = None
        for action in actions:
            if action["index"] == key:
                keyAction = action
                break
        if keyAction is not None:
            update_key_image(deck, key, keyAction["icon"], keyAction["label"])
    deck.set_key_callback(key_change_callback)

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    global debug
    debug = args.debug
    print(f"Debug: {debug}")

    print(f"{Fore.LIGHTMAGENTA_EX}Starting Auto MH:World ...{Style.RESET_ALL}")


    if args.debug:
        print(f"\t{Fore.LIGHTGREEN_EX}Debugging mode enabled{Style.RESET_ALL}")

    print(f"Press Ctrl+C to exit...")

    while True:
        try:
            time.sleep(100)
        except KeyboardInterrupt:
            print("Exiting...")
            # Wait until all application threads have terminated (for this example,
            # this is when all deck handles are closed).
            currentDeck.reset()
            currentDeck.close()
            exit()
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    main()
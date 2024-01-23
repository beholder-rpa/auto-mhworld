from win32gui import GetWindowText, GetForegroundWindow
import simpleaudio as sa
import numpy as np
import os
from time import sleep
import argparse
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
from colorama import Style, Fore, init as colorama_init
import time
from StreamDeck.DeviceManager import DeviceManager
from modules.charge_blade import ChargeBlade

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

charge_blade = ChargeBlade(
    mouse,
    keyboard,
    {"fanfare": fanfare, "bell": bell, "start": start, "stop": stop, "error": error},
)
actions = [
    {
        "index": 0,
        "icon": "charge_sword.png",
        "label": "Charge Sword",
        "action": charge_blade.charge_sword,
    },
    {
        "index": 1,
        "icon": "charge_shield.png",
        "label": "Charge Shield",
        "action": charge_blade.charge_shield,
    },
    {
        "index": 4,
        "icon": "charge_phials.png",
        "label": "Bank It",
        "action": charge_blade.bank_it,
    },
    {
        "index": 5,
        "icon": "Fill_Phials_1.png",
        "label": "Fill Phials Far",
        "action": charge_blade.fill_phials,
    },
    {
        "index": 6,
        "icon": "Fill_Phials_2.png",
        "label": "Fill Phials Near",
        "action": charge_blade.fill_phials_2,
    },
    {
        "index": 8,
        "icon": "SAED_2.png",
        "label": "SAED 2",
        "action": charge_blade.saed_combo_2,
    },
    {
        "index": 9,
        "icon": "Savage_Axe_Finisher_2.png",
        "label": "S. Axe Combo",
        "action": charge_blade.savage_axe_combo,
    },
    {
        "index": 10,
        "icon": "Combo_1.png",
        "label": "Full Combo Far",
        "action": charge_blade.charge_blade_sword_combo,
    },
    {
        "index": 11,
        "icon": "Combo_2.png",
        "label": "Full Combo Near",
        "action": charge_blade.charge_blade_sword_combo_2,
    },
    {
        "index": 13,
        "icon": "SAED_1.png",
        "label": "SAED",
        "action": charge_blade.saed_combo,
    },
    {
        "index": 14,
        "icon": "Savage_Axe_Finisher_1.png",
        "label": "S. Axe Finisher",
        "action": charge_blade.savage_axe_finisher,
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


def init_streamdeck():
    streamdecks = DeviceManager().enumerate()
    print(
        f"Found {len(streamdecks)} Stream Deck(s). Using the first visual Stream Deck."
    )

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

    if debug:
        print(
            "Opened '{}' device (serial number: '{}', fw: '{}')".format(
                deck.deck_type(), deck.get_serial_number(), deck.get_firmware_version()
            )
        )

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
    currentDeck.set_key_callback(key_change_callback)
    return currentDeck


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    global debug
    debug = args.debug
    print(f"Debug: {debug}")

    currentDeck = init_streamdeck()

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

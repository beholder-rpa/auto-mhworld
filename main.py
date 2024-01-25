from win32gui import GetWindowText, GetForegroundWindow

import argparse
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
from colorama import Style, Fore, init as colorama_init
import time
from modules.charge_blade import ChargeBlade
from modules.charge_blade_actions_original import get_charge_blade_actions_original
from modules.charge_blade_actions_xl import get_charge_blade_actions_xl

from modules.deckard import init_streamdeck
from modules.sounds import sounds

colorama_init()
MHW_WINDOW_NAME = "Monster Hunter: World"

debug = False
keyboard = KeyboardController()
mouse = MouseController()
currentDeck = None
actions = []

charge_blade = ChargeBlade(
    mouse,
    keyboard,
    sounds,
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    return args


def main():
    print(f"{Fore.LIGHTMAGENTA_EX}Starting Auto MH:World ...{Style.RESET_ALL}")

    args = parse_args()
    currentDeck = init_streamdeck(
        lambda: get_charge_blade_actions_original(charge_blade),
        lambda: get_charge_blade_actions_xl(charge_blade),
        args.debug,
    )

    debug = args.debug

    if debug:
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

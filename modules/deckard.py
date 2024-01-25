from PIL import Image, ImageDraw, ImageFont
from StreamDeck.ImageHelpers import PILHelper
from StreamDeck.DeviceManager import DeviceManager
import os

# Folder location of image assets used by this example.
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "..", "assets")


# Generates a custom tile with run-time generated text and custom image via the
# PIL module.
def render_key_image(deck, icon_filename, font_filename, label_text):
    # Resize the source image asset to best-fit the dimensions of a single key,
    # leaving a margin at the bottom so that we can draw the key title
    # afterwards.
    icon = Image.open(icon_filename)
    image = PILHelper.create_scaled_key_image(deck, icon, margins=[0, 0, 20, 0])

    # Load a custom TrueType font and use it to overlay the key index, draw key
    # label onto the image a few pixels from the bottom of the key.
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_filename, 10)
    draw.text(
        (image.width / 2, image.height - 5),
        text=label_text,
        font=font,
        anchor="ms",
        fill="white",
    )

    return PILHelper.to_native_key_format(deck, image)


# Returns styling information for a key based on its position and state.
def get_key_style(deck, key, state):
    # Last button in the example application is the exit button.
    exit_key_index = deck.key_count() - 1

    if key == exit_key_index:
        name = "exit"
        icon = "{}.png".format("Exit")
        font = "Roboto-Regular.ttf"
        label = "Bye" if state else "Exit"
    else:
        name = "emoji"
        icon = "{}.png".format("Pressed" if state else "Released")
        font = "Roboto-Regular.ttf"
        label = "Pressed!" if state else "Key {}".format(key)

    return {
        "name": name,
        "icon": os.path.join(ASSETS_PATH, "images", icon),
        "font": os.path.join(ASSETS_PATH, "fonts", font),
        "label": label,
    }


# Creates a new key image based on the key index, style and current key state
# and updates the image on the StreamDeck.
def update_key_image(deck, key, icon, label, font="Roboto-Regular.ttf"):
    font = os.path.join(ASSETS_PATH, "fonts", font)
    icon = os.path.join(ASSETS_PATH, "images", icon)

    # Generate the custom key with the requested image and label.
    image = render_key_image(deck, icon, font, label)

    # Use a scoped-with on the deck to ensure we're the only thread using it
    # right now.
    with deck:
        # Update requested key with the generated image.
        deck.set_key_image(key, image)


def init_streamdeck(
    get_actions_original: lambda: list,
    get_actions_xl: lambda: list,
    debug: bool = False,
):
    streamdecks = DeviceManager().enumerate()
    print(
        f"Found {len(streamdecks)} Stream Deck(s). Using the first visual Stream Deck."
    )

    # Get the first streamdeck where is_visual is True
    for deck in streamdecks:
        if deck.is_visual():
            deckType = deck.deck_type()
            print(f"Using {deck.deck_type()} as the Stream Deck.")
            currentDeck = deck
            if deckType == "Stream Deck XL":
                actions = get_actions_xl()
            elif deckType == "Stream Deck Original":
                actions = get_actions_original()
            else:
                print(f"Unknown deck type: {deckType}")
                exit()
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

    currentDeck.set_key_callback(key_change_callback)
    return currentDeck

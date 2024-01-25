import os
import simpleaudio as sa

# Folder location of sound assets
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "..", "assets")

# Initialize an empty dictionary for sounds
sounds = {}

# Load all .wav files in the directory
for file_name in os.listdir(os.path.join(ASSETS_PATH, "sounds")):
    if file_name.endswith(".wav"):
        sound_name = file_name[:-4]  # Removes the '.wav' extension
        sounds[sound_name] = sa.WaveObject.from_wave_file(
            os.path.join(ASSETS_PATH, "sounds", file_name)
        )

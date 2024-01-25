from pynput.keyboard import Key
from time import sleep

class Shortcuts:
    def __init__(self, mouse, keyboard, sounds):
        self.mouse = mouse
        self.keyboard = keyboard
        self.sounds = sounds

        # define functions for each shortcut, f1-f4, 1-8
        for f_key in [Key.f1, Key.f2, Key.f3, Key.f4]:
          for i in range(1, 8):
              setattr(self, f"shortcut_{f_key.name.lower()}_{i}", lambda nk=str(i), solo=False, fk=f_key: self.generic_shortcut(fk, nk, solo))
        

    def generic_shortcut(self, functionKey, numberKey, solo):
        if solo:
            self.sounds["alert"].play()

        self.keyboard.press(functionKey)
        sleep(0.25)
        self.keyboard.release(functionKey)

        self.keyboard.press(numberKey)
        sleep(0.25)
        self.keyboard.release(numberKey)

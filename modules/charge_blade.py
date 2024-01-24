from pynput.mouse import Button
from time import sleep


class ChargeBlade:
    def __init__(self, mouse, keyboard, sounds):
        self.mouse = mouse
        self.keyboard = keyboard
        self.sounds = sounds

    # Bank the Phials, aka Charge Phials
    def bank_it(self, solo=False):
        if solo:
            self.sounds["start"].play()
        # R+B
        self.mouse.press(Button.x2)
        self.mouse.press(Button.right)
        sleep(0.25)
        self.mouse.release(Button.right)
        self.mouse.release(Button.x2)
        if solo:
            self.sounds["stop"].play()

    def fill_phials(self, solo=False):
        if solo:
            self.sounds["start"].play()

        # Y+B
        self.mouse.press(Button.x1)
        sleep(0.25)
        self.mouse.release(Button.x1)
        sleep(0.5)  # Since we're lunging, we're slightly slower to the charge.

        # Hold B
        self.mouse.press(Button.right)
        sleep(1)
        self.mouse.release(Button.right)
        sleep(0.25)

        # Y
        self.mouse.press(Button.left)
        sleep(0.25)
        self.mouse.release(Button.left)
        sleep(0.5)

        # R+B
        self.bank_it()

        if solo:
            self.sounds["stop"].play()

    def fill_phials_2(self, solo=False):
        if solo:
            self.sounds["start"].play()
        # Y + Hold B (release) + Y + (Hold RT + B)

        # Y + Hold B (release)
        self.mouse.press(Button.left)
        sleep(0.25)
        self.mouse.release(Button.left)
        sleep(0.25)

        # Hold B
        self.mouse.press(Button.right)
        sleep(1)
        self.mouse.release(Button.right)
        sleep(0.25)

        # Y
        self.mouse.press(Button.left)
        sleep(0.25)
        self.mouse.release(Button.left)
        sleep(0.5)

        # R+B
        self.bank_it()

        if solo:
            self.sounds["stop"].play()

    def charge_shield(self, solo=False):
        if solo:
            self.sounds["start"].play()
            self.mouse.press(Button.x1)
            sleep(0.25)
            self.mouse.release(Button.x1)
            sleep(1)

        # Y+B
        self.mouse.press(Button.x1)
        sleep(0.25)
        self.mouse.release(Button.x1)
        sleep(1)

        # Y+B
        self.mouse.press(Button.x1)
        sleep(0.25)
        self.mouse.release(Button.x1)
        sleep(0.5)

        # R2
        self.mouse.press(Button.x2)
        sleep(0.25)
        self.mouse.release(Button.x2)
        if solo:
            self.sounds["stop"].play()

    def charge_sword(self, solo=False):
        if solo:
            self.sounds["start"].play()
        # R+B
        self.mouse.press(Button.x2)
        self.mouse.press(Button.right)
        sleep(0.25)
        self.mouse.release(Button.right)
        self.mouse.release(Button.x2)
        sleep(0.5)

        # Hold Y
        self.mouse.press(Button.left)
        sleep(2)
        self.mouse.release(Button.left)
        if solo:
            self.sounds["stop"].play()

    def charge_blade_sword_combo(self, solo=False):
        if solo:
            self.sounds["start"].play()
        # Y+B, hold B, Y, R+B, Y+B, Y+B, Y+B, R2, R+B, hold Y
        # Left+Right, Hold Right, Left, Ctrl+Right, Left+Right, Left+Right, Ctrl, Ctrl+Left, Hold Left then release

        self.fill_phials()
        sleep(0.25)

        # Charge Shield
        # Y+B
        self.mouse.press(Button.x1)
        sleep(0.25)
        self.mouse.release(Button.x1)
        sleep(1)  # If we don't wait long enough, it does an elemental discharge

        # Y+B
        self.mouse.press(Button.x1)
        sleep(0.25)
        self.mouse.release(Button.x1)
        sleep(0.5)  # If we don't wait long enough, it completes the SAED

        # This cancels the SAED, charging the shield
        self.mouse.press(Button.x2)
        sleep(1.25)  # If we don't wait long enough, we go into a morph slash
        # Then we charge the sword
        self.mouse.press(Button.right)
        sleep(0.25)
        self.mouse.release(Button.right)
        self.mouse.press(Button.left)
        sleep(
            2.5
        )  # The charge ls lengthy, if we don't wait long enough, it's just a return slash
        self.mouse.release(Button.left)
        self.mouse.release(Button.x2)

        if solo:
            self.sounds["stop"].play()

    def charge_blade_sword_combo_2(self, solo=False):
        if solo:
            self.sounds["start"].play()
        # Y + Hold B (release) + Y + (Hold RT + B) + Y + Hold B (Release) + (Y+B) + (Y+B) + (Hold RT + B + Hold Y + Release)

        self.fill_phials_2()
        sleep(0.25)

        # Y + Hold B (release)
        self.mouse.press(Button.left)
        sleep(0.25)
        self.mouse.release(Button.left)
        sleep(1.25)

        self.mouse.press(Button.right)
        sleep(0.5)
        self.mouse.release(Button.right)
        sleep(1)

        # Charge Shield
        # Y+B
        self.mouse.press(Button.x1)
        sleep(0.25)
        self.mouse.release(Button.x1)
        sleep(0.5)

        # Y+B
        self.mouse.press(Button.x1)
        sleep(0.25)
        self.mouse.release(Button.x1)
        sleep(0.5)

        # This cancels the SAED, charging the shield
        self.mouse.press(Button.x2)
        sleep(1)
        # Then we charge the sword
        self.mouse.press(Button.right)
        sleep(0.25)
        self.mouse.release(Button.right)
        sleep(0.5)
        self.mouse.press(Button.left)
        sleep(2)  # The charge ls lengthy
        self.mouse.release(Button.left)
        self.mouse.release(Button.x2)

        if solo:
            self.sounds["stop"].play()

    def saed_combo(self, solo=False):
        if solo:
            self.sounds["start"].play()

        # Morph to Axe
        # R+Y
        self.mouse.press(Button.x2)
        self.mouse.press(Button.left)
        sleep(0.25)
        self.mouse.release(Button.left)
        self.mouse.release(Button.x2)
        sleep(1.5)

        # Y+B
        self.mouse.press(Button.left)
        self.mouse.press(Button.right)
        sleep(0.25)
        self.mouse.release(Button.left)
        self.mouse.release(Button.right)
        if solo:
            self.sounds["stop"].play()

    def saed_combo_2(self, solo: bool = False):
        if solo:
            self.sounds["start"].play()

        # Morph to Axe
        # R+Y
        self.mouse.press(Button.x2)
        self.mouse.press(Button.left)
        sleep(0.25)
        self.mouse.release(Button.left)
        self.mouse.release(Button.x2)
        sleep(2)

        # B
        self.mouse.press(Button.right)
        sleep(0.25)
        self.mouse.release(Button.right)
        sleep(1)

        # B
        self.mouse.press(Button.right)
        sleep(0.25)
        self.mouse.release(Button.right)
        if solo:
            self.sounds["stop"].play()

    def savage_axe_combo(self, solo: bool = False):
        if solo:
            self.sounds["start"].play()
        # Morph to Axe
        # R+Y
        self.mouse.press(Button.x2)
        self.mouse.press(Button.left)
        sleep(0.25)
        self.mouse.release(Button.left)
        self.mouse.release(Button.x2)
        sleep(2)

        # Y+B
        self.mouse.press(Button.x1)
        sleep(0.25)
        self.mouse.release(Button.x1)
        sleep(1)

        # C
        self.keyboard.press("c")
        sleep(0.25)
        self.keyboard.release("c")
        sleep(3.0)

        # Controversial, morph back to sword
        self.mouse.press(Button.x2)
        sleep(0.25)
        self.mouse.release(Button.x2)

        if solo:
            self.sounds["stop"].play()

    def savage_axe_finisher(self, solo: bool = False):
        if solo:
            self.sounds["start"].play()
        # Morph to Axe
        # R+Y
        self.mouse.press(Button.x2)
        self.mouse.press(Button.left)
        sleep(0.25)
        self.mouse.release(Button.left)
        self.mouse.release(Button.x2)
        sleep(2)

        # Y+B
        self.mouse.press(Button.x1)
        sleep(0.25)
        self.mouse.release(Button.x1)
        sleep(1)

        # C
        self.keyboard.press("c")
        sleep(0.25)
        self.keyboard.release("c")
        sleep(3.25)

        # now we do the finisher
        self.mouse.press(Button.left)
        self.mouse.press(Button.right)
        sleep(0.25)
        self.mouse.release(Button.left)
        self.mouse.release(Button.right)

        if solo:
            self.sounds["stop"].play()

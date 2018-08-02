#!/usr/bin/env python3

import pyscreenshot as ImageGrab
from PIL import ImageFilter, Image
import os

h_dir = os.getenv("HOME")

pepe_Width = 813 / 2.5 # Division needed to resize the image
pepe_Hight = 976 / 2.5 # Division needed to resize the image

def __init__():
    # takes the screenshot with scrot and grabs the size
    screenshot = ImageGrab.grab(backend="scrot")
    width, height = screenshot.size

    # opens the pepe and the phrase img
    pepe_layer = Image.open(h_dir+"/i3lock_pepe/Pepe.png")
    phrase_layer = Image.open(h_dir+"/i3lock_pepe/phrase.png")

    # blurs the screenshot and resizes the image
    img_blur = screenshot.filter(ImageFilter.GaussianBlur(6)) # Blurs the sreenshot
    pepe_resized = pepe_layer.resize((int(pepe_Width), int(pepe_Hight))) # Resizes the pepe image

    # pastes the pepe and the text into the screenshot
    img_blur.paste(pepe_resized, (0, int(height-pepe_Hight)), mask=pepe_resized)
    img_blur.paste(phrase_layer, (280, 350), mask=phrase_layer)

    # saves the edited image to the /tmp/ directory
    img_blur.save("/tmp/Pepe_Screenshot.png")
    # runs the i3lock command
    os.system('i3lock -i /tmp/Pepe_Screenshot.png --bar-indicator --bar-position=748 --bar-color A0000000 --keyhlcolor=b58900FF --ringwrongcolor=dc322FFF --ringvercolor=268bd2FF --veriftext= --wrongtext= ' )

if __name__ == "__main__":
    __init__()


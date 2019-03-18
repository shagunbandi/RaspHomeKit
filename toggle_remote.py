# PIGPIO_ADDR=10.109.2.165 python3 toggle_remote.py
# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=raspberrypi.local python3 toggle_remote.py
# https://gpiozero.readthedocs.io/en/stable/remote_gpio.html

from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from signal import pause
from PIL import ImageGrab
from PIL import Image
import time, os, colorsys



# factory = PiGPIOFactory(host='raspberrypi.local')
factory = PiGPIOFactory(host='10.109.2.165')

led_r = PWMLED(24, pin_factory=factory)
led_g = PWMLED(22, pin_factory=factory)
led_b = PWMLED(17 , pin_factory=factory)

def set_colour(red, green, blue):
 
    led_r.value = red/255
    led_b.value = blue/255
    led_g.value = green/255

    print("Changing")

def main():
    rx = 64
    ry = 36
    totpixels = rx * ry

    # led_r.pulse()
    # led_b.pulse()
    # led_g.pulse()



    # screen scanning loop
    while True:
        img = ImageGrab.grab()
        t1 = time.perf_counter()
        # let PIL to shrink the image into a more manageable size
        # (just few ms in your average machine)
        img = img.resize((rx, ry))
        red = green = blue = 0
        for y in range(0, img.size[1]):
            for x in range(0, img.size[0]):
                c = img.getpixel((x,y))
                red = red + c[0]
                green = green + c[1]
                blue = blue + c[2]

        red = red / totpixels
        green = green / totpixels
        blue = blue / totpixels

        # for y in range(0, img.size[1]):
        #     for x in range(0, int(img.size[0]/4)):
        #         c = img.getpixel((x,y))
        #         red = red + c[0]
        #         green = green + c[1]
        #         blue = blue + c[2]
        #     for x in range(int(img.size[0]*3/4), img.size[0]):
        #         c = img.getpixel((x,y))
        #         red = red + c[0]
        #         green = green + c[1]
        #         blue = blue + c[2]

        # for x in range(0, img.size[0]):
        #     for y in range(0, int(img.size[1]/4)):
        #         c = img.getpixel((x,y))
        #         red = red + c[0]
        #         green = green + c[1]
        #         blue = blue + c[2]
        #     for y in range(int(img.size[1]*3/4), img.size[1]):
        #         c = img.getpixel((x,y))
        #         red = red + c[0]
        #         green = green + c[1]
        #         blue = blue + c[2]

        # totpixxxies = img.size[1] * img.size[0] / 2 + img.size[0] * img.size[1] / 2

        # red = red / totpixxxies
        # green = green / totpixxxies
        # blue = blue / totpixxxies

        print ("\rRGB %3d %3d %3d" % (red, green, blue), )
        # print(t1)

        set_colour(red, green, blue)
        t2 = time.perf_counter()

        print ("- Time %2.4f" % (t2-t1), )

        time.sleep(1/500)
    # pause()


if __name__ == '__main__':
    main()

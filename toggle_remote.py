# PIGPIO_ADDR=10.109.2.165 python3 toggly_remote.py
# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.1.3 python3 toggly_remote.py
# https://gpiozero.readthedocs.io/en/stable/remote_gpio.html

from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='raspberrypi.local')
# factory4 = PiGPIOFactory(host='192.168.1.4')

led_r = PWMLED(17, pin_factory=factory)
led_g = PWMLED(24, pin_factory=factory)
led_b = PWMLED(22, pin_factory=factory)

def set_colour(red, green, blue):
 
    led_r.value = red/255
    led_b.value = blue/255
    led_g.value = green/255

    print("Changing")



from PIL import ImageGrab
from PIL import Image
import time, os, colorsys

def main():
    rx = 64
    ry = 36
    totpixels = rx * ry

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

        print ("\rRGB %3d %3d %3d" % (red, green, blue), )
        # print(t1)

        set_colour(red, green, blue)
        t2 = time.perf_counter()

        print ("- Time %2.4f" % (t2-t1), )

        time.sleep(1/500)

if __name__ == '__main__':
    main()

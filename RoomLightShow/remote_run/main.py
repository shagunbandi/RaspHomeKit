from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='raspberrypi.local')

blue = LED(23,pin_factory=factory)
red = LED(24,pin_factory=factory)
green = LED(25,pin_factory=factory)

while True:
    red.on()
    sleep(1)
    blue.on()
    sleep(1)
    green.on()
    sleep(1)
    red.off()
    blue.off()
    green.off()
    sleep(1)


    # sudo pigpiod
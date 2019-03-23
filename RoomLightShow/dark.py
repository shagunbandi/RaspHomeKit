# PIGPIO_ADDR=10.109.2.165 python3 toggle_remote.py
# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=raspberrypi.local python3 toggle_remote.py
# https://gpiozero.readthedocs.io/en/stable/remote_gpio.html

from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import soundcard as sc
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time


factory = PiGPIOFactory(host='raspberrypi.local')
# factory = PiGPIOFactory(host='10.109.2.165')

red_bulb = LED(2, pin_factory=factory)
red_bulb.on()

green_bulb = LED(3, pin_factory=factory)
green_bulb.on()


def blink(_LED, _SLEEP=0.05, _TIMES=1):
    _LED.off()
    sleep(_SLEEP)
    _LED.on()
    sleep(_SLEEP)


def turn_on(_LED):
    _LED.off()


def turn_off(_LED):
    _LED.on()



channel = 1

# turn_on(red_bulb)


samplerate = 44.1e3
numframes = 44.1e2
T = 1.0 / samplerate
x = np.linspace(0.0, numframes*T, numframes)
xf = np.linspace(0.0, 1.0/(2.0*T), numframes//2)

input = sc.all_microphones()[3]
print(input)
prev = 0
num1 = num2 = 0
with input.recorder(samplerate) as mic:
    for i in range(200000):
        y = mic.record(numframes)
        yf = np.fft.fft(y[:, channel])
        num = 2.0/numframes * np.abs(yf[10])
        num2 = num1
        num1 = num

        if(i >= 2):
            avg = (num + num1 + num2) / 3.0
            # avg = num
            # print(1/numframes)
            print(avg)
            # if avg > 0.015:
            #     turn_on(red_bulb)
            # if avg < 0.015:
            #     turn_off(red_bulb)

            # if avg >= 0.06:
            # 	blink(green_bulb)

            # if avg > 0.16:
            #     blink(red_bulb)
            #     turn_on(red_bulb)

            if avg <= 0.06:
                turn_off(red_bulb)
                turn_off(green_bulb)
            
            if avg >= 0.03 and avg < 0.06:
                blink(green_bulb)
                turn_on(red_bulb)

            if avg >= 0.09:
                turn_on(red_bulb)
                blink(green_bulb)

            prev = num


            #     turn_on(green_bulb)
            # if num < 0.03:
            #     turn_off(green_bulb)


            # x = [1,2 ,3,4,5,6]
            # y = [1,2 ,3,4,5,6]
            # plt.clf()
            # # plt.ylim(0, 0.5)
            # # plt.plot(xf[:], 2.0/numframes * np.abs(yf[0:numframes//2]))
            # plt.plot(x, y)
            # plt.grid()
            # # plt.pause(0.01)
            # plt.show();



# PIGPIO_ADDR=10.109.2.165 python3 toggle_remote.py
# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=raspberrypi.local python3 toggle_remote.py
# https://gpiozero.readthedocs.io/en/stable/remote_gpio.html

import sys

from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
import soundcard as sc
import numpy as np
import time

from play_like_this import play

# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt

CHANNEL = 1
SAMPLERATE = 44.1e3
NUMFRAMES = 44.1e2
MIC_NUM = 3
RED_PIN = 3
GREEN_PIN = 2


def main(RED, GREEN):

    channel = CHANNEL
    samplerate = SAMPLERATE
    numframes = NUMFRAMES

    T = 1.0 / samplerate
    x = np.linspace(0.0, numframes*T, numframes)
    xf = np.linspace(0.0, 1.0/(2.0*T), numframes//2)

    input = sc.all_microphones()[MIC_NUM]
    print(input)

    with input.recorder(samplerate) as mic:
        for i in range(200000):
            y = mic.record(numframes)
            yf = np.fft.fft(y[:, channel])
            
            ampl = 2.0/numframes * np.abs(yf[10])                
            print(ampl)

            play(ampl, RED, GREEN, sys.argv)


def set_up_lights(RED_PIN=RED_PIN, GREEN_PIN=GREEN_PIN):
    factory = PiGPIOFactory(host='raspberrypi.local')
    # factory = PiGPIOFactory(host='10.109.2.165')
    RED = LED(RED_PIN, pin_factory=factory)
    GREEN = LED(GREEN_PIN, pin_factory=factory)
    return RED, GREEN

if __name__ == "__main__":
    RED, GREEN = set_up_lights()
    main(RED, GREEN)


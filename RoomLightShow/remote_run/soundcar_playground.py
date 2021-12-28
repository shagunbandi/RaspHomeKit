# PIGPIO_ADDR=10.109.2.165 python3 toggle_remote.py
# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=raspberrypi.local python3 toggle_remote.py
# https://gpiozero.readthedocs.io/en/stable/remote_gpio.html

import sys

from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
import soundcard as sc
import numpy as np
import time

import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

CHANNEL = 0
SAMPLERATE = int(44.1e3)
NUMFRAMES = int(44.1e2)
MIC_NUM = 2
RED_PIN = 3
GREEN_PIN = 2
PLAY_NUM = 1


def main():
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
            plt.clf()
            plt.ylim(0, 0.1)
            plt.xlim(0, 500)
            plt.plot(xf[:], 2.0/numframes * np.abs(yf[0:numframes//2]))
            
            plt.grid()
            plt.pause(0.01)

        plt.show()



if __name__ == "__main__":
    main()


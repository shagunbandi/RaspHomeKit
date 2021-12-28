import sys
import matplotlib.pyplot as plt
import soundcard as sc
import numpy as np
import time
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from play_like_this import play, play_no_music
import matplotlib

matplotlib.use('TkAgg')

CHANNEL = 0
SAMPLERATE = int(44.1e3)
NUMFRAMES = int(44.1e2)
MIC_NUM = 2
RED_PIN = 23
BLUE_PIN = 24
GREEN_PIN = 25
PLAY_NUM = 1


def main(RED, GREEN, BLUE):

    try:
        play_num = int(sys.argv[1])
    except:
        play_num = PLAY_NUM

    print(play_num)
    if play_num > 100:
        play_no_music(RED, GREEN, BLUE, play_num)
    else:
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
                play(ampl, RED, GREEN, BLUE, play_num)


def set_up_lights(RED_PIN=RED_PIN, GREEN_PIN=GREEN_PIN, BLUE_PIN=BLUE_PIN):
    factory = PiGPIOFactory(host='raspberrypi.local')
    # factory = PiGPIOFactory(host='10.109.2.165')
    RED = LED(RED_PIN, pin_factory=factory)
    GREEN = LED(GREEN_PIN, pin_factory=factory)
    BLUE = LED(BLUE_PIN, pin_factory=factory)
    return RED, GREEN, BLUE


if __name__ == "__main__":
    RED, GREEN, BLUE = set_up_lights()
    main(RED, GREEN, BLUE)

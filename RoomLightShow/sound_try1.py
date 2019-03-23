import soundcard as sc 
import numpy as np 
# import matplotlib.pyplot as plt
import time
from time import sleep



from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory


factory = PiGPIOFactory(host='raspberrypi.local')
# factory = PiGPIOFactory(host='10.109.2.165')

red_bulb = LED(3, pin_factory=factory)
red_bulb.on()

green_bulb = LED(2, pin_factory=factory)
green_bulb.on()


def blink(_LED, _SLEEP=0.1, _TIMES=1):
    _LED.off()
    sleep(_SLEEP)
    _LED.on()
    sleep(_SLEEP)


while True:
	blink(red_bulb)
	blink(green_bulb)


# channel = 1
# samplerate = 48000
# numframes = 4800
# T = 1.0 / samplerate
# x = np.linspace(0.0, numframes*T, numframes)
# xf = np.linspace(0.0, 1.0/(2.0*T), numframes//2)

# input = sc.all_microphones(include_loopback=True)[0]
# print(input)
# with input.recorder(samplerate) as mic:
#     for i in range(2000):
#         y = mic.record(numframes)
#         yf = np.fft.fft(y[:, channel])


#         num = 2.0/numframes * np.abs(yf[20])
#         if num > 0.02 and num <= 0.4:
#             blink(red_bulb)
#         if num >= 0.4:
#             blink(green_bulb)


#         # plt.clf()
#         # plt.ylim(0, 0.5)
#         # plt.plot(xf[:], 2.0/numframes * np.abs(yf[0:numframes//2]))
#         # plt.grid()
#         # plt.pause(0.01)
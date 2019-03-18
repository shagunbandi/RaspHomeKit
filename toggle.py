#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This script toggles lights on and off using the phue library and a physical swi$
It is started on boot in /etc/rc.local with this line:
python /home/pi/light_button_control/light_button_control.py &
'''

from time import sleep
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)

on = True


def toggle_lights():
  global on
  print("toggling")
  if on:
    GPIO.setup(3, GPIO.OUT)
    on = False
  else:
    GPIO.setup(3, GPIO.IN)
    on = True


prev_input = 0

while True:
  print("something")
  toggle_lights()
  #update previous input
  time.sleep(0.5)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

import RPi.GPIO as GPIO



def lampon(request):
    GPIO.setmode(GPIO.BCM)
	GPIO.setup(2, GPIO.OUT)
	GPIO.output(2, True)

	return HttpResponse("Turned on")


def lampoff(request):
    GPIO.setmode(GPIO.BCM)
	GPIO.setup(2, GPIO.OUT)
	GPIO.output(2, False)

	return HttpResponse("Turned on")


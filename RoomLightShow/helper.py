from time import sleep

def turn_on(_LED):
    _LED.off()


def turn_off(_LED):
    _LED.on()


def blink(_LED, _SLEEP=0.01):
    turn_on(_LED)
    sleep(_SLEEP)
    turn_off(_LED)
    sleep(_SLEEP)


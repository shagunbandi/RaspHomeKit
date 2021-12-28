from helper import turn_off, turn_on, blink
from time import sleep

# import threading

BASE_0 = 0.06
BASE_1 = 0.10
BASE_2 = 0.13
BASE_3 = 0.18
BASE_4 = 0.3
_SLEEP = 1


def play(ampl, RED, GREEN, BLUE, play_num):

    if play_num == -1:
        only_red(ampl, RED, GREEN, BLUE)

    elif play_num == -2:
        only_green(ampl, RED, GREEN, BLUE)

    elif play_num == -3:
        only_blue(ampl, RED, GREEN, BLUE)

    elif play_num == -4:
        both_tog(ampl, RED, GREEN, BLUE)

    elif play_num == 1:
        light_rand(ampl, RED, GREEN, BLUE)

    elif play_num == 2:
        dark_rand(ampl, RED, GREEN, BLUE)

    elif play_num == 3:
        less_blinks(ampl, RED, GREEN, BLUE)

    elif play_num == 4:
        even_less_blinks(ampl, RED, GREEN, BLUE)

    elif play_num == 5:
        even_even_less_blinks(ampl, RED, GREEN, BLUE)

    elif play_num == 6:
        no_blink(ampl, RED, GREEN, BLUE)

    elif play_num == 7:
        super_random(ampl, RED, GREEN, BLUE)


def play_no_music(RED, GREEN, BLUE, play_num):

    print("Playing No Music... ENjoy !!")

    if play_num == 101:
        print("Plaing RGB PnC")
        turn_off(RED)
        turn_off(BLUE)
        turn_off(GREEN)
        sleep(_SLEEP)

        while True:
            # 001
            turn_on(RED)
            sleep(_SLEEP)

            # 011
            turn_on(GREEN)
            sleep(_SLEEP)

            # 010
            turn_off(RED)
            sleep(_SLEEP)

            # 110
            turn_on(BLUE)
            sleep(_SLEEP)

            # 111
            turn_on(RED)
            sleep(_SLEEP)

            # 101
            turn_off(GREEN)
            sleep(_SLEEP)

            # 100
            turn_off(RED)
            sleep(_SLEEP)

            # 000
            turn_off(BLUE)
            sleep(_SLEEP)


def only_red(ampl, RED, GREEN, BLUE):
    print("playing only_red")
    turn_off(BLUE)
    turn_off(GREEN)
    turn_on(RED)
    if ampl >= BASE_0:
        blink(RED, 0.01)


def only_green(ampl, RED, GREEN, BLUE):
    print("playing only_green")
    turn_off(RED)
    turn_off(BLUE)
    turn_on(GREEN)
    if ampl >= BASE_0:
        blink(GREEN, 0.01)


def only_blue(ampl, RED, GREEN, BLUE):
    print("playing only_green")
    turn_off(RED)
    turn_off(GREEN)
    turn_on(BLUE)
    if ampl >= BASE_0:
        blink(GREEN, 0.01)


def both_tog(ampl, RED, GREEN, BLUE):
    print("playing both_tog")
    turn_on(RED)
    turn_on(GREEN)
    if ampl >= BASE_0:
        blink(GREEN, 0.01)
        blink(RED, 0.01)


def light_rand(ampl, RED, GREEN, BLUE):
    print("playing on light_rand")
    if ampl <= 0.06:
        turn_on(RED)
        turn_on(GREEN)
    else:
        turn_off(RED)
        turn_off(GREEN)
    if ampl >= 0.03 and ampl < 0.06:
        blink(GREEN)
        turn_off(RED)
    if ampl >= 0.09:
        turn_on(RED)
        turn_off(GREEN)


def dark_rand(ampl, RED, GREEN, BLUE):
    print("playing on dark_rand")
    if ampl <= 0.06:
        turn_off(RED)
        turn_off(GREEN)

    if ampl >= 0.03 and ampl < 0.06:
        blink(GREEN)
        turn_on(RED)

    if ampl >= 0.09:
        turn_on(RED)
        blink(GREEN)


def less_blinks(ampl, RED, GREEN, BLUE):
    print("playing on less_blinks")
    if ampl <= BASE_1:
        turn_on(RED)
        turn_on(GREEN)

    if ampl >= BASE_1 and ampl < BASE_2:
        blink(GREEN)
        turn_off(RED)

    if ampl >= BASE_2 and ampl < BASE_3:
        turn_on(RED)
        turn_off(GREEN)

    if ampl >= BASE_3:
        blink(RED)
        blink(GREEN)


def even_less_blinks(ampl, RED, GREEN, BLUE):
    print("playing on even_less_blinks")
    if ampl <= BASE_2:
        turn_on(RED)
        turn_on(GREEN)

    if ampl >= BASE_2 and ampl < BASE_3:
        blink(GREEN)
        turn_off(RED)

    if ampl >= BASE_3 and ampl < BASE_4:
        turn_on(RED)
        turn_off(GREEN)

    if ampl >= BASE_4:
        blink(RED)
        blink(GREEN)


def even_even_less_blinks(ampl, RED, GREEN, BLUE):
    print("playing on even_even_less_blinks")
    if ampl <= BASE_2:
        turn_on(RED)
        turn_on(GREEN)

    if ampl >= BASE_2 and ampl < BASE_3:
        turn_on(GREEN)
        turn_off(RED)

    if ampl >= BASE_3 and ampl <= BASE_4:
        turn_on(RED)
        turn_off(GREEN)

    if ampl >= BASE_4:
        blink(RED)
        blink(GREEN)


def no_blink(ampl, RED, GREEN, BLUE):
    print("playing on no_blink")
    if ampl <= BASE_0:
        turn_on(RED)
        turn_on(GREEN)
        turn_on(BLUE)

    if ampl >= BASE_0 and ampl < BASE_1:
        turn_on(GREEN)
        turn_off(RED)

    if ampl >= BASE_1:
        turn_on(RED)
        turn_off(GREEN)


def super_random(ampl, RED, GREEN, BLUE):
    print("playing on super_random")
    if ampl <= BASE_0:
        turn_on(RED)
        turn_on(GREEN)
    if ampl > BASE_0 and ampl <= BASE_1:
        blink(RED)
        turn_on(GREEN)
    if ampl > BASE_1 and ampl <= BASE_2:
        turn_on(GREEN)
        turn_on(RED)
    if ampl >= BASE_2 and BASE_3:
        turn_off(RED)
        turn_off(GREEN)
    if ampl >= BASE_3 and ampl < BASE_4:
        blink(GREEN)
        turn_off(RED)
    if ampl >= BASE_4:
        blink(RED)
        blink(GREEN)

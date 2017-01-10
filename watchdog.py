import RPi.GPIO as GPIO
import config
import opendoor
import closedoor
import time
import datetime


def isdoorclosed():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config.REED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    if GPIO.input(config.REED):
        print('Door status: CLOSED')
    else:
        print('Door status: OPEN')
    return not GPIO.input(config.REED)


def watch():
    while True:
        if not isclosed():
            #notifyonopen()
            print('Door is opening...')
            opentime = datetime.datetime.now()
            while not isclosed():
                opencount = datetime.datetime.now()
                print('Door has been open for ')


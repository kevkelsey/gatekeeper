import RPi.GPIO as GPIO
import config
import open
import close
import time
import datetime


def isclosed():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(port_or_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    if GPIO.input(config.REED):
        print('Door status: CLOSED')
    else:
        print('Door status: OPEN')
    return GPIO.input(config.REED)


def watch():
    while True:
        if not isclosed():
            notifyonopen()
            print('Door is opening...')
            opentime = datetime.datetime.now()
            while not isclosed():
                opencount = datetime.datetime.now()
                print('Door has been open for ')


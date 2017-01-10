import RPi.GPIO as GPIO
import config
import opendoor
import closedoor
import time
import requests
import datetime


def isdoorclosed():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config.REED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    doorclosed = not GPIO.input(config.REED)
    if doorclosed:
        print('Door status: CLOSED')
    else:
        print('Door status: OPEN')
    GPIO.cleanup(config.REED)
    return doorclosed

def notifyopen()
    requests.get(config.openKEY)

def notifyclose()
    requests.get(config.closeKEY)


def watch():
    while True:
        if not isclosed():
            #notifyonopen()
            print('Door is opening...')
            opentime = datetime.datetime.now()
            while not isclosed():
                opencount = datetime.datetime.now()
                print('Door has been open for ')


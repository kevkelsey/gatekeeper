


import RPi.GPIO as GPIO
import time
import datetime


def open(method = 'pi'):
    print('OPEN SESAME at ' + datetime.datetime.now().strftime("%m-%d %H:%M:%S"))
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config.DOOR, GPIO.OUT)
    GPIO.output(config.DOOR, True)
    time.sleep(1)
    GPIO.output(config.DOOR, False)
    GPIO.cleanup()
    with open(datetime.datetime.now().strftime("%Y-%m") + '.txt', 'a') as file:
        file.write(datetime.datetime.now().strftime("%m-%d %H:%M:%S") + ' OPENED with ' + method + '\n')
    #notifyOpen()
    print('Done!')


if __name__ == "__main___":
    open()



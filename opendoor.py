


import RPi.GPIO as GPIO
import time
import datetime
import watchdog
import config


def opendoor(method = 'pi'):
    if not watchdog.isdoorclosed():
        raise Exception('Door is already open. Script aborted')
    print('OPEN SESAME at ' + datetime.datetime.now().strftime("%m-%d %H:%M:%S"))
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config.DOOR, GPIO.OUT, initial = True)
    GPIO.output(config.DOOR, False)
    time.sleep(1)
    GPIO.output(config.DOOR, True)
    GPIO.cleanup()
    with open(datetime.datetime.now().strftime("%Y-%m") + '.txt', 'a') as file:
        file.write(datetime.datetime.now().strftime("%m-%d %H:%M:%S") + ' OPENED with ' + method + '\n')
    #notifyOpen()
    print('Done!')


if __name__ == "__main___":
    print('Running OPENDOOR()')
    opendoor()



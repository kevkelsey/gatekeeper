import RPi.GPIO as GPIO
import time
import datetime
import watchdog
import config


def closedoor(retries=0, method = 'pi'):
    if watchdog.isdoorclosed():
        raise Exception('Door already closed!')
    print('CLOSED FOR BUSINESS at ' + datetime.datetime.now().strftime("%m-%d %H:%M:%S"))
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config.DOOR, GPIO.OUT, initial = True)
    GPIO.output(config.DOOR, False)
    time.sleep(1)
    GPIO.output(config.DOOR, True)
    time.sleep(1)
    GPIO.cleanup()
    time.sleep(config.CLOSETIME)
    if watchdog.isdoorclosed():
        with open(datetime.datetime.now().strftime("%Y-%m") + '.txt', 'a') as file:
            file.write(datetime.datetime.now().strftime("%m-%d %H:%M:%S") + ' CLOSED with ' + method + '\n')
        watchdog.notifyclose()
        print('Done!')
    else:
        if retries < config.RETRIES:
            print('Door close failed, trying again in {} seconds'.format(config.RETRYTIME))
            time.sleep(config.RETRYTIME)
            closedoor(retries + 1, 'retry')
        else:
            print('Max retries hit.')



if __name__ == "__main__":
    print('Running closedoor()')
    closedoor()
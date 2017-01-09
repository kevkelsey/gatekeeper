import RPi.GPIO as GPIO
import time
import datetime
import watchdog


def close(retries=0, method = 'pi'):
    print('CLOSED FOR BUSINESS at ' + datetime.datetime.now().strftime("%m-%d %H:%M:%S"))
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config.DOOR, GPIO.OUT, initial = True)
    time.sleep(1)
    GPIO.output(config.DOOR, False)
    time.sleep(config.CLOSETIME)
    if watchdog.isclosed():
        GPIO.cleanup()
        with open(datetime.datetime.now().strftime("%Y-%m") + '.txt', 'a') as file:
            file.write(datetime.datetime.now().strftime("%m-%d %H:%M:%S") + ' CLOSED with ' + method + '\n')
        #notifyOpen()
        print('Done!')
    else:
        if retries < config.RETRIES:
            print('Door close failed, trying again in {} seconds'.format(config.RETRYTIME))
            time.sleep(config.RETRYTIME)
            GPIO.cleanup()
            close(retries + 1, 'retry')



if __name__ == "__main___":
    close()
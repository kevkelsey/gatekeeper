#!/usr/bin/env python3

import watchdog
import datetime

print('Running test...')
with open(datetime.datetime.now().strftime("%Y-%m") + '.txt', 'a') as file:
    file.write(datetime.datetime.now().strftime("%m-%d %H:%M:%S") + ' NO CHANGE testing file log\n')
watchdog.notifyopen()
print('Test done!')


# GPIO pin mapping
DOOR = 12
REED = 6

# Time it takes in seconds from switch push to full door closure
CLOSETIME = 20
RETRIES = 1

# Time in seconds to wait before retrying close operation
RETRYTIME = 20

# Maker keys
openKEY = 'https://maker.ifttt.com/trigger/door_open/with/key/GIq_WDg-g9UHWOMec8_hr'
closeKEY = 'https://maker.ifttt.com/trigger/door_closed/with/key/GIq_WDg-g9UHWOMec8_hr'

# Gatekeeper install path for use with apache
PATH = '/home/pi/gatekeeper/'
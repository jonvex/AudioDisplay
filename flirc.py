import os
import time
import errno
import threading
import activities
import I2C_LCD_driver

FIFO = '/tmp/jbvpipe'

try:
    os.mkfifo(FIFO)
except OSError as oe: 
    if oe.errno != errno.EEXIST:
        raise

#commands
VOLUME_UP_CMD = 0
VOLUME_DOWN_CMD = 1
SOURCE_TOSLINK_CMD = 2
SOURCE_USB_CMD = 3
POWER_ON_CMD = 4
POWER_OFF_CMD = 5


lcd = I2C_LCD_driver.LCD()
lcd.backlight(0)
activity = activities.Clock(lcd)
activity.start()



while True:
    with open(FIFO) as fifo:
        while True:
            data = fifo.read()
            if len(data) == 0:
                break
            if data == VOLUME_UP_CMD:
                if activity.activity() == activities.AUDIO_A:
                    activity.increase_volume()
            elif data == VOLUME_DOWN_CMD:
                if activity.activity() == activities.AUDIO_A:
                    activity.decrease_volume()
            elif data == SOURCE_TOSLINK_CMD:
                if activity.activity() == activities.AUDIO_A:
                    activity.set_source(activities.TOSLINK_VAL)
            elif data == SOURCE_USB_CMD:
                if activity.activity() == activities.AUDIO_A:
                    activity.set_source(activities.USB_VAL)
            elif data == POWER_OFF_CMD:
                if activity.activity() == activities.AUDIO_A:
                    activity = activities.Clock(lcd)
                    activity.start()
            elif data == POWER_ON_CMD:
                if activity.activity() == activities.CLOCK_A:
                    activity.stop()
                    time.sleep(1)
                    activity = activities.Audio(lcd)

            else:
                print("Unknown command" + data)
                



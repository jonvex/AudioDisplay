import clock
import time
import atexit

def exit_handler():
    time.sleep(2)
    mylcd.lcd_clear()
    mylcd.backlight(0)

atexit.register(exit_handler)


c = clock.clock()
while True:
    c.refresh_time()
    time.sleep(0.1)

import clock
import time
import atexit


c = clock.clock()

def exit_handler():
    time.sleep(0.5)
    c.clear()

atexit.register(exit_handler)


c.refresh_day()
while True:
    c.refresh_time(4)
    time.sleep(0.1)

import clock
import time
import atexit


c = clock.clock()

def exit_handler():
    time.sleep(2)
    c.clear()

atexit.register(exit_handler)



while True:
    c.refresh_time()
    time.sleep(0.1)

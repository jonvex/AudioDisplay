from lcd.I2C_LCD_driver import lcd
from lcd.clock import clock
import threading
import atexit

#display activities
START_A = 0
CLOCK_A = 1
END_A = 2

#amp states
AMP_OFF = 0
AMP_ON = 1
AMP_START = 2
AMP_STOP = 3


class audiodisplay:
    def __init__(self):
        self.__lcd = lcd()
        self.__lcd.backlight(0)
        self.__active = START_A
        self.__amp = AMP_OFF
        self.__lock = threading.Lock()
        self.__running = False
        self.__clock = None
        
    
    def run(self):
        self.__lock.acquire()
        self.__running = True
        while self.__running:
            if self.__amp == AMP_OFF and self.__active != CLOCK_A:
                self.__clock = clock(self.__lcd)
                self.__clock.start()
                self.__active = CLOCK_A
            self.__lock.release()
            self.__lock.acquire()
    
    def stop(self):
        with self.__lock:
            if self.__active == CLOCK_A:
                self.__active = END_A
                self.__clock.stop()
            self.__running = False
            self.__lcd.backlight(0)



a = audiodisplay()
atexit.register(audiodisplay.stop,a)
a.run()
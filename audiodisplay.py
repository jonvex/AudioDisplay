import activities
import minidsp
import I2C_LCD_driver
import threading
import atexit
import time


class AudioDisplay:
    def __init__(self):
        self.__lcd = I2C_LCD_driver.LCD()
        self.__lcd.backlight(0)
        self.__activity = None
        self.__lock = threading.Lock()
        self.__running = False
        self.__minidsp = minidsp.MiniDSP()
        self.__minidsp.start()
        
    
    def run(self):
        self.__lock.acquire()
        self.__running = True
        self.__activity = activities.Clock(self.__lcd)
        self.__activity.start()
        time.sleep(1)
        audioON = True
        while self.__running:
            if self.__activity.activity() == activities.CLOCK_A:
                if audioON:
                    self.__activity.stop()
                    time.sleep(1)
                    self.__activity = activities.Audio(self.__lcd, self.__minidsp)
                    self.__activity.start()
            if self.__activity.activity() == activities.AUDIO_A:
                if not audioON:
                    self.__activity.stop()
                    self.__activity = activities.Clock(self.__lcd)
                    self.__activity.start()
            self.__lock.release()
            time.sleep(0.1)
            self.__lock.acquire()
    
    def stop(self):
        with self.__lock:
            self.__activity.stop()
            self.__running = False
            self.__lcd.backlight(0)



a = AudioDisplay()
atexit.register(AudioDisplay.stop,a)
time.sleep(5)
a.run()
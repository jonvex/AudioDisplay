import lcd.I2C_LCD_driver
from datetime import datetime
import threading
import time


#custom character enums
TOP_RIGHT_CC = 0
TOP_CC = 1
LEFT_BAR_CC = 2
RIGHT_BAR_CC = 3
RIGHT_L_CC = 4
LEFT_L_CC = 5
DOT_CC = 6
EMPTY_CC = 128

#custom character bytes
top_right_cc = [0b00111,
	            0b00111,
	            0b00111,
                0b00000,
                0b00000,
                0b00000,
                0b00000,
                0b00000]

top_cc = [  0b11111,
            0b11111,
            0b11111,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000]

left_bar_cc = [ 0b11100,
                0b11100,
                0b11100,
                0b11100,
                0b11100,
                0b11100,
                0b11100,
                0b11100]

right_bar_cc = [0b00111,
                0b00111,
                0b00111,
                0b00111,
                0b00111,
                0b00111,
                0b00111,
                0b00111]

right_l_cc = [  0b11111,
                0b11111,
                0b11111,
                0b00111,
                0b00111,
                0b00111,
                0b00111,
                0b00111]

left_l_cc =  [  0b11111,
                0b11111,
                0b11111,
                0b11100,
                0b11100,
                0b11100,
                0b11100,
                0b11100]

dot_cc = [  0b00000,
	        0b00000,
            0b00000,
            0b01110,
            0b01110,
            0b01110,
            0b00000,
            0b00000]

customCC = [top_right_cc, top_cc, left_bar_cc, right_bar_cc, right_l_cc, left_l_cc, dot_cc]

#numbers made from custom characters
numbers = [EMPTY_CC, EMPTY_CC, EMPTY_CC, EMPTY_CC, EMPTY_CC, EMPTY_CC] * 11
numbers[0] = [LEFT_L_CC, RIGHT_L_CC, LEFT_BAR_CC, RIGHT_BAR_CC, TOP_CC, TOP_CC]
numbers[1] = [TOP_RIGHT_CC, LEFT_BAR_CC, EMPTY_CC, LEFT_BAR_CC, TOP_RIGHT_CC, TOP_CC]
numbers[2] = [TOP_CC, RIGHT_L_CC, LEFT_L_CC, TOP_CC, TOP_CC, TOP_CC]
numbers[3] = [TOP_CC, RIGHT_L_CC, TOP_RIGHT_CC, RIGHT_L_CC, TOP_CC, TOP_CC]
numbers[4] = [LEFT_BAR_CC, RIGHT_BAR_CC, TOP_CC, RIGHT_L_CC, EMPTY_CC, TOP_RIGHT_CC]
numbers[5] = [LEFT_L_CC, TOP_CC, TOP_CC, RIGHT_L_CC, TOP_CC, TOP_CC]
numbers[6] = [LEFT_BAR_CC, EMPTY_CC, LEFT_L_CC, RIGHT_L_CC, TOP_CC, TOP_CC]
numbers[7] = [TOP_CC, RIGHT_L_CC, EMPTY_CC, RIGHT_BAR_CC, EMPTY_CC, TOP_RIGHT_CC]
numbers[8] = [LEFT_L_CC, RIGHT_L_CC, LEFT_L_CC, RIGHT_L_CC, TOP_CC, TOP_CC]
numbers[9] = [LEFT_L_CC, RIGHT_L_CC, TOP_CC, RIGHT_L_CC, EMPTY_CC, TOP_RIGHT_CC]
numbers[10] = [EMPTY_CC, EMPTY_CC, EMPTY_CC, EMPTY_CC, EMPTY_CC, EMPTY_CC]

class clock(threading.Thread):
    def __init__(self, lcd):
        threading.Thread.__init__(self, daemon=True)
         #init lcd and turn off backlight
        self.__lcd = lcd
        self.__jbvlock = threading.Lock()
        self.__running = False
        self.__newday = True
    
    def run(self):
        self.__load_cc()
        self.__jbvlock.acquire()
        self.__running = True
        self.__refresh_day()
        while self.__running:
            self.__refresh_time(4)
            self.__jbvlock.release()
            time.sleep(0.1)
        self.__lcd.lcd_clear()

    def stop(self):
        with self.__jbvlock:
            self.__running = False


    def __refresh_time(self,position=0):
        now = datetime.now()
        if now.hour == 0 and now.minute == 0 and self.__newday:
            self.__refresh_day()
            self.__newday = False

        if now.hour == 0 and now.minute == 1 and not self.__newday:
            self.__newday = True
        
        if now.hour > 9:
            self.__write_num(now.hour // 10, 0 + position)
        else:
            self.__write_num(10,0 + position)
        self.__write_num(now.hour % 10, 3 + position)
        self.__write_dot(5 + position)
        self.__write_num(now.minute // 10, 6 + position)
        self.__write_num(now.minute % 10, 9 + position)


    def __refresh_day(self):
        self.__lcd.lcd_display_string(datetime.now().strftime('%A %B %d %Y'), 1, 0)

    def __write_num(self,number,position):
        for i,cc in enumerate(numbers[number]):
            self.__lcd.lcd_write_custom_char(cc,(i+4) // 2, (i % 2) + position)

    def __write_dot(self,position):
        self.__lcd.lcd_write_custom_char(DOT_CC, 2, position)
        self.__lcd.lcd_write_custom_char(DOT_CC, 3, position)

    def __load_cc(self):
        #load custom characters
        self.__lcd.lcd_load_custom_chars(customCC)



    
import I2C_LCD_driver
import time

TOP_RIGHT_CC = 0
TOP_CC = 1
LEFT_BAR_CC = 2
RIGHT_BAR_CC = 3
RIGHT_L_CC = 4
LEFT_L_CC = 5
EMPTY_CC = 128

numbers = [EMPTY_CC, EMPTY_CC, EMPTY_CC, EMPTY_CC, EMPTY_CC, EMPTY_CC] * 10
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

class clock:
    def __init__(self):
         #init lcd and turn off backlight
        self.__lcd = I2C_LCD_driver.lcd()
        self.__lcd.backlight(0)

        #load custom characters
        customCC = [      

            #Top right 0 
            [ 0b00111,
	        0b00111,
	        0b00111,
	        0b00000,
	        0b00000,
	        0b00000,
	        0b00000,
	        0b00000],

            #Top 1
            [ 0b11111,
	        0b11111,
	        0b11111,
	        0b00000,
	        0b00000,
	        0b00000,
	        0b00000,
	        0b00000],

            #Left bar 2
            [  0b11100,
            0b11100,
            0b11100,
            0b11100,
            0b11100,
            0b11100,
            0b11100,
            0b11100],

            #Right bar 3
            [  0b00111,
            0b00111,
            0b00111,
            0b00111,
            0b00111,
            0b00111,
            0b00111,
            0b00111],

            #Right L 4
            [  0b11111,
            0b11111,
            0b11111,
            0b00111,
            0b00111,
            0b00111,
            0b00111,
            0b00111],

            #Left L 5
            [  0b11111,
            0b11111,
            0b11111,
            0b11100,
            0b11100,
            0b11100,
            0b11100,
            0b11100],
              
        ]
        self.__lcd.lcd_load_custom_chars(customCC)
        self.__lcd.backlight(0)

    def write_num(self,number,position):
        for i,cc in enumerate(numbers[number]):
            self.__lcd.lcd_write_custom_char(cc,(i+4) // 2, (i % 2) + position)




    
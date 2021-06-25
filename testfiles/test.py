import I2C_LCD_driver
import time
import atexit

HOLD_TIME = 1
CLEAR_TIME = 0.1

mylcd = I2C_LCD_driver.lcd()

def exit_handler():
    time.sleep(2)
    mylcd.lcd_clear()
    mylcd.backlight(0)

def changestr(old,new):
    if old == new:
        return old
    else:
        return " "


atexit.register(exit_handler)

mylcd.backlight(1)
numstr = "Number:"
numstr = numstr.rjust(17)
oldstr = ""
newstr = ""

customCC = [      

            #music note
            [ 0b00001,
	          0b00011,
	          0b00101,
	          0b01001,
	          0b01001,
	          0b01011,
	          0b11011,
	          0b11000],
        ]
mylcd.lcd_load_custom_chars(customCC)
mylcd.lcd_write(0x80 + 0x54)
mylcd.lcd_write_char(0)

while True:
    for i in range(256):
        oldstr = newstr
        newstr = numstr + str(i).rjust(3)
        mylcd.lcd_display_string(newstr,1)
        mylcd.lcd_write(0x80 + 0x54)
        mylcd.lcd_write_char(i)
        time.sleep(HOLD_TIME)
        mylcd.lcd_display_string(map(changestr,oldstr,newstr),1)
        time.sleep(CLEAR_TIME)




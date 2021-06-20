import I2C_LCD_driver
import time
import atexit

HOLD_TIME = 0.25
CLEAR_TIME = 0.1

mylcd = I2C_LCD_driver.lcd()

def exit_handler():
    time.sleep(2)
    mylcd.lcd_clear()
    mylcd.backlight(0)

atexit.Register(exit_handler)

mylcd.backlight(1)
numstr = "Number:"
numstr = numstr.rjust(17)
emptyln = " " * 20
while True
    for i in range(100):
        mylcd.lcd_display_string(numstr + str(i).rjust(3),1)
        time.sleep(HOLD_TIME)
        mylcd.lcd_display_string(numstr,1)
        time.sleep(CLEAR_TIME)




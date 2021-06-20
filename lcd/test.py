import I2C_LCD_driver
import time

mylcd = I2C_LCD_driver.lcd()

# keepgoing = True
# line = ""
# lines = {}
# while (keepgoing):
#     line = input("Enter Line Number: ")
#     if line == 0:
#         keepgoing = False
#     else:
#         lines[line] = input("Enter Text For Line " + str(line) + ":")

# keepgoing = (len(lines) != 0)
# str_pad = " " * 20
# for line in lines:
#     lines[line] = str_pad + lines[line]

# while keepgoing:
#     line = input("Enter Line Number: ")
#     for i in range (0)
#     for line in lines:
mylcd.backlight(1)
numstr = "Number:"
numstr = numstr.rjust(17)
emptyln = " " * 20
for i in range(100):
    mylcd.lcd_display_string(numstr + str(i).rjust(3),1)
    time.sleep(0.25)
    mylcd.lcd_display_string(numstr,1)
    time.sleep(0.05)

time.sleep(2)
mylcd.lcd_clear()
mylcd.backlight(0)


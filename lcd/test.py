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
       
str_pad = " " * 20
my_long_string = "Hi Mom!" * 10
while True:
    for i in range(0,len(my_long_string)):
        lcd_text = my_long_string[i:(i+20)]
        mylcd.lcd_display_string(lcd_text,1)
        time.sleep(0.4)
        mylcd.lcd_display_string(str_pad,1)


mylcd.lcd_clear()
mylcd.lcd_display_string("Goodbye!!!",2,6)
time.sleep(2)
mylcd.lcd_clear()


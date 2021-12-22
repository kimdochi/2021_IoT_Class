from lcd import drivers
import time

display = drivers.Lcd()

try:
    print("Writing to Display")
    display.lcd_display_string("Hello, World!!", 1)
    while True:
        # Write line of text to first line of display
        display.lcd_display_string("** WELCOME **", 2)
        time.sleep(2)
        display.lcd_display_string("   WELCOME   ", 2)
        time.sleep(2)
        
finally:
    print('cleaning up')
    display.lcd_clear()
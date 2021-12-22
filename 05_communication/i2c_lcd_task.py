from lcd import drivers
import datetime
import Adafruit_DHT

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
DHT_PIN = 4

try:
    print("Writing to Display")
    while True:
        now = datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x%X"), 1)
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        display.lcd_display_string('%.1f*C, %.1f%%' % (t,h), 2)
        
finally:
    print('cleaning up')
    display.lcd_clear()
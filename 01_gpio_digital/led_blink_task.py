import RPi.GPIO as GPIO
import time

LED_RED = 17
LED_YELLOW = 27
LED_GREEN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)

GPIO.output(LED_RED, GPIO.HIGH)
print("red led on")
time.sleep(2)
GPIO.output(LED_RED, GPIO.LOW)
print("red led off")
time.sleep(2)
GPIO.output(LED_YELLOW, GPIO.HIGH)
print("yellow led on")
time.sleep(2)
GPIO.output(LED_YELLOW, GPIO.LOW)
print("yellow led off")
time.sleep(2)
GPIO.output(LED_GREEN, GPIO.HIGH)
print("green led on")
time.sleep(2)
GPIO.output(LED_GREEN, GPIO.LOW)
print("green led off")
time.sleep(2)

GPIO.cleanup()
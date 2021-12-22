#스위치로 LED 제어하기
import RPi.GPIO as GPIO

RED_LED = 12
RED_SWITCH = 4
YELLOW_LED = 16
YELLOW_SWITCH = 17
GREEN_LED = 20
GREEN_SWITCH = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부 풀다운저항(안 눌렀을 때 : 0, 눌렀을 때 : 1)
GPIO.setup(YELLOW_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GREEN_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val = GPIO.input(RED_SWITCH)
        print(val)
        GPIO.output(RED_LED, val) #GPIO.HIGH(1), GPIO.LOW(0)

        val1 = GPIO.input(YELLOW_SWITCH)
        print(val1)
        GPIO.output(YELLOW_LED, val1) #GPIO.HIGH(1), GPIO.LOW(0)

        val2 = GPIO.input(GREEN_SWITCH)
        print(val2)
        GPIO.output(GREEN_LED, val2) #GPIO.HIGH(1), GPIO.LOW(0)
finally:
    GPIO.cleanup()
    print('cleanup and exit')

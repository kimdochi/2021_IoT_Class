# 학교종 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

#주파수 설정(262Hz = 도)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) # duty cycle(0~100)

# 도레미파솔라시도
melody = [392, 392, 440, 440, 392, 392, 330, 392, 392, 330, 330, 294, 392, 392, 440, 440, 392, 392, 330, 392, 330, 294, 330, 262]
try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)


finally:
    pwm.stop()
    GPIO.cleanup()
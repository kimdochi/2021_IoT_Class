#컵라면을 향한 여정

# 불러오기
import RPi.GPIO as GPIO 
import time
import threading

# 핀 설정
LED_RED = 17
LED_YELLOW = 27
LED_GREEN = 22
SWITCH_PIN = 4
BUZZER_PIN = 23
            #  A, B,  C,  D,  E,  F,  G
SEGMENT_PINS = [5, 6, 13, 19, 26, 21, 20]
DIGIT_PINS = [16, 12, 25, 24]

# input, output 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)

# LED가 다 꺼지게 설정
GPIO.output(LED_RED, GPIO.LOW)
GPIO.output(LED_YELLOW, GPIO.LOW)
GPIO.output(LED_GREEN, GPIO.LOW)

# Segment핀은 HIGH->ON, LOW->OFF
# 세그먼트 핀 모두 꺼지게 설정
for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

# Digit핀은 HIGH->OFF, LOW->ON
# 모두 꺼지게 설정
for digit in DIGIT_PINS:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)


# 시간 3분으로 설정
t=180

# 숫자 설정
data = [[1, 1, 1, 0, 0, 1, 1],  # 9를 나타냄    # 0번째
        [1, 1, 1, 1, 1, 1, 1],  # 8을 나타냄    # 1번째
        [1, 1, 1, 0, 0, 0, 0],  # 7을 나타냄    # 2번째
        [1, 0, 1, 1, 1, 1, 1],  # 6을 나타냄    # 3번째
        [1, 0, 1, 1, 0, 1, 1],  # 5를 나타냄    # 4번째
        [0, 1, 1, 0, 0, 1, 1],  # 4를 나타냄    # 5번째
        [1, 1, 1, 1, 0, 0, 1],  # 3을 나타냄    # 6번째
        [1, 1, 0, 1, 1, 0, 1],  # 2를 나타냄    # 7번째
        [0, 1, 1, 0, 0, 0, 0],  # 1을 나타냄    # 8번째
        [1, 1, 1, 1, 1, 1, 0]]  # 0을 나타냄    # 9번째


def display(digit, number): # 자릿수, 숫자
    # 해당하는 자릿수의 핀만 LOW로 설정, 나머지는 HIGH
    for i in range(4):
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i], GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)

    # 숫자 출력
    for i in range(7):  # 0~6
        GPIO.output(SEGMENT_PINS[i], data[number][i])
    time.sleep(0.006) # 0.006초간 쉼

def second():
    while True:
        d2 = 9 - int((t/100)%10)    #d2 = 백의 자리
        d3 = 9 - int((t/10)%10)     #d3 = 십의 자리
        d4 = 9 - (t%10)             #d4 = 일의 자리
        display(2, d2)  # 두번째 자릿수에 d2 출력
        display(3, d3)  # 세번째 자릿수에 d3 출력
        display(4, d4)  # 네번째 자릿수에 d4 출력

try:
    while True:
        display(1, 9)   # 첫번째 자릿수에 0을 출력
        display(2, 8)   # 두번째 자릿수에 1을 출력
        display(3, 1)   # 세번째 자릿수에 8을 출력
        display(4, 9)   # 네번째 자릿수에 0을 출력

        # 스위치를 누르면 실행
        val = GPIO.input(SWITCH_PIN)
        if val == 1:

            # 30만큼의 세기로 소리를 1초간 출력
            pwm = GPIO.PWM(BUZZER_PIN, 303) # 피에조 부저 아무소리로 설정
            pwm.start(30)   # duty cycle(0~100)
            time.sleep(1)   # 1초간 쉼
            pwm.ChangeDutyCycle(0)  # 부저음이 들리지 않음
            GPIO.output(LED_GREEN, GPIO.HIGH)   # 초록색 LED 키기

            # 남은 시간 나타내기
            while True:
                My_Thread = threading.Thread(target=second) # 남은 시간을 나타내기 위해서 스레드 설정
                My_Thread.start()   # 스레드 실행
                time.sleep(1)   # 1초 간격
                t = t-1 # 시간 설정

                # 남은 시간이 1분일 경우 30만큼의 세기로 소리를 1초간 출력
                if t == 60:
                    GPIO.output(LED_YELLOW, GPIO.HIGH)  # 노란색 LED 키기
                    GPIO.output(LED_GREEN, GPIO.LOW)    # 초록색 LED 끄기
                    pwm.start(30)   # duty cycle(0~100)
                    time.sleep(1) # 1초간 쉼
                    pwm.ChangeDutyCycle(0)  # 부저음이 들리지 않음
                    t = t-1 # 시간 설정

                # 남은 시간이 10초일 경우 40만큼의 세기로 소리를 1초간 출력
                if t == 10:
                    GPIO.output(LED_RED, GPIO.HIGH)     # 빨간색 LED 키기
                    GPIO.output(LED_YELLOW, GPIO.LOW)   # 노란색 LED 끄기
                    pwm.start(40)   # duty cycle(0~100)
                    time.sleep(1) # 1초간 쉼
                    pwm.ChangeDutyCycle(0)  # 부저음이 들리지 않음
                    t = t-1 # 시간 설정

                # 시간이 끝났을 경우 50만큼의 세기로 소리를 1초간 출력 후 정지
                if t == 0:
                    pwm.start(50)   # duty cycle(0~100)
                    time.sleep(1) # 1초간 쉼
                    pwm.ChangeDutyCycle(0)  # 부저음이 들리지 않음
                    break 
            break
                
finally:
    GPIO.cleanup()
    pwm.stop()
    print('bye')
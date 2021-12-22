from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)
RED_LED = 27
BLUE_LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)

@app.route("/")
def hello():
    return '''
    <p>Hello, Flask!!</p>
    <a href="/led/red/on">RED LED ON</a>
    <a href="/led/red/off">RED LED OFF</a>
    <a href="/led/blue/on">BLUE LED ON</a>
    <a href="/led/blue/off">BLUE LED OFF</a>
    '''

@app.route("/led/<color>/<op>")
def led_op(color, op):
    if color == "red":
        if op == "on":
            GPIO.output(RED_LED, GPIO.HIGH)
            print("RED LED ON")
            return '''
            <p>RED LED ON</p>
            <a href="/">Go Home</a>
            '''
        elif op == "off":
            GPIO.output(RED_LED, GPIO.LOW)
            print("RED LED OFF")
            return '''
            <p>RED LED OFF</p>
            <a href="/">Go Home</a>
            '''
    elif color == "blue":
        if op == "on":
            GPIO.output(BLUE_LED, GPIO.HIGH)
            print("BLUE LED ON")
            return '''
            <p>BLUE LED ON</p>
            <a href="/">Go Home</a>
            '''
        elif op == "off":
            GPIO.output(BLUE_LED, GPIO.LOW)
            print("BLUE LED OFF")
            return '''
            <p>BLUE LED OFF</p>
            <a href="/">Go Home</a>
            '''
    else:
        return "URL Erorr"

# 터미널에서 직접 실행한 경우
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        print("clean up")
        GPIO.cleanup()

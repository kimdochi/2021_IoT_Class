from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
RED_LED = 4
BLUE_LED = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)

@app.route("/")
def hello():
    return render_template("led2.html")

@app.route("/led/<color>/<op>")
def led_op(color, op):
    if color == "red":
        if op == "on":
            GPIO.output(RED_LED, GPIO.HIGH)
            print("RED LED ON")
            return "RED LED ON"
        elif op == "off":
            GPIO.output(RED_LED, GPIO.LOW)
            print("RED LED OFF")
            return"RED LED OFF"
    elif color == "blue":
        if op == "on":
            GPIO.output(BLUE_LED, GPIO.HIGH)
            print("BLUE LED ON")
            return "BLUE LED ON"
        elif op == "off":
            GPIO.output(BLUE_LED, GPIO.LOW)
            print("BLUE LED OFF")
            return "BLUE LED OFF"
    else:
        return "URL Erorr"

# 터미널에서 직접 실행한 경우
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        print("clean up")
        GPIO.cleanup()

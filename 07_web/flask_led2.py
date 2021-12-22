from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
LED = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

@app.route("/")
def home():
    return render_template("led.html")

@app.route("/led/<op>")
def led_op(op):
    print(op)
    if op == "on":
        GPIO.output(LED, GPIO.HIGH)
        return "LED ON"
    elif op == "off":
        GPIO.output(LED, GPIO.LOW)
        return "LED OFF"
    else:
        return "URL Erorr"

# 터미널에서 직접 실행한 경우
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        print("clean up")
        GPIO.cleanup()
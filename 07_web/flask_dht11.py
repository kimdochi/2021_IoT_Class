from flask import Flask, render_template
import Adafruit_DHT
import json

senser = Adafruit_DHT.DHT11
DHT_PIN = 4

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dht11.html")

@app.route("/monitor")
def monitoring():
    h, t = Adafruit_DHT.read_retry(senser, DHT_PIN)
    if h is not None and t is not None:
        obj = {'humidity': h, 'temperature': t}
        return json.dumps(obj) # 객체를 문자열로 변환
    else:
        return 'Read error'

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        print('clean up')
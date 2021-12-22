from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("hello.html", title="Hello")

@app.route("/first")
def first():
    return render_template("first.html", title="First Page")

@app.route("/second")
def second():
    return render_template("second.html", title="Second Page")

# 터미널에서 직접 실행한 경우
if __name__ == "__main__":
    app.run(host="0.0.0.0")
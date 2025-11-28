from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

count = 0

@app.route("/")
def index():
    return render_template("index.html", count=count)

@app.route("/increment")
def increment():
    global count
    count += 1
    return redirect(url_for("index"))

@app.route("/decrement")
def decrement():
    global count
    count -= 1
    return redirect(url_for("index"))

@app.route("/reset")
def reset():
    global count
    count = 0
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


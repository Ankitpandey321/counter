from flask import Flask, render_template, redirect, url_for
import mysql.connector
import time

app = Flask(__name__)

# Retry MySQL connection
def get_connection():
    retries = 10
    delay = 5  # seconds

    for attempt in range(1, retries + 1):
        try:
            conn = mysql.connector.connect(
                host="mysql",
                user="root",
                password="password",
                database="counterdb"
            )
            return conn

        except mysql.connector.Error as err:
            print(f"MySQL connection failed (Attempt {attempt}/{retries}): {err}")

            if attempt == retries:
                raise  # final failure

            time.sleep(delay)

# Fetch current count
def get_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM counter WHERE id = 1")
    value = cursor.fetchone()[0]
    conn.close()
    return value

# Update count
def set_count(new_value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE counter SET value = %s WHERE id = 1", (new_value,))
    conn.commit()
    conn.close()

@app.route("/")
def index():
    count = get_count()
    return render_template("index.html", count=count)

@app.route("/increment")
def increment():
    current = get_count()
    set_count(current + 1)
    return redirect(url_for("index"))

@app.route("/decrement")
def decrement():
    current = get_count()
    set_count(current - 1)
    return redirect(url_for("index"))

@app.route("/reset")
def reset():
    set_count(0)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

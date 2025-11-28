from flask import Flask, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Function to connect to MySQL
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="counterdb"
    )

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

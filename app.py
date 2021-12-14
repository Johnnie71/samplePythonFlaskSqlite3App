from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def db_connection(): ## creating the connection to the sql database
    connection = None
    try:
        connection = sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return connection


@app.route('/')
def index():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
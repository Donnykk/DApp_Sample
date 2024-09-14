from flask import Flask, render_template, request
import sqlite3
import datetime

app = Flask(__name__)


@app.route('/', methods=["get", "post"])
def index():
    return render_template('index.html')


@app.route('/main', methods=["get", "post"])
def main():
    user_input = request.form.get("q")
    timestamp = datetime.datetime.now()

    with sqlite3.connect('dapp.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user VALUES (?, ?)", (user_input, timestamp))
        conn.commit()

    return render_template('main.html', user_input=user_input)


@app.route('/store_money', methods=["get", "post"])
def store_money():
    return render_template('store_money.html')


@app.route('/transfer_money', methods=["get", "post"])
def transfer_money():
    return render_template('transfer_money.html')


@app.route('/admin', methods=["get", "post"])
def admin():
    return render_template('admin.html')


@app.route('/viewDB', methods=["GET", "POST"])
def view_database():
    with sqlite3.connect('dapp.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        db_records = cursor.fetchall()
    return render_template('viewDB.html', db_records=db_records)


@app.route('/deleteDB', methods=["GET", "POST"])
def delete_database_entries():
    with sqlite3.connect('dapp.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user")
        conn.commit()
    return render_template('deleteDB.html')


if __name__ == '__main__':
    app.run()

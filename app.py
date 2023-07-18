from flask import Flask, render_template, request
from flask import redirect, url_for, abort, g
import sqlite3
import numpy as np

app = Flask(__name__)

def get_message_db():
    try:
        return g.message_db
    except:
        g.message_db = sqlite3.connect("messages_db.sqlite")
        cmd = 'CREATE TABLE IF NOT EXISTS messages(id INT, handle TEXT, message TEXT)'
        cursor = g.message_db.cursor()
        cursor.execute(cmd)
        return g.message_db

def insert_messages(request):
    db = get_message_db()
    cursor = db.cursor()
    cmd = 'SELECT COUNT(*) FROM messages'
    new_id = cursor.execute(cmd).fetchone()[0] + 1
    
    cmd = f"INSERT INTO messages VALUES ({new_id}, '{request.form['handle']}', '{request.form['message']}')"
    cursor.execute(cmd)
    db.commit()
    db.close()
    
@app.route("/", methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        insert_message(request.form)
        return render_template('submit.html', message=message, handle=handle)

def random_messages(n):
    db = get_message_db()
    cursor = db.cursor()
    cmd = f"SELECT * FROM messages ORDER BY RANDOM() LIMIT {n}"
    messages = cursor.execute(cmd).fetchall()
    db.close()

    return messages

@app.route('/view/', methods=['POST', 'GET'])
def view():
    messages = random_submissions(np.random.randint(1,6))
    return render_template('view.html', messages=messages)



from flask import Flask, render_template, request
from flask import redirect, url_for, abort
import sqlite3

app = Flask(__name__)

def get_message_db():
  # write some helpful comments here
    try:
        return g.message_db
    except:
        g.message_db = sqlite3.connect("messages_db.sqlite")
        cmd = 'CREATE TABLE IF NOT EXISTS messages(id INT, handle TEXT, message TEXT)'
        cursor = g.message_db.cursor()
        cursor.execute(cmd)
        return g.message_db

def insert_messages(request):
    
    



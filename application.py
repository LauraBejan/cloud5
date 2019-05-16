from dbconn import *
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    message_to_display = ""
    row = customQuery("SELECT * FROM PLAYLISTS")
    for word in row:
        message_to_display += str(word)
    return message_to_display

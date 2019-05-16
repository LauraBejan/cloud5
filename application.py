from dbconn import *
from yt_api import *
from flask import Flask,render_template, flash, request
from sendMail import sendMail
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import json
from sendMail import sendMail

from flask import Flask
app = Flask(__name__)
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
@app.route("/")
def hello():
    
    # message_to_display = ""
    # row = customQuery("SELECT * FROM PLAYLISTS")
    # for word in row:
    #     message_to_display += str(word)
    # return message_to_display
    # return("gets here?")
    receiver="lepowobo@directmail.top"
    sendMail(receiver)
    return render_template("hello.html")
    # return str(getRandomAnswer('kim kardashian'))

@app.route("/result",methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form["Question"]
        if len(result) < 3:
            return str(getRandomAnswer(result))
        else:
            search = " ".join(result.split(" ")[-2:])
            return str(getRandomAnswer(search))
    #   return str(result)
    #   return render_template("result.html",result = result)
    return str(getRandomAnswer('kim kardashian'))

from dbconn import *
from yt_api import *
from flask import Flask,render_template, flash, request
from sendMail import sendMail
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import json
from sendMail import sendMail
from yt import *

from flask import Flask

global answer
def setAnswer(this):
    global answer
    answer = this

app = Flask(__name__)
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
@app.route("/")
def hello():
    # return "hello"
    # result,comm,answer = getTitles("kim")
    # out = ""
    # for title in result:
    #     out += title
    # out += "<br>"
    # out += comm + "<br>" + str(answer)
    # return out
    # # return render_template("hello.html")
    # # return str(getRandomAnswer('kim kardashian'))
    # return "hello"
    return getRandKey()

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


@app.route("/mail")
def mail():
    return render_template("mail.html")

@app.route("/options")
def displayOptions():
    result, comm, answer = getTitles("kim")
    setAnswer("opt" + str(answer))
    return render_template("options.html",comm=comm,opt1=result[0],opt2=result[1],opt3=result[2])


@app.route("/process+result", methods=['POST'])
def processResult():
    if request.method == 'POST':
            option = request.form["option"]
            global answer
            if option == answer:
                return "Nice, option {} was correct".format(option[-1])
            return "Wrong, option {} was incorrect".format(option[-1])


@app.route("/preview",methods=['POST','GET'])
def preview():
    if request.method == 'POST':
            receiver = request.form["receiver"]
            title = request.form["title"]
            message = request.form["message"]
            sendMail(receiver,title,message)
    return "Mail sent"

@app.route("/suggestion")
def suggestKeyWords():
    return render_template("suggestion.html")

@app.route("/ThankYou",methods=['POST'])
def processSuggestion():
    if request.method == 'POST':
            suggestion = request.form["suggestion"]
            return suggestion

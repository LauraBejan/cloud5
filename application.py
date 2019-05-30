from dbconn import *
from yt_api import *
from flask import Flask,render_template, flash, request
from sendMail import sendMail
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import json
from sendMail import sendMail
from yt import *
from thumbnail import *
from flask import Flask
#from azure import *
#from azure.cognitiveservices.vision.computervision import ComputerVisionClient
#from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
#from msrest.authentication import CognitiveServicesCredentials

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

@app.route("/down")
def down():
    return render_template("down.html")
    
@app.route("/mail")
def mail():
    return render_template("mail.html")
    

@app.route("/preview",methods=['POST','GET'])
def preview():
    if request.method == 'POST':
            receiver = request.form["receiver"]
            title = request.form["title"]
            message = request.form["message"] + "\n \n You should also try this game \n http://ccproiect2.azurewebsites.net/options"
            sendMail(receiver,title,message)
    return "Mail sent"




import random
@app.route("/options")
def displayOptions():
    rand_seed = random.randint(1,1000) / 1000
    if rand_seed > 0.3:
        key = getRandKey()
        # result, comm, answer = getTitles(key)
        result, comm, answer = ["Kanye west", "Prank video", "Why Im quitting youtube"], "Very nice", 1
        hint = getThumbnail(result[answer])
        setAnswer("opt" + str(answer))
        return render_template("options.html",comm=comm,opt1=result[0],opt2=result[1],opt3=result[2],hint=hint)
    else:
        return render_template("suggestion.html")


@app.route("/process+result", methods=['POST'])
def processResult():
    if request.method == 'POST':
            option = request.form["option"]
            global answer
            if option == answer:
                return render_template("correct.html",opt=option[-1])
               # return "Nice, option {} was correct".format(option[-1])
            return render_template("fail.html",opt=option[-1])


@app.route("/img", methods=['POST'])
def analyzeImg():
    ACCOUNT_ENDPOINT='https://westus.api.cognitive.microsoft.com/'
    ACCOUNT_KEY='48fdf3934f4648779d8fca132cb7c21e'
    endpoint = 'https://westus.api.cognitive.microsoft.com/'
    key = '48fdf3934f4648779d8fca132cb7c21e'

    # Set credentials
    credentials = CognitiveServicesCredentials(key)

    # Create client
    client = ComputerVisionClient(endpoint, credentials)

    domain = "landmarks"
    # https://westus.api.cognitive.microsoft.com/
    url = "http://www.public-domain-photos.com/free-stock-photos-4/travel/san-francisco/golden-gate-bridge-in-san-francisco.jpg"
    language = "en"
    max_descriptions = 3

    analysis = client.describe_image(url, max_descriptions, language)

    for caption in analysis.captions:
        return str(caption.text)

    


@app.route("/suggestion")
def suggestKeyWords():
    return render_template("suggestion.html")

import requests
@app.route("/ThankYou",methods=['POST'])
def processSuggestion():
    if request.method == 'POST':
            suggestion = request.form["suggestion"]
            checkProfanity = requests.get("https://www.purgomalum.com/service/json?text={}".format(suggestion))
            response = checkProfanity.json()["result"]
            if "*" not in response:
                insertKey(response)
                return "Thank you for your suggestion!"
            else:
                return "Hey, that's not very nice!" 

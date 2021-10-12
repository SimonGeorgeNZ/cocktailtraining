import os
import random
from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from class_ import *

app = Flask(__name__)

class MongoInfo():

    app.config["MONGO_DBNAME"] = 'CocktailTraining'
    app.config["MONGO_URI"] = 'mongodb+srv://root:Dunedin100@myfirstcluster.jekwe.mongodb.net/CocktailTraining?retryWrites=true&w=majority'


mongo = PyMongo(app) 


@app.route('/')
def home():

    pickSB = initialInfo().pickSub
    fullCT = Question.FullCT
    ansName = Question.AnsName
    choices = Question.choices

    return render_template('index.html', 
                            ps=pickSB, full=fullCT, name=ansName, choices=choices)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

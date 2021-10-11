import os
import random
from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'CocktailTraining'
app.config["MONGO_URI"] = 'mongodb+srv://root:Dunedin100@myfirstcluster.jekwe.mongodb.net/CocktailTraining?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def home():
    class Question():

        sub = ['garnish', 'glass']  #List of entry for question
        pickSub = random.choice(sub)  # Finds random question
        cocktailsAll = mongo.db.cocktail.find()
        CTnames = cocktailsAll.distinct("name")
        NameList = [CTnames]
        for names in NameList:
            choices = random.sample(names, 4)
        correct = random.choice(choices)
        FullCT = mongo.db.cocktail.find_one({"name":correct})
        AnsName = correct
        choices = choices
        

    pickSB = Question.pickSub
    fullCT = Question.FullCT
    ansName = Question.AnsName
    choices = Question.choices

    return render_template('index.html', 
                            ps=pickSB, full=fullCT, name=ansName, choices=choices)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

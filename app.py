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
    allCock = list(mongo.db.cocktail.find().sort("_id"))

    class InitialInfo:
        YN = ['strained', 'double strained']
        multi = ['garnish', 'glass', 'base spirit',
                'ingredients', 'steps']  # List of entry for question
        sub = ['YN', 'multi']
        SubChoice = random.choice(sub)  # Finds random question
        if SubChoice == 'multi':
            pickSub = random.choice(multi)
        else:
            pickSub = random.choice(YN)
        cocktailsAll = mongo.db.cocktail.find()
        allNames = cocktailsAll.distinct("name")

    pickSB = InitialInfo.pickSub

    class Question:
        CTnames = InitialInfo.allNames
        NameList = [CTnames]
        for names in NameList:
            choices = random.sample(names, 4)
            correct = random.choice(choices)
            FullCT = mongo.db.cocktail.find_one({"name": correct})

    choices = Question.choices
    sc = InitialInfo.SubChoice
    fullCT = Question.FullCT
    A_Sub = fullCT[pickSB]
    ansName = Question.correct

    for each in allCock:
        for x in choices:
            if each['name'] == x:
                if each[pickSB] == A_Sub:
                    print('yes')
    
    return render_template('index.html',
                           ps=pickSB, full=fullCT, theName=ansName, choices=choices, x=sc, allCock=allCock, As=A_Sub)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

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
        list = ['multi', 'single']  #List of collection
        cat = random.choice(list)  # Finds random collection
        cocktail = ['Mojito', 'Pina Colada', 'Pink Gin Fizz', 'Margarita Classic', 'Backwards Negroni', 'Sugar Mama', 'The girl next door']
        pickCock = random.choice(cocktail)

        def __str__(self):
            return self.name

    ps = Question.pickSub
    cate = Question.cat
    all = mongo.db[ps].find_one()  #Find subject
    pc = Question.pickCock  #Generate cocktail name
    getCT = mongo.db.cocktail.find_one({"name": pc })  #Find cocktail
    sm = all[cate]  #Get single or multi
    quest = getCT[ps]
    return render_template('index.html', sm=sm, CT=getCT, pc=pc, ps=ps, q=quest, cate=cate)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

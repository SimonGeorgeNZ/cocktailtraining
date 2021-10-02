import os
from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

import class_

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'CocktailTraining'
app.config["MONGO_URI"] = 'mongodb+srv://root:Dunedin100@myfirstcluster.jekwe.mongodb.net/CocktailTraining?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def home():
    list = ['multi', 'single'] #List of collection
    q_list = ['garnish', 'glass'] #List of category for question
    cat = random.choice(list) # Finds random collection
    MDB_cat = mongo.db[cat].find_one() #Finds collection in MDB
    quest = random.choice(q_list) # Finds random question
    question = getattr(MDB_cat, 'quest')
    MDB_quest = mongo.db[MDB_cat][quest].find_one() # Adds all info together
    return render_template('index.html', x=MDB_quest)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

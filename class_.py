from app import MongoInfo, mongo
import random


class initialInfo():
    sub = ['garnish', 'glass', 'base spirit', 'ingredients', 'strained', 'double strained', 'steps']  #List of entry for question
    pickSub = random.choice(sub)  # Finds random question
    cocktailsAll = mongo.db.cocktail.find()
    allNames = cocktailsAll.distinct("name")

class Question():

    CTnames = initialInfo.allNames
    NameList = [CTnames]
    for names in NameList:
        choices = random.sample(names, 4)
    correct = random.choice(choices)
    FullCT = mongo.db.cocktail.find_one({"name":correct})
    AnsName = correct
    choices = choices

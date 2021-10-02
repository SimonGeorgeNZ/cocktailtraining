from app import mongo
import random


class Question:

    list = ['multi', 'single'] #List of collection
    q_list = ['garnish', 'glass'] #List of category for question
    cat = random.choice(list) # Finds random collection
    quest = random.choice(q_list) # Finds random question
    MDB_cat = mongo.db[cat].find_one() #Finds collection in MDB

    question = Question()

    quest = getattr(question, MDB_cat, 'quest' )


    cat = mongo.db.cocktail.find()



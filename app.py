
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! This is my main page <h1>HELLO</h1>"

if __name__ == "__main__":
    app.run()
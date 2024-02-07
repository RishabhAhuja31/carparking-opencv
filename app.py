from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/")
def welcome():
    return "Hello World"

@app.route("/home")
def home():
    return "This is homepage"

from controller import *
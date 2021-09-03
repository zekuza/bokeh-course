# imports
from flask import Flask, render_template

# instantiate the flask app

app = Flask(__name__)

# create index page function

@app.route("/")
def index():
    return render_template("index.html")

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello There!</h1>"

app.run(host=os.getenv('0.0.0.0'), port=os.getenv('8000'), debug=True)
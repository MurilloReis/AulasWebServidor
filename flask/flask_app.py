from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ' <h1>Hello from Flask!</h1> <br> <p> <strong> Hi, bro! </strong> </p>'

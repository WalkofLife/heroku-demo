from flask import Flask, request

app = Flask(__name__)

@app.route('/')

def home():
    return "Learning Heroku "

@app.route('/someendpoints')
def firendpoint():
    return "This is my first path on heroku"

if __name__ == '__main__':
    app.run()
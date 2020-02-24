from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World 001!"

@application.route("/color")
def hello():
    return "The color is: XXX"

if __name__ == "__main__":
    application.run()

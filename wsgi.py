from flask import Flask
application = Flask(__name__)

import uuid

@application.route("/")
def hello():
    return "Hello World 001!"

@application.route("/color")
def color():
    myuuid = uuid.uuid4().hex
    return "The color is: {}".format(myuuid)

if __name__ == "__main__":
    application.run()

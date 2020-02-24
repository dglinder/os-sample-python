from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World 001!"

@application.route("/color")
def color():
    uuid = uuid.uuid4().hex
    return "The color is: {}".format(uuid)

if __name__ == "__main__":
    application.run()

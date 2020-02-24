from flask import Flask
application = Flask(__name__)

import random
import uuid

@application.route("/")
def hello():
    return "Hello World 001! <A href='/color'>Click here</A>"

@application.route("/color")
def color():
    myuuid = uuid.uuid4().hex
    random.seed(myuuid)
    red = random.randrange(0,255)
    green = random.randrange(0,255)
    blue = random.randrange(0,255)
    mycolor = ("#{}{}{}".format(hex(red).replace("0x",""),hex(green).replace("0x",""),hex(blue).replace("0x","")))
    return "The color is: {}".format(mycolor)

if __name__ == "__main__":
    application.run()

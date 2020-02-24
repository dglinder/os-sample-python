from flask import Flask
application = Flask(__name__)

import random
import uuid
import socket

@application.route("/")
def hello():
    return "Hello World 001! <A href='/color'>Click here</A>"

@application.route("/color")
def color():
    myname = socket.gethostname()
    random.seed(myname)
    red = hex(random.randrange(0,255)).replace("0x","")
    green = hex(random.randrange(0,255)).replace("0x","")
    blue = hex(random.randrange(0,255)).replace("0x","")
    mycolor = ("#{}{}{}".format(red,green,blue))
    return "The color for {} is: {}".format(myname,mycolor)

if __name__ == "__main__":
    application.run()

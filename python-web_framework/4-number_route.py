"""
A simple script that starts a flask web application
"""
# import needed modules
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """hello function:
        returns Hello HBNB!
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb function:
        returns HBNB
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def name(text):
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)

@app.route("/python", strict_slashes=False)
def default():
    return "Python is cool"

@app.route("/python/<text>", strict_slashes=False)
def magic(text):
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)

@app.route("/number/<n>", strict_slashes=False)
def num(n):
    if n.isdigit:
        return "{} is a number".format(n)
    else:
        return "404", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
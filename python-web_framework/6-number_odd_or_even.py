"""
A simple script that starts a flask web application
"""
# import needed modules
from flask import Flask, render_template

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

@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
     return render_template("5-number.html", name=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
     return render_template("6-number_odd_or_even.html", num=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
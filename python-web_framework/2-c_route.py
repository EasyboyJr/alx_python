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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
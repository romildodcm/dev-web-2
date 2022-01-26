from datetime import datetime
import imp
from flask import Flask, render_template
from utils import hello_world
# Controller

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    return render_template("index.html", now=now)

@app.route("/ifpr")
def ifpr():
    return "<h1>IFPR</h1>"

@app.route("/helloworld")
def helloworld():
    return hello_world()

@app.route("/hello/<name>")
def hello(name):
    return f"<h1>Hello {name}</h1>"


if __name__ == "__main__":
    app.run(port=8080, debug=True)
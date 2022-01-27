from datetime import datetime
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello/<name>")
def hello(name):
    today = datetime.now()
    data_local = today.strftime("%d/%m/%y - %H:%M:%S")
    return render_template("hello.html", name=name, today=data_local)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
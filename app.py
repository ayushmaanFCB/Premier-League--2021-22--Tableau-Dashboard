from flask import Flask, render_template, request, session, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/players")
def search():
    df = pd.read_excel("./static/data/dataset.xlsx")
    df = df.fillna(0)
    data = df.to_dict()
    return render_template("search.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
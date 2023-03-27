from flask import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/malls-and-shopping-centers")
def malls():
    return render_template("malls.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/blog/lifestyle")
def lifestyle():
    return render_template("lifestyle.html")

@app.route("/blog/fashion")
def fashion():
    return render_template("fashion.html")

@app.route("/blog/food-and-drink")
def foodanddrink():
    return render_template("food.html")
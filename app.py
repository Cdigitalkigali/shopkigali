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

@app.route("/malls-and-shopping-centers/names")
def names():
    return render_template("names.html")

@app.route("/malls-and-shopping-centers/stores")
def stores():
    return render_template("stores.html")

@app.route("/offers-and-promotions")
def offersandpromo():
    return render_template("offersandpromo.html")

@app.route("/offers-and-promotions/current-sales")
def currentsales():
    return render_template("currentsales.html")

@app.route("/offers-and-promotions/events")
def events():
    return render_template("events.html")

@app.route("/offers-and-promotions/gift-cards")
def giftcards():
    return render_template("giftcards.html")

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
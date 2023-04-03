from flask import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/malls-and-shopping-centers")
def malls_and_shopping_centers():
    return render_template("malls-and-shopping-centers.html")

@app.route("/hotels")
def hotels():
    return render_template("hotels.html")

@app.route("/restaurants")
def restaurants():
    return render_template("restaurants.html")





@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")
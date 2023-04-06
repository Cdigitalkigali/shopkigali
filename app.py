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

@app.route("/mall")
def mall():
    return render_template("mall.html")

@app.route("/hotels")
def hotels():
    return render_template("hotels.html")

@app.route("/restaurants")
def restaurants():
    return render_template("restaurants.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/admin")
def admin():
    return render_template("admin-login.html")




@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")
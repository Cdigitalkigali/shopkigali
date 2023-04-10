from flask import *
from cs50 import SQL
from auxiliary import dbinit
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import gettempdir

app = Flask(__name__)
db = SQL("sqlite:///database.db")
dbinit()

app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "789/456/127/894/561/278ssa94/5ds6a1s2"

Session(app)


## ---------------------------------------------------------- 
## Customer-interface of the site
## ----------------------------------------------------------

@app.route("/")
def index():
    session.clear()
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

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/blog/food")
def blog_food():
    return render_template("blog-food.html")

@app.route("/blog/lifestyle")
def blog_lifestyle():
    return render_template("blog-lifestyle.html")

@app.route("/blog/fashion")
def blog_fashion():
    return render_template("blog-fashion.html")



@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirmation = request.form.get("cpassword")

        if not email or not password or not password_confirmation:
            flash("please fill in all required fields")
            return redirect("/signup")
        else:
            check = db.execute("SELECT * FROM users WHERE email = :email", email=email)
            if len(check) != 0:
                flash("An account with that email already exists")
                return redirect("/signup")
            else:
                password_hash = generate_password_hash(password)
                db.execute("INSERT INTO users (email, password_hash) VALUES (:email, :password_hash)", email=email, password_hash=password_hash)
                session["user_id"] = db.execute("SELECT id FROM users WHERE email = :email", email=email)[0]
                session["role"] = "user"
                flash("Signed in successfully")
                return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email == request.form.get("email")
        password == request.form.get("password")
        rowsusers = db.execute("SELECT * FROM users WHERE email = :email", email = email)
        if len(rowsusers) == 1 and check_password_hash(rowsusers[0]["password_hash"], password):
            session["user_id"] = rowsusers[0]["id"]
            session["role"] = "user"
            return redirect("/")
        else:
            flash("username or password is incorrect")
            return redirect("/login")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out Successfully")
    return redirect("/")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        db.execute("INSERT INTO contacts (sender_name, sender_email, sender_message, message_read) VALUES (:name, :email, :message, :read)", name=name, email=email, message=message, read=1)
        flash("Message submitted successfully")
        return redirect("/")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

## ---------------------------------------------------------- 
## Administrator-interface of the site
## ----------------------------------------------------------

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        return render_template("admin-login.html")
    else:
        password = request.form.get("password")
        password_correct = "78945612"
        if password == password_correct:
            return redirect("/admin/contacts")
        else:
            flash("Username or password is incorrect")
            return redirect("/admin")

@app.route("/admin/contacts")
def admin_contacts():
    unread_contacts = db.execute("SELECT * FROM contacts WHERE message_read == 1")
    read_contacts = db.execute("SELECT * FROM contacts WHERE message_read == 0")
    return render_template("admin-contacts.html", unread=unread_contacts, read=read_contacts)

@app.route("/admin/listing-applications")
def admin_listing_applications():
    return render_template("admin-listing-applications.html")

@app.route("/admin/mall-listings")
def admin_malls():
    return render_template("admin-mall-listings.html")
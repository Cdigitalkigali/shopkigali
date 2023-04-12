from flask import *
from cs50 import SQL
from auxiliary import dbinit
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.utils import secure_filename
from tempfile import gettempdir
import os
import random

# Initialize App
app = Flask(__name__)
# Initialize Database
db = SQL("sqlite:///database.db")
dbinit()
# Define flask_session config
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "789/456/127/894/561/278ssa94/5ds6a1s2"
Session(app)
# File upload config
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(basedir, 'static/uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS


## ---------------------------------------------------------- 
## Customer-interface of the site
## ----------------------------------------------------------

@app.route("/")
def index():
    malls = db.execute("SELECT * FROM mall_listings")
    return render_template("index.html", malls=malls)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/malls-and-shopping-centers")
def malls_and_shopping_centers():
    malls = db.execute("SELECT * FROM mall_listings")
    return render_template("malls-and-shopping-centers.html", malls=malls)

@app.route("/malls-and-shopping-centers/<mall_id>")
def mall(mall_id):
    mall = db.execute("SELECT * FROM mall_listings WHERE id = :id", id=mall_id)
    return render_template("mall.html", mall=mall)

@app.route("/restaurants")
def restaurants():
    restaurants = db.execute("SELECT * FROM restaurant_listings")
    return render_template("restaurants.html", restaurants=restaurants)

@app.route("/restaurants/<restaurant_id>")
def restaurant(restaurant_id):
    restaurant = db.execute("SELECT * FROM restaurant_listings WHERE id = :id", id=restaurant_id)
    return render_template("restaurant.html", restaurant=restaurant)

@app.route("/hotels")
def hotels():
    return render_template("hotels.html")

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
        return render_template("/admin-login.html")
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

# Malls        ---------------------------------------------------------------------------------------
@app.route("/admin/mall-listings")
def admin_malls():
    malls = db.execute("SELECT * FROM mall_listings")
    return render_template("admin-mall-listings.html", malls=malls)

@app.route("/admin/mall-listings/<mall_id>")
def admin_mall_listing(mall_id):
    mall = db.execute("SELECT * FROM mall_listings WHERE id = :id", id=mall_id)
    return render_template("admin-mall.html", mall=mall)


@app.route("/admin/mall-listings/new", methods=["GET", "POST"])
def admin_malls_new():
    if request.method == "GET":
        return render_template("admin-mall-create.html")
    else:
        # Fetch mall details
        mall_name = request.form.get("mall_name")
        mall_address = request.form.get("mall_address")
        mall_phone = request.form.get("mall_phone")
        mall_website = request.form.get("mall_website")
        mall_opening = request.form.get("mall_opening")
        mall_closing = request.form.get("mall_closing")
        mall_description = request.form.get("mall_description")
        mall_photo = request.form.get("photo")

        # Generate Unique ID
        num = random.randrange(1, 10**7)
        new_id = '{:07}'.format(num)

        # Handle Uploaded Files
        # photo = request.files['photo']
        # photo.save(os.path.join(Config.UPLOAD_FOLDER, secure_filename(new_id + '_photo.jpg')))

        # Write data into database
        db.execute("INSERT INTO mall_listings (id, mall_name, mall_address, mall_phone, mall_website, mall_opening, mall_closing, mall_description, mall_photo_path, mall_popular) VALUES (:id, :name, :address, :phone, :website, :opening, :closing, :description, :photo, :mall_popular)",
        id = new_id,
        name = mall_name,
        address = mall_address,
        phone = mall_phone,
        website = mall_website,
        opening = mall_opening,
        closing = mall_closing,
        description = mall_description,
        photo = mall_photo,
        mall_popular = 0
        )

        # Finish
        flash("Successfully Listed Mall")
        return redirect("/admin/mall-listings")

# restaurants  ---------------------------------------------------------------------------------------
@app.route("/admin/restaurant-listings")
def admin_restaurants():
    restaurants = db.execute("SELECT * FROM restaurant_listings")
    return render_template("admin-restaurant-listings.html", restaurants=restaurants)

@app.route("/admin/restaurant-listings/<restaurant_id>")
def admin_restaurant_listing(restaurant_id):
    restaurant = db.execute("SELECT * FROM restaurant_listings WHERE id = :id", id=restaurant_id)
    return render_template("admin-restaurant.html", restaurant=restaurant)


@app.route("/admin/restaurant-listings/new", methods=["GET", "POST"])
def admin_restaurants_new():
    if request.method == "GET":
        return render_template("admin-restaurant-create.html")
    else:
        # Fetch restaurant details
        restaurant_name = request.form.get("restaurant_name")
        restaurant_address = request.form.get("restaurant_address")
        restaurant_phone = request.form.get("restaurant_phone")
        restaurant_website = request.form.get("restaurant_website")
        restaurant_opening = request.form.get("restaurant_opening")
        restaurant_closing = request.form.get("restaurant_closing")
        restaurant_description = request.form.get("restaurant_description")
        restaurant_photo = request.form.get("photo")

        # Generate Unique ID
        num = random.randrange(1, 10**7)
        new_id = '{:07}'.format(num)

        # Handle Uploaded Files
        # photo = request.files['photo']
        # photo.save(os.path.join(Config.UPLOAD_FOLDER, secure_filename(new_id + '_photo.jpg')))

        # Write data into database
        db.execute("INSERT INTO restaurant_listings (id, restaurant_name, restaurant_address, restaurant_phone, restaurant_website, restaurant_opening, restaurant_closing, restaurant_description, restaurant_photo_path, restaurant_popular) VALUES (:id, :name, :address, :phone, :website, :opening, :closing, :description, :photo, :restaurant_popular)",
        id = new_id,
        name = restaurant_name,
        address = restaurant_address,
        phone = restaurant_phone,
        website = restaurant_website,
        opening = restaurant_opening,
        closing = restaurant_closing,
        description = restaurant_description,
        photo = restaurant_photo,
        restaurant_popular = 0
        )

        # Finish
        flash("Successfully Listed restaurant")
        return redirect("/admin/restaurant-listings")
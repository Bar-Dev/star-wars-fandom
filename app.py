import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
# Home Page
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/")
# Test Page
@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/")
# Main Reviews page
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find().sort("film_order", 1))
    return render_template("reviews.html", reviews=reviews)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    # reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    regex_query = {'$regex': '.*{0}.*'.format(query), '$options': 'i'}
    reviews = list(mongo.db.reviews.find(
            {"$or": [
                {"review_name": regex_query},
                {"film_subtitle": regex_query},
                {"review_description": regex_query},
                {"reviewed_by": regex_query}
            ]}
        ))
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
# User registration
def register():
    if request.method == "POST":
        # Check for existing User in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "sides": request.form.get("sides"),
            "profile_image": request.form.get("profile_image")
        }
        mongo.db.users.insert_one(register)

        # Enter new seesion cookie for User
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    # If no User exists redirect to registration
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    sides = mongo.db.users.find_one(
                        {"username": session["user"]})["sides"]
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Get session users's username and info to populate profile page
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    sides = mongo.db.users.find_one(
        {"username": session["user"]})["sides"]
    profile_image = mongo.db.users.find_one(
        {"username": session["user"]})["profile_image"]
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        return render_template(
            "profile.html",
            username=username,
            sides=sides,
            user=user,
            profile_image=profile_image
        )

    return redirect(url_for("login"))


@app.route("/view_profiles/<username>", methods=["GET", "POST"])
def view_profiles(username):
    user = mongo.db.users.find_one(
        {"username": username})
    sides = user["sides"]
    profile_image = user["profile_image"]
    return render_template(
        "user_profile.html", username=username, sides=sides, user=user, profile_image=profile_image)



@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if request.method == "POST":
        # Check request is been triggered
        print("POST REQUEST")
        print(request.form)
        submit = {"$set": {
            "sides": request.form.get("sides"),
            "profile_image": request.form.get("profile_image")
        }}
        user = mongo.db.users.find_one(
            {"_id": ObjectId(user_id)})
        print(user)
        # Update User preferences to DB
        mongo.db.users.update_one(
            {"_id": ObjectId(user_id)}, submit)
        flash("Profile Successfully Updated")
        return redirect(url_for("profile", username=session["user"]))
    user = mongo.db.users.find_one(
            {"_id": ObjectId(user_id)})
    sides = mongo.db.users.find().sort("sides", 1)
    return render_template("edit_user.html", user=user, sides=sides)


@app.route("/logout")
def logout():
    # End User's session
    flash("You have been logged out, may the Force be with You!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        # Populate DB with Review information
        reviews = {
            "review_name": request.form.get("review_name"),
            "film_subtitle": request.form.get("film_subtitle"),
            "review_description": request.form.get("review_description"),
            "icon_name": request.form.get("icon_name"),
            "reviewed_by": session["user"],
            "film_order": request.form.get("film_order")
        }
        # Add Review to DB
        mongo.db.reviews.insert_one(reviews)
        flash("Review Successfully Added")
        return redirect(url_for("get_reviews"))

    icons = mongo.db.icons.find().sort("icon_name", 1)
    categories = mongo.db.categories.find().sort("category_name", 1)
    films = mongo.db.films.find().sort("film_name", 1)
    return render_template("add_review.html", icons=icons, films=films, categories=categories)


@app.route("/edit_review/<reviews_id>", methods=["GET", "POST"])
def edit_review(reviews_id):
    if request.method == "POST":
        # Allow session user to edit DB
        submit = {
            "review_name": request.form.get("review_name"),
            "film_subtitle": request.form.get("film_subtitle"),
            "review_description": request.form.get("review_description"),
            "icon_name": request.form.get("icon_name"),
            "reviewed_by": session["user"],
            "film_order": request.form.get("film_order")
        }
        # Send updated review info to DB
        mongo.db.reviews.update({"_id": ObjectId(reviews_id)}, submit)
        flash("Review Successfully Updated")

    reviews = mongo.db.reviews.find_one({"_id": ObjectId(reviews_id)})
    icons = mongo.db.icons.find().sort("icon_name", 1)
    films = mongo.db.films.find().sort("film_name", 1)
    return render_template("edit_review.html", reviews=reviews, icons=icons, films=films)


@app.route("/delete_review/<reviews_id>")
def delete_review(reviews_id):
    # Allow session user to delete review
    mongo.db.reviews.remove({"_id": ObjectId(reviews_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("get_reviews"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

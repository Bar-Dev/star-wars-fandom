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
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find().sort("review_name", 1))
    return render_template("reviews.html", reviews=reviews)


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "sides": request.form.get("sides")
        } 
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful") 
        return redirect(url_for("profile", username=session["user"]))  
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
    sides = mongo.db.users.find_one(
        {"username": session["user"]})["sides"]
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("profile.html", username=username, sides=sides)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out, may the Force be with You!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        reviews = {
            "review_name": request.form.get("review_name"),
            "film_name": request.form.get("film_name"),
            "film_subtitle": request.form.get("film_subtitle"),
            "review_era": request.form.get("review_era"),
            "review_description": request.form.get("review_description"),
            "icon_name": request.form.get("icon_name"),
            "reviewed_by": session["user"]
        }
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
        submit = {
            "review_name": request.form.get("review_name"),
            "film_name": request.form.get("film_name"),
            "review_subtitle": request.form.get("review_subtitle"),
            "review_era": request.form.get("review_era"),
            "review_description": request.form.get("review_description"),
            "icon_name": request.form.get("icon_name"),
            "reviewed_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(reviews_id)}, submit)
        flash("Review Successfully Updated")

    reviews = mongo.db.reviews.find_one({"_id": ObjectId(reviews_id)})
    icons = mongo.db.icons.find().sort("icon_name", 1)
    films = mongo.db.films.find().sort("film_name", 1)
    return render_template("edit_review.html", reviews=reviews, icons=icons, films=films)


@app.route("/delete_review/<reviews_id>")
def delete_review(reviews_id):
    mongo.db.reviews.remove({"_id": ObjectId(reviews_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("get_reviews"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

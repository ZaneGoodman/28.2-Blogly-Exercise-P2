"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///Blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True


from flask_debugtoolbar import DebugToolbarExtension

app.config["SECRET_KEY"] = "SECRET!"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def user_list():
    """List users"""
    users = User.query.all()
    return render_template("list.html", users=users)


@app.route("/", methods=["POST"])
def add_user():
    """Retrieve New user from form data & add to db"""
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"]

    new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect("/")


@app.route("/user-details/<int:user_id>")
def user_details(user_id):
    """shows user details"""
    user = User.query.get(user_id)
    return render_template("details.html", user=user)


@app.route("/user-details/<int:user_id>/edit")
def edit_user(user_id):
    """directed to user edit form"""
    user = User.query.get(user_id)

    return render_template("edit_user.html", user=user)


@app.route("/user-details/<int:user_id>/edit", methods=["POST"])
def apply_edits_to_user(user_id):
    """Apply changes to user details from edit user form"""
    user = User.query.get(user_id)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"]

    user.first_name = first_name
    user.last_name = last_name
    user.img_url = img_url

    db.session.add(user)
    db.session.commit()
    return redirect(f"/user-details/{user.id}")


@app.route("/user-details/<int:user_id>/delete")
def delete_user(user_id):
    """Delete user"""
    user = User.query.get(user_id)

    db.session.delete(user)
    db.session.commit()
    return redirect("/")

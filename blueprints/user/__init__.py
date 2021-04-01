from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from models import User
from database import db_session

user = Blueprint('user', __name__,template_folder='templates')


@user.route('sign_in/')
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    return render_template("user/login_page.html")


@user.route('/sign_in/', methods=['POST'])
def login_page2():
    email = request.form["email"]
    password = request.form["password"]

    user_1 = User.query.filter(User.email == email).first()
    if user_1 and user_1.check_password(password):
        try:
            remember_me = True if request.form["remember_me"] == "on" else False
        except:
            remember_me = False
        login_user(user_1,remember=remember_me)
        flash(f"Welcome {user_1.name} !","success")
    else:
        flash("Incorrect email or password","danger")
        return redirect(url_for(".login_page"))

    return redirect(url_for('home_page'))


@user.route("/sign_out")
@login_required
def logout():
    logout_user()
    flash("We looking forward to see you again !","success")
    return redirect(url_for("home_page"))


@user.route('/sign_up/')
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    return render_template("user/register_page.html")


@user.route('/sign_up/',methods=["POST"])
def register_page2():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    user1 = User.query.filter(User.email == email).first()
    user2 = User.query.filter(User.name == username).first()

    if user1:
        flash("User with this email address already exist.","danger")
        return render_template("user/register_page.html",username=username)
    elif user2:
        flash("User with this username already exist.","danger")
        return render_template("user/register_page.html", email=email)
    else:
        u = User(username,email)
        u.set_password(password)
        db_session.add(u)
        db_session.commit()
        flash("Welcome to our site !","success")
        login_user(u)
        return redirect(url_for("home_page"))


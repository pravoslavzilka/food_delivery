from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from models import User

user = Blueprint('user', __name__,template_folder='templates')


@user.route('/login/')
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    return render_template("user/login_page.html")


@user.route('/login/', methods=['POST'])
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


@user.route("/logout/")
@login_required
def logout():
    logout_user()
    flash("We looking forward to see you again !","success")
    return redirect(url_for("home_page"))


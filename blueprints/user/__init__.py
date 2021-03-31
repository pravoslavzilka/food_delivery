from flask import Blueprint, render_template

user = Blueprint('user', __name__,template_folder='templates')


@user.route('/hello')
def login_page():
    return render_template("user/login_page.html")
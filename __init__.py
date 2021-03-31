from flask import Flask, render_template
from blueprints.user.__init__ import user
from database import db_session
from flask_login import LoginManager
from models import User


app = Flask(__name__)
app.register_blueprint(user,url_prefix='/user')
app.secret_key = b'\xf4\xd48}\xeb\xefF5\x87|\xd6\xcd\x94\x02\xb2\x0f'

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "user.login_page"
login_manager.login_message = "Please sign in to access this page"
login_manager.login_message_category = "info"


@app.route("/")
def home_page():
    return render_template("index.html",text="hi there !")


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.run(debug=True)
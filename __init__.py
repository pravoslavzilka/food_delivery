from flask import Flask, render_template
from blueprints.user.__init__ import user
from database import db_session
from models import User


app = Flask(__name__)
app.register_blueprint(user,url_prefix='/user')


@app.route("/")
def home_page():
    return render_template("index.html",text="hi there !")



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.run(debug=True)
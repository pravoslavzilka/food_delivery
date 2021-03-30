from flask import Flask, render_template
from blueprints.user.__init__ import user


app = Flask(__name__)
app.register_blueprint(user,url_prefix='/user')


@app.route("/")
def home_page():
    return render_template("index.html",text="hi there !")


if __name__ == "__main__":
    app.run(debug=True)
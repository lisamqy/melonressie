from flask import Flask, session, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db

app = Flask(__name__)
app.secret_key = 'secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("homepage.html")

@app.route("/new", methods=['POST'])
def register():
    """New user registration page."""

    return render_template("register.html")   

@app.route("/reservation", methods=['POST'])
def make_reservation():
    """User reservations."""

    return render_template("reservation.html")       


if __name__ == "__main__":
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0")
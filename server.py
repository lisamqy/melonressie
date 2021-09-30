from flask import Flask, session, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """Show homepage."""
    
    if "current_user" in session:
        user = crud.get_user_by_id(session["current_user"])
    else: 
        user = None

    return render_template("homepage.html", user=user)

@app.route("/handle-login", methods=["POST"])
def handle_login():
    """Log user into application"""   
    
    username = request.form["username"]
    email = request.form["email"]
    user = crud.get_user_by_email(email) #communicates with db to grab existing users info from db
        
    if username == user.username and user.username!= None: #checks against database
        session["current_user"] = user.user_id #saves the current user's user_id in session
        flash(f'Logged in as {user.username}') 
        return redirect(f"/user/{user.user_id}")
    else:
        flash("Email or password incorrect, please try again.")
        return redirect("/")

@app.route("/goodbye")   
def logout():
    """Clear the session and return to homepage"""

    session.clear()
    return redirect("/")    

@app.route("/user/<user_id>")
def user_page(user_id):
    """Show user's account details"""

    user = crud.get_user_by_id(user_id)
    appts = crud.find_appt_by_user(user_id)

    return render_template("reservation.html", appts=appts)

@app.route("/reservation", methods=['POST'])
def make_reservation():
    """User reservations."""

    user_id = crud.get_user_by_id(session["current_user"])
    date = request.form["date"]
    time = request.form["start-time"]
    # print(f'\n\n{date} {time}\n\n')
    datetime = ",".join(date.split("-")) + "," + time + ":00"
    print(f'\n\n{datetime}\n\n')
    crud.create_appt(user_id, datetime)

    return redirect(f"/user/{user_id}")       


if __name__ == "__main__":
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0")
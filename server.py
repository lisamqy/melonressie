from flask import Flask, session, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """Show homepage."""
    
    if "current_user" in session:
        user = crud.get_user_by_id(session["current_user"])
        return redirect(f"/user/{user.user_id}") 
    else: 
        return render_template("homepage.html")

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
    end_times = []

    #grab all found appointment times associated user
    for dtime in appts:
        #create datetime object from timestamp string
        date_format_str = "%H:%M"
        dtime = dtime.datetime.strftime("%H:%M")
        given_time = datetime.strptime(dtime, date_format_str)

        n = 30 # Add 30 minutes to datetime object
        end_time = given_time + timedelta(minutes=n)
        # Convert datetime object to string in specific format 
        end_time_str = end_time.strftime('%H:%M')
        end_times.append(end_time_str)

    return render_template("reservation.html", packed=zip(appts, end_times))

@app.route("/reservation", methods=['POST'])
def make_reservation():
    """User reservations."""

    user_id = session["current_user"]
    date = request.form["date"]
    time = request.form["start-time"]

    date_time = ",".join(date.split("-")) + "," + time + ":00"
    print(f'\n\n{date_time}\n\n')

    #In case users try to book a reservation at the same date and time
    if crud.check_appt_time(date_time) < 1:
        crud.create_appt(user_id, date_time)
    else:
        flash(f'Time slot taken, please try another')

    return redirect(f"/user/{user_id}")       


if __name__ == "__main__":
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0")
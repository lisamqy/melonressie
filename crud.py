"""CRUD operations."""

from model import db, User, Appointment, connect_to_db


def create_user(username, email):
    """Create and return a new user"""

    user = User(username=username, email=email)
    
    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_id(num):   
    """Get user from database by their id."""    
    
    return User.query.filter_by(user_id=num).first()

def get_user_by_email(email):
    """Get a user by their email from database."""  

    return User.query.filter(User.email==email).first()    

def create_appt(user_id, datetime):
    """Reserves an appointment slot for a user"""

    appt = Appointment(user_id=user_id, datetime=datetime)

    db.session.add(appt)
    db.session.commit()

    return appt

def show_appts():
    """Show all appointsment in database."""
    #prob will use to doublecheck for dupe res

    return Appointment.query.all()

def find_appt_by_user(user_id):
    """Find any appointment(s) associated with a specific user_id"""

    return Appointment.query.filter_by(user_id=user_id).all()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
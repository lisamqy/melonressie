from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A User."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    
    # NOTE: a user can only have 1 reservation on a calendar date
    # find user's appt via user1.appt or appt1.user
    appt = db.relationship("Appointment", backref="users")
    

    def __repr__(self):
        """Show user's id and email."""
        return f"<User user_id={self.user_id} email={self.email}>"


class Appointment(db.Model):
    """Appointments created"""

    __tablename__ = "appts"

    appt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # reservation details; ex: time date etc 
    datetime = datetime = db.Column(db.DateTime)




def connect_to_db(app, db_uri="postgresql:///melon"):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print("Connected to DB.")

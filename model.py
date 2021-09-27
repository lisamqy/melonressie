from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A User."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    
    def __repr__(self):
        """Show user's id and email."""
        return f"<User user_id={self.user_id} | username={self.username} | email={self.email}>"


class Appointment(db.Model):
    """Appointments created"""

    __tablename__ = "appts"

    appt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    # reservation details; ex: time date etc 
    # ex format for entering -> Appointment(user_id=1, datetime='2022, 1, 24, 22:30:00')
    datetime = db.Column(db.DateTime)

    def __repr__(self):
        """Show user's appts."""
        return f"<Appointment: appt_id={self.appt_id} | User user_id={self.user_id} | datetime={self.datetime}>"


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

from enum import Enum

from werkzeug.security import generate_password_hash , check_password_hash

from app import db
from flask_login import UserMixin

class Roles(Enum):
    DEFAULT = 0
    MED_STUDENT = 1

class User ( UserMixin , db.Model ) :
    __tablename__ = 'users'

    # Table attributes
    id = db.Column ( db.Integer , primary_key=True )
    email = db.Column ( db.String ( 256 ) , unique=True , nullable=False )
    username = db.Column ( db.String ( 32 ) , unique=True , nullable=False )
    password = db.Column ( db.String ( 128 ) , nullable=False )
    gender = db.Column(db.String(32), nullable=False)
    role = db.Column ( db.Enum ( Roles , name="roles" ) , nullable=False )

    # Initialise
    def __init__ ( self , email , username , password , role = Roles.DEFAULT ) :
        # Encrypt the password before storing the data
        encrypted_pass = generate_password_hash ( password )

        self.email = email
        self.username = username
        self.password = encrypted_pass
        self.role = role

    # Returns True, if there is such a user and
    # the given password matches the actual password
    @staticmethod
    def check_user ( username , password ) :
        user = User.query.filter_by ( username=username ).first ()
        return user and check_password_hash ( user.password , password )

    # Returns True if the current User is Staff
    def is_med_student ( self ) :
        return self.role == Roles.MED_STUDENT

    def db_commit( self ) :
        db.session.add ( self )
        db.session.commit()
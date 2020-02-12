''' Admin model '''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import func
from config import *

PW_REGEX = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')

class Organizer(db.Model):
    __tablename__ = "organizers"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(225))
    last_name = db.Column(db.String(225))
    email = db.Column(db.String(225))
    password = db.Column(db.String(225))
    user_level = db.Column(db.String(225), default = 0)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr(self):
        return '<Organizer{}>'.format(self.first_name)

    def __repr(self):
        return '<Organizer{}>'.format(self.email)

# admin updat functions
    def update_firstName(self, new_fname):
        self.first_name = new_fname
        db.session.commit()
    def update_lastName(self, new_lname):
        self.last_name = new_lname
        db.session.commit()
    def update_email(self, new_email):
        self.email = new_email
        db.session.commit()
    def update_password(self, new_password):
        pwd_hash = bcrypt.generate_password_hash(new_password)
        self.password = pwd_hash
        db.session.commit()
    def make_admin(self):
        self.user_level = 10
        db.session.commit()
    def make_staff(self):
        self.user_level = 0
        db.session.commit()

#validate update admin & staff
    @classmethod
    def validate_password(cls,name):
        errors=[]
        return errors
    @classmethod
    def validate_email(cls,name):
        errors=[]
        return errors
    @classmethod
    def validate_info(cls,customer_info):
        errors=[]
        return errors
    
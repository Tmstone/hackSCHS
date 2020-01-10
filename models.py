from sqlalchemy.sql import func
from config import *

# database build and methods

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')
PHONE_REGEX=re.compile('^\d{3}-\d{3}-\d{4}$')

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(45), nullable = False)
    last_name = db.Column(db.String(45), nullable = False)
    email = db.Column(db.String(45), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    phone = db.Column(db.String(45), nullable = False)
    gender = db.Column(db.String(45), nullable = False)
    ethnicity = db.Column(db.String(45), nullable = False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    

class Gender(db.Model):
    __tablename__ = "genders"
    id = db.Column(db.Integer, primary_key = True)
    gender = db.Column(db.String(45), nullable = False)
#foriegn key here
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
#relationship here

class Ethnicity(db.Model):
    __tablename__ = "ethnicities"
    id = db.Column(db.Integer, primary_key = True)
    ethnicity = db.Column(db.String(45), nullable = False)
#foriegn key here
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
#relationship here

class School(db.Model):
    __tablename__ ="schools"
    id = db.Column.Integer, primary_key = True)
    school = db.Column(db.String(225), nullable = False)

    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

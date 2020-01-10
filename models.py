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
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
#relationships      

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
    id = db.Column(db.Integer, primary_key = True)
    school = db.Column(db.String(225), nullable = False)
    graduation = db.Column(db.String(45), nullable = False)
#foriegn key here
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
#relationship here

class Parent(db.Model):
    __tablename__ = "parents"
    id = db.Column(db.Integer, primary_key = True)
    parent_first = db.Column(db.String(45), nullable = False)
    parent_last = db.Column(db.String(45), nullable = False)  
    parent_phone = db.Column(db.String(45), nullable = False)
    parent_email = db.Column(db.String(45), nullable = False)

    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Bonus(db.Model):
    __tablename__ = "bonuses"
    id = db.Column(db.Integer, primary_key = True)


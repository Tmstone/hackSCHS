from sqlalchemy.sql import func
from config import *

# database build and methods

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')
PHONE_REGEX = re.compile('^\d{3}-\d{3}-\d{4}$')

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    password = db.Column(db.String(255))
    phone = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return '<User {}>'.format(self.first_name)
    
    @classmethod
    def validate_user(cls, email):
        errors=[]
        existing_users=cls.query.filter(cls.email==email).count()
        if (existing_users)>0:
            errors.append('This email address is already registered!')
        return errors

    @classmethod
    def validate_name(cls, first_name, last_name):
        errors=[]
        if len(first_name and last_name) < 2:
            errors.append('Please enter a valid name (*at least three characters*).')
        return errors

    @classmethod
    def validate_password(cls, password, confirm_password):
        errors=[]
        if not PW_REGEX.match(password):
            errors.append('* Please enter a valid password: 6-20 characters, A-Z and (# $ % @ &)')
        if password != confirm_password:
            errors.append('Passwords don\'t match.')
        return errors
    
    @classmethod
    def validate_email(cls, email):
        errors=[]
        if not EMAIL_REGEX.match(email):
            errors.append('Please enter a valid email.')
        return errors
    
    @classmethod
    def validate_phone(cls, phone):
        errors=[]
        if len(phone) < 7:
            errors.append('Please enter a valid number')
        return errors

    @classmethod
    def validate_school(cls, school):
        errors=[]
        if len(school) < 2:
            errors.append('Please enter a valid school name.')
        return errors    

    def validate_graduation(cls, graduation):
        errors=[]
        if len(school) < 4:
            errors.append('Please enter a valid year.')
        return errors 

    @classmethod
    def validate_parent(cls, parent_first, parent_last):
        errors=[]
        if len(parent_first and parent_last) < 2:
            errors.append('Please enter a parent name.')
        return errors
    
    @classmethod
    def validate_parent_phone(cls, parent_phone):
        errors=[]
        if not PHONE_REGEX.match(phone):
            errors.append('Please enter a valid phone number.')
        return errors

    @classmethod
    def validate_parent_email(cls, parent_email):
        errors = []
        if not EMAIL_REGEX.match(parent_email):
            errors.append('Please enter a valid parent email.')
        return errors
    
    @classmethod
    def validate_attendee(cls, attendee_info):
        errors = []
        errors += cls.validate_name(attendee_info['first_name'], attendee_info['last_name'])
        errors += cls.validate_password(attendee_info['password'])
        
        return errors

    @classmethod
    def new(cls, attendee_info):
    pw_hash = bcrypt.generate_password_hash(attendee_info['password'])    
    new_attendee=cls(first_name=attendee_info['first_name'], last_name=attendee_info['last_name'], )
    db.session.add(new_attendee)
    db.session.commit()
    return new_attendee

class Gender(db.Model):
    __tablename__ = "genders"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    gender = db.Column(db.String(45), nullable = False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    user=db.relationship('User',foreign_keys=[user_id],backref=db.backref("genders",cascade="all,delete-orphan"))

class Ethnicity(db.Model):
    __tablename__ = "ethnicities"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    ethnicity = db.Column(db.String(45), nullable = False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    user=db.relationship('User',foreign_keys=[user_id],backref=db.backref("ethnicities",cascade="all,delete-orphan"))

class School(db.Model):
    __tablename__ ="schools"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    school = db.Column(db.String(225), nullable = False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    user=db.relationship('User',foreign_keys=[user_id],backref=db.backref("schools",cascade="all,delete-orphan"))

class Graduation(db.Model):
    __tablename__ = "graduations"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    graduation = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    customer=db.relationship('User',foreign_keys=[user_id],backref=db.backref("graduations",cascade="all,delete-orphan"))

class Goal(db.Model):
    __tablename__ =  "goals"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    goal = db.Column(db.String(255))   
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    user=db.relationship('User',foreign_keys=[user_id],backref=db.backref("goals",cascade="all,delete-orphan"))

class Parent(db.Model):
    __tablename__ = "parents"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    parent_first = db.Column(db.String(45), nullable = False)
    parent_last = db.Column(db.String(45), nullable = False)  
    parent_phone = db.Column(db.String(45))
    parent_email = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    user=db.relationship('User',foreign_keys=[user_id],backref=db.backref("parents",cascade="all,delete-orphan"))

class Bonus(db.Model):
    __tablename__ = "bonuses"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    langage = db.Column(db.String(45))
    hobby = db.Column(db.String(45))   
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    user=db.relationship('User',foreign_keys=[user_id],backref=db.backref("bonuses",cascade="all,delete-orphan"))
    

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
            errors.append('Please enter a valid phone number')
        return errors

    @classmethod
    def validate_school(cls, school):
        errors=[]
        if len(school) < 2:
            errors.append('Please enter a valid school name.')
        return errors    

    @classmethod
    def validate_graduation(cls, graduation):
        errors=[]
        if len(graduation) < 4:
            errors.append('Please enter a valid year [yyyy].')
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
        if len(parent_phone) < 7:
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
        errors += cls.validate_email(attendee_info['email'])
        errors += cls.validate_password(attendee_info['password'], attendee_info['confirm_password'])
        errors += cls.validate_phone(attendee_info['phone'])
        errors += cls.validate_school(attendee_info['school'])
        errors += cls.validate_graduation(attendee_info['graduation'])
        errors += cls.validate_parent(attendee_info['parent_first'], attendee_info['parent_last'] )
        errors += cls.validate_parent_email(attendee_info['parent_email'])
        errors += cls.validate_parent_phone(attendee_info['parent_phone'])
        return errors

    @classmethod
    def add_user(cls, attendee_info):
        pw_hash = bcrypt.generate_password_hash(attendee_info['password'])    
        new_attendee = cls (
            first_name=attendee_info['first_name'], 
            last_name=attendee_info['last_name'],
            email=attendee_info['email'], 
            password=pw_hash, 
            phone=attendee_info['phone']
            )
        db.session.add(new_attendee)
        db.session.commit()
        gender = Gender.new(new_attendee.id, attendee_info)
        ethnicity = Ethnicity.new(new_attendee.id, attendee_info)
        school = School.new(new_attendee.id , attendee_info)
        graduation = Graduation.new(new_attendee.id, attendee_info)
        goal = Goal.new(new_attendee.id , attendee_info)
        parents = Parent.new(new_attendee.id, attendee_info)
        bonus = Bonus.new(new_attendee.id, attendee_info)
        return new_attendee
    
    @classmethod
    def edit_user(cls,user_id, form):
        user_update = User.query.get(session['user_id'])
        user_update.first_name = form['first_name']
        user_update.last_name = form['last_name']
        user_update.email = form['email']
        user_update.phone = form['phone']
        db.session.commit()
        return user_update.first_name
    
    @classmethod
    def get(cls, user_id):
        return cls.query.get(user_id)
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def validate_login(cls, form):
        user = cls.query.filter_by(email = form['email']).first()
        print(user)
        if user:
            if bcrypt.check_password_hash(user.password, form['password']):
                return user
        return None

class Gender(db.Model):
    __tablename__ = "genders"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    gender = db.Column(db.String(45), nullable = False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    user=db.relationship('User',foreign_keys=[user_id],backref=db.backref("genders",cascade="all,delete-orphan"))
    
    @classmethod
    def new(cls, user_id, gender):
        new_gender = cls(user_id=user_id, gender=gender['gender'])
        db.session.add(new_gender)
        db.session.commit()
        return new_gender
    @classmethod
    def get_all(cls):
        return cls.query.all()
    @classmethod
    def by_gender(cls, gender):
        return cls.query.filter(cls.gender==gender).first()

class Ethnicity(db.Model):
    __tablename__ = "ethnicities"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    ethnicity = db.Column(db.String(45), nullable = False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    user=db.relationship('User',foreign_keys=[user_id],backref=db.backref("ethnicities",cascade="all,delete-orphan"))

    @classmethod
    def new(cls, user_id, race):
        new_ethnicity = cls(user_id=user_id, ethnicity=race['ethnicity'])
        db.session.add(new_ethnicity)
        db.session.commit()
        return new_ethnicity
    @classmethod
    def get_all(cls):
        return cls.query.all()
    @classmethod
    def by_ethnicity(cls, race):
        return cls.query.filter(cls.race==race).first()

class School(db.Model):
    __tablename__ ="schools"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    school = db.Column(db.String(225), nullable = False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    user=db.relationship('User',foreign_keys=[user_id],backref=db.backref("schools",cascade="all,delete-orphan"))
    
    @classmethod
    def new(cls, user_id, school):
        new_school = cls(user_id=user_id, school=school['school'])
        db.session.add(new_school)
        db.session.commit()
        return new_school
    @classmethod
    def get(cls, user_id):
        return cls.query.get(user_id)
    @classmethod
    def get_all(cls):
        return cls.query.all()
    @classmethod
    def by_school(cls, school):
        return cls.query.filter(cls.school==school).first()

class Graduation(db.Model):
    __tablename__ = "graduations"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    graduation = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    customer=db.relationship('User',foreign_keys=[user_id],backref=db.backref("graduations",cascade="all,delete-orphan"))
    
    @classmethod
    def new(cls, user_id, year):
        new_graduation = cls(user_id=user_id, graduation=year['graduation'])
        db.session.add(new_graduation)
        db.session.commit()
        return new_graduation
    @classmethod
    def get_all(cls):
        return cls.query.all()
    @classmethod
    def by_gender(cls, year):
        return cls.query.filter(cls.year==year).first()

class Goal(db.Model):
    __tablename__ =  "goals"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    goal = db.Column(db.String(255))   
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    user=db.relationship('User',foreign_keys=[user_id],backref=db.backref("goals",cascade="all,delete-orphan"))
    
    @classmethod
    def new(cls, user_id, goal):
        new_goal = cls(user_id=user_id, goal=goal['goal'])
        db.session.add(new_goal)
        db.session.commit()
        return new_goal

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

    @classmethod
    def new(cls, user_id, parent):
        new_parent = cls(user_id=user_id, parent_first=parent['parent_first'], parent_last=parent['parent_last'],
        parent_phone=parent['parent_phone'], parent_email=parent['parent_email'])
        db.session.add(new_parent)
        db.session.commit()
        return new_parent
    
    @classmethod
    def edit_parent(cls,user_id, form):
        update_parent = Parent.query.get(session['user_id'])
        update_parent.parent_first = form['parent_first']
        update_parent.parent_last = form['parent_last']
        update_parent.parent_phone = form['parent_phone']
        update_parent.parent_email = form['parent_email']
        db.session.commit()
        return update_parent.parent_first

    @classmethod
    def get(cls, user_id):
        return cls.query.get(user_id)
    @classmethod
    def get_all(cls):
        return cls.query.all()   

class Bonus(db.Model):
    __tablename__ = "bonuses"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    langage = db.Column(db.String(45))
    hobby = db.Column(db.String(45))   
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    user=db.relationship('User',foreign_keys=[user_id],backref=db.backref("bonuses",cascade="all,delete-orphan"))
    
    @classmethod
    def new(cls, user_id, bonus):
        new_bonus = cls(user_id=user_id, langage=bonus['language'], hobby=bonus['hobby'])
        db.session.add(new_bonus)
        db.session.commit()
        return new_bonus
    @classmethod
    def get_all(cls):
        return cls.query.all()
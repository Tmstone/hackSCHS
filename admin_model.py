''' Admin model '''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import func
from config import *

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
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
    def validate_password(cls, password):
        errors=[]
        if not PW_REGEX.match(password) or password != password:
            errors.append('* Please enter a valid password: 6-20 characters, A-Z and (# $ % @ &)')
        if password == "":
            errors.append('Please enter a valid password')
        return errors

    @classmethod
    def validate_email(cls, email):
        errors=[]
        if not EMAIL_REGEX.match(email):
            errors.append('Please enter a valid email.')
        return errors

    @classmethod
    def create_default_admin(cls):
        '''
        Create a default administrator to start the database with.
        Normally you would call this only from a command line python session.
        '''
        admin_info={'first_name': 'default', 'last_name': 'admin', 'password': 'changeme', 'email':'admin@hackschs.info', 'user_level': '10'}
        admin=cls.new(admin_info)
        admin.make_admin()
        return admin
    @classmethod
    def validate_login(cls,form):
        '''
        form=['username':string,'password':string]
        '''
        # print(form)
        admin = cls.query.filter_by(email = form['email']).first()
        # print('*'*80,user)
        if admin:
            if admin.password == form['password'] or bcrypt.check_password_hash(admin.password, form['password']):
                return admin
        return None

    @classmethod
    def get_all_admins(cls):
        return cls.query.filter(cls.user_level>=6).all()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def is_logged_in_as_admin(cls,admin_id,login_session):
        user=cls.query.get(admin_id)
        print("employee id",admin_id)
        result=False
        if user:
            if bcrypt.check_password_hash(login_session,str(user.created_at)):
                if user.user_level>=6:
                    print("admin login_success")
                    result=True
        return result

    @classmethod
    def edit_user(cls,form):
        admin_update = Organizer.query.get(session['user_id'])
        admin_update.first_name = form['first_name']
        admin_update.last_name = form['last_name']
        admin_update.email = form['email']
        admin_update.user_level = form['user_level']
        db.session.commit()
        return admin_update.first_name
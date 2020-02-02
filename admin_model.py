''' Admin model '''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import func
from config import *


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

    
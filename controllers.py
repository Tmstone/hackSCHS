from flask import render_template, redirect, request, session, flash
from config import db, datetime
#from models import User

### Controller Functions ###
#render index
def index():
    return render_template('index.html')

#register user
def new_user():
    return render_template('register.html')
#login user

#admin login

#process form

#pull all records

#display dashboard
def dashboard():
    return render_template('dashboard.html')

#logout user
def logout():
    session.clear
    return redirect('/')

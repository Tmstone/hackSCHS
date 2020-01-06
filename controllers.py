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
def login():
    return redirect('/dash')

#admin login
def admin():
    return render_template('admindash.html')

#process form

#pull all records

#display dashboard
def dashboard():
    return render_template('dashboard.html')

#logout user
def logout():
    session.clear
    return redirect('/')

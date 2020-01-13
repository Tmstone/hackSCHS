from flask import render_template, redirect, request, session, flash
from config import db, datetime
from models import *

### Controller Functions ###
#render index
def index():
    return render_template('index.html')

#register form
def register():
    return render_template('register.html')

#Add new user
def new_user():
    errors = User.validate(request.form)
    if errors:
        for error in errors:
            flash(error)
        return redirect('/')
    user_id = User.add_user(request.form)
    session['user_id'] = user_id
    return redirect('/dashboard')

#login user
def login():
    return redirect('/dash')

##admin routes##
#admin dashboard
def admin():
    return render_template('admindash.html')

def pi():
    return render_template('login.html')

def admin_in():
    
    return redirect('/admindash')

#process registration form

#pull all records

#display dashboard
def dashboard():
    return render_template('dashboard.html')

#display user update page
def account():
    return render_template('account.html')

#logout user
def logout():
    session.clear
    return redirect('/')

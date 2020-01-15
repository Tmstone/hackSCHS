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
    errors = User.validate_attendee(request.form)
    if errors:
        for error in errors:
            flash(error)
        return redirect('/register')
    user = User.add_user(request.form)
    session['user_id'] = user.id
    return redirect('/dashboard')

#login user
def login():
    user = User.validate_login(request.form)
    if user:
        session['user_id'] = user.id
        session['first_name'] = user.first_name
        return redirect('/dashboard')
    flash('Email and password do not match')
    return redirect('/dashboard')

#Adding first name
def first():
    user = User.query.get(session['user_id'])
    print (user)
    return user.first_name

#display dashboard
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get(session['user_id'])
    session['first_name'] = user.first_name
    details = User.query.all()
    return render_template('dashboard.html',
    user = user, data = details
    )

#display user update page
def account():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get(session['user_id'])
    session['first_name'] = user.first_name
    return render_template('account.html',
    user = user
    )

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

#logout user
def logout():
    session.clear
    return redirect('/')

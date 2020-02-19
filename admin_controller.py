''' Admin controller '''
from flask import render_template, redirect, request, session, flash
from config import db, datetime
from admin_model import Organizer
from models import *

##admin routes##
#admin dashboard
def admin():
    if 'admin_id' not in session:
        return redirect('/')
    admin = session['first_name']
    attendees = User.get_all_users()
    #gender = Gender.by_gender(id)
    print(admin)
    print(attendees)
    return render_template('admindash.html',
    name = admin, hackers = attendees #, gender = gender
    )

def pi():
    return render_template('login.html')

#log in admin
def admin_in(): 
    admin = Organizer.validate_login(request.form)
    if admin:
        session['admin_id'] = admin.id
        session['first_name'] = admin.first_name
        print('*'*90)
        print(session['admin_id'], session['first_name'])
        return redirect('/admindash')
    flash('Email and password do not match')
    return redirect('/')

def admin_account():

    return render_template('adminaccount.html')


#pull all records

def admin_logout():
    session.clear()
    return redirect('/')
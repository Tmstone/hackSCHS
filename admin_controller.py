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
    schools = School.get_all()
    parents = Parent.get_all()
    #gender = Gender.by_gender(id)
    print('*'*80)
    print(admin)
    print(attendees)
    print(schools)
    print(parents)
    return render_template('admindash.html',
    name = admin, hackers = attendees, schools = schools, parents = parents
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
    if 'admin_id' not in session:
        return redirect('/')
    admin = session['first_name']
    return render_template('adminacc.html', name = admin)


#pull all records

def admin_logout():
    session.clear()
    return redirect('/')
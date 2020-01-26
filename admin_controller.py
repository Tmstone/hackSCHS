''' Admin controller '''
from flask import render_template, redirect, request, session, flash
from config import db, datetime
#from admin_models import Organizer

##admin routes##
#admin dashboard
def admin():
    if 'admin_id' not in session:
        return redirect('/')
    return render_template('admindash.html')

def pi():
    return render_template('login.html')

def admin_in():
    if 'admin_id' not in session:
        return redirect('/')
    return redirect('/admindash')


#pull all records

def admin_logout():
    session.clear()
    return redirect('/')
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
    return render_template('admindash.html')

def pi():
    return render_template('login.html')

def admin_in():
    if 'admin_id' not in session:
        return redirect('/')
    return redirect('/admindash')

def admin_account():
    return render_template('adminaccount.html')


#pull all records

def admin_logout():
    session.clear()
    return redirect('/')
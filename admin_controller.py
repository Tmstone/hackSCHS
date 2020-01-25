''' Admin controller '''





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
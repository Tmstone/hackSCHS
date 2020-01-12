from config import app
from controllers import *

### routing for all pages ###

###master Routes###
app.add_url_rule('/', view_func=index)
#logout user
app.add_url_rule('/logout', view_func=logout)

#register user page
app.add_url_rule('/register', view_func=register)
#add new user 
app.add_url_rule('/user/new', view_func=new_user, methods=['POST'])
#login user
app.add_url_rule('/login', view_func=login)


#display dashboard
app.add_url_rule('/dashboard', view_func=dashboard)

#display user update page
app.add_url_rule('/user/id', view_func=account)

#admin routes
app.add_url_rule('/raspberry', view_func=pi)
app.add_url_rule('/admin', view_func=admin_in, methods=['POST'])
app.add_url_rule('/admindash', view_func=admin)

#process form






#pull all records


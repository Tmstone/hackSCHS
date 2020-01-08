from config import app
from controllers import *

### routing for all pages ###

###master Routes###
app.add_url_rule('/', view_func=index)
#logout user
app.add_url_rule('/logout', view_func=logout)

#register user
app.add_url_rule('/register', view_func=new_user)

#login user
app.add_url_rule('/login', view_func=login)


#display dashboard
app.add_url_rule('/dash', view_func=dashboard)

#display user update page
app.add_url_rule('/user/id', view_func=account)

#admin login
app.add_url_rule('/admindash', view_func=admin)

#process form






#pull all records


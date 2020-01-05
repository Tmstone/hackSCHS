from config import app
from controllers import *

### routing for all pages ###

###master Routes###
app.add_url_rule('/', view_func=index)
app.add_url_rule('/logout', view_func=logout)

#register user
app.add_url_rule('/register', view_func=new_user)

#login user
#app.add_url_rule('/signin', view_func=log_in)
#logout user

#display dashboard
app.add_url_rule('/dash', view_func=dashboard)

#admin login

#process form

#pull all records


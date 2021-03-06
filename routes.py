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
app.add_url_rule('/login', view_func=login, methods=['POST'])

#display dashboard
app.add_url_rule('/dashboard', view_func=dashboard)

#display user update page
app.add_url_rule('/user/account', view_func=account)
#update user
app.add_url_rule('/user/update', view_func=update, methods=['POST'])



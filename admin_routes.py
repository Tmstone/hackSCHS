''' Admin routes '''
from config import app
from admin_controller import *


#admin routes
app.add_url_rule('/raspberry', view_func=pi)
app.add_url_rule('/admin', view_func=admin_in, methods=['POST'])
app.add_url_rule('/admindash', view_func=admin)
app.add_url_rule('/update/user', view_func=admin_account)
app.add_url_rule('/view/<id>/hacker', view_func=attendee)
app.add_url_rule('/admin/logout', view_func=admin_logout)

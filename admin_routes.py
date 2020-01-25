''' Admin routes 


#admin routes
app.add_url_rule('/raspberry', view_func=pi)
app.add_url_rule('/admin', view_func=admin_in, methods=['POST'])
app.add_url_rule('/admindash', view_func=admin)
'''
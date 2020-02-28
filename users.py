from models import User, Parent, db
users = User.get_all_users()
for user in users:
    print("Name: " + user.first_name + " " + user.last_name)
    print("Email: " + user.email)
print()
print()
contacts = Parent.get_all()
for contact in contacts:
    print("Name: " + contact.parent_first + " " + contact.parent_last)
    print("Email: " + contact.parent_email + " " + contact.parent_phone)

   
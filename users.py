from models import User, Parent, db
users = User.get_all_users()
counter = 0
for user in users:
    counter = counter + 1
    print(str(counter) + " Name: " + user.first_name + " " + user.last_name)
    print("Email: " + user.email)
print()
print()
contacts = Parent.get_all()
for contact in contacts:
    print(str(counter) + " Parent Name: " + contact.parent_first + " " + contact.parent_last)
    print("Parent Email: " + contact.parent_email + " " + "Parent Phone: " + contact.parent_phone)

   
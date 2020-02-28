from models import User, Parent, db
users = User.get_all_users()
counter = 0
parent_counter = 0
print("Attendees")
for user in users:
    counter = counter + 1
    print(str(counter) + " Name: " + user.first_name + " " + user.last_name)
    print("Email: " + user.email)
print()
print()
contacts = Parent.get_all()
print("Parent Contact")
for contact in contacts:
    parent_counter = parent_counter + 1
    print(str(parent_counter) + " Parent Name: " + contact.parent_first + " " + contact.parent_last)
    print("Parent Email: " + contact.parent_email + " " + "Parent Phone: " + contact.parent_phone)

   
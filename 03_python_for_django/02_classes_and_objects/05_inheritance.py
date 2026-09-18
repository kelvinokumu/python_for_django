"""
Inheritance A child class can inherit attributes and
methods from a parent class.
"""

class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} logged in.")


class Admin(User):
    def delete_user(self):
        print("User deleted.")

admin = Admin("Sean")

# Inherited method
admin.login()

# Method belonging to Admin
admin.delete_user()
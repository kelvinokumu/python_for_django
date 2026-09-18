"""
Methods

A method is a function defined inside a class.
"""


class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def greet(self):
        print(f"Welcome, {self.username}!")

    def display_profile(self):
        print("Username:", self.username)
        print("Email:", self.email)


user = User(
    "kelvin",
    "kelvin@example.com"
)

user.greet()

user.display_profile()